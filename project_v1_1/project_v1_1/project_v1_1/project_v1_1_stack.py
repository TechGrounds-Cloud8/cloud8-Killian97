
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_backup as backup,
)

from constructs import Construct

# import seperate files
from project_v1_1.vpc_construct import vpc_webserver_construct, vpc_adminserver_construct
from project_v1_1.sg_construct import webvpc_sg_construct, adminvpc_sg_construct
from project_v1_1.nacl_construct import nacl_construct
from project_v1_1.s3_construct import s3_construct
from project_v1_1.backup_construct import backup_construct
from project_v1_1.asg_contruct import asg_construct
from project_v1_1.lb_construct import lb_construct


my_ip="84.85.157.1/32"


class ProjectV11Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        ############################
        ###Calling on both VPC's ###
        ############################

        self.vpc_webserver = vpc_webserver_construct(self, "app-prd-vpc").vpc_webserver
        self.vpc_adminserver = vpc_adminserver_construct(self, "manage-prd-vpc").vpc_adminserver


        ###########################################
        ###Peering connection between the 2 VPC's##
        ###########################################

        # create peering connection between the webserver VPC and the management server vpc
        vpc_peer_connection = ec2.CfnVPCPeeringConnection(
            self, "VPC_peer_connection",
            peer_vpc_id=self.vpc_adminserver.vpc_id,
            vpc_id=self.vpc_webserver.vpc_id,
        )

        for subnet in self.vpc_webserver.private_subnets:
            ec2.CfnRoute(
                self,
                id=f"${subnet.node.id} Peer",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.20.0.0/16",
                vpc_peering_connection_id=vpc_peer_connection.ref,
            )

        for subnet in self.vpc_webserver.public_subnets:
            ec2.CfnRoute(
                self,
                id=f"${subnet.node.id} Peer",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.20.0.0/16",
                vpc_peering_connection_id=vpc_peer_connection.ref,
            )
        
        for subnet in self.vpc_adminserver.public_subnets:
            ec2.CfnRoute(
                self, 
                id=f"${subnet.node.id} Peer",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.10.0.0/16",
                vpc_peering_connection_id=vpc_peer_connection.ref,
            )


        #################################
        ###Adding NACL's to both VPC's###
        #################################

        self.nacl = nacl_construct(
            self, "nacl",
            vpc_webserver=self.vpc_webserver,
            vpc_adminserver=self.vpc_adminserver,
        )


        ####################################################
        ###Creating webserver instance and calling the SG###
        ####################################################

        self.webvpc_sg = webvpc_sg_construct(
            self, "webvpc_sg",
            vpc=self.vpc_webserver,
        )

        ##############################################################
        ###Webserver Load balancing and creating webserver instance###
        ##############################################################

        self.as_group = asg_construct(
            self, "Auto_Scaling_Group",
            vpc_webserver=self.vpc_webserver,
            security_group=self.webvpc_sg.webvpc_sg,
            role=iam.Role(
                self, "Web template Role for S3",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                description="Webserver role"
            ),    
        )

        self.alb = lb_construct(
            self, "Web server ALB",
            vpc=self.vpc_webserver,
            asg=self.as_group.as_group,
        )

        self.as_group.as_group.scale_on_request_count(
            "request count auto scaling",
            target_requests_per_minute=250,
        )
        
        
        web_instance = ec2.Instance(
            self, "Web-Instance",
            instance_type=ec2.InstanceType("t3.nano"),
            vpc=self.vpc_webserver,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            security_group=self.webvpc_sg.webvpc_sg,
            key_name="webmin_key_pair",
            role=iam.Role(
                self, "Role for S3",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                description="Webserver role"
            ),
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=True,    
                    )
                )
            ]
        )
        

        
        ######################################################
        ###Creating adminserver instance and calling the SG###
        ######################################################

        self.adminvpc_sg = adminvpc_sg_construct(
            self, "adminvpc_sg",
            vpc=self.vpc_adminserver,
        )

        # Create and configure manage ec2 instance
        admin_instance = ec2.Instance(
            self, "Admin-Instance",
            instance_type=ec2.InstanceType("t3.nano"),
            vpc=self.vpc_adminserver,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
            security_group=self.adminvpc_sg.adminvpc_sg,
            key_name="webmin_key_pair",
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=True,    
                    )
                )
            ]
        )

        # install open SSH on admin server
        admin_instance.user_data.for_windows()
        admin_instance.add_user_data(
            "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0",
            "Start-Service sshd",
            "Set-Service -Name sshd -StartupType 'Automatic'",
            "New-NetFirewallRule -Name sshd -DisplayName 'Allow SSH' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22",
        )


        ################
        ###S3 bucket####
        ################

        # calling the post deployment S3 bucket
        self.postdeployments3 = s3_construct(self, "post_depployment_bucket")


        #############################
        ###User data for webserver###
        #############################
        
        # download the userdata for the web instance
        web_userdata = web_instance.user_data.add_s3_download_command(
            bucket=self.postdeployments3.postdeployments3,
            bucket_key="user_data_web.sh"
        )

        # execute the userdata file
        web_instance.user_data.add_execute_file_command(file_path=web_userdata)

        # download the webpage folder for the web instance
        web_instance.user_data.add_s3_download_command(
            bucket=self.postdeployments3.postdeployments3,
            bucket_key="demo_website.zip",
            local_file="/tmp/demo_website.zip",
        )

        # add command for the CLI so the html folder of apache can be overwritten
        web_instance.user_data.add_commands("chmod 755 -R /var/www/html/")
        # add command for the CLI to unzip the website.zip in the s3 bucket into the html folder we just allowed to be overwritten
        web_instance.user_data.add_commands("unzip /tmp/demo_website.zip -d /var/www/html/")
        
        # give the web instance acces to read the s3 bucket
        self.postdeployments3.postdeployments3.grant_read(web_instance)
        

        ###########################
        ###User data for ASGroup###
        ###########################

        # download the userdata for the auto scaling group instance
        asg_userdata = self.as_group.user_data.add_s3_download_command(
            bucket=self.postdeployments3.postdeployments3,
            bucket_key="user_data_web.sh"
        )

        # execute the userdata file
        self.as_group.user_data.add_execute_file_command(file_path=asg_userdata)

        # download the webpage folder for the asg instance
        self.as_group.user_data.add_s3_download_command(
            bucket=self.postdeployments3.postdeployments3,
            bucket_key="demo_website.zip",
            local_file="/tmp/demo_website.zip",
        )

        # add command for the CLI so the html folder of apache can be overwritten
        self.as_group.user_data.add_commands("chmod 755 -R /var/www/html/")
        # add command for the CLI to unzip the website.zip in the s3 bucket into the html folder we just allowed to be overwritten
        self.as_group.user_data.add_commands("unzip /tmp/demo_website.zip -d /var/www/html/")

        # give the web instance acces to read the s3 bucket
        self.postdeployments3.postdeployments3.grant_read(self.as_group.as_group)

        #########################
        ##########Back up#######
        #########################

        # call on the back up plan
        
        back_up_plan = backup_construct(
            self, "backup_plan",
        )

        # define what needs to be backed up
        back_up_plan.back_up_plan.add_selection(
            "webserver_instance",
            resources=[backup.BackupResource.from_ec2_instance(web_instance)],
            allow_restores=True,
        )
        

        CfnOutput(self, "DNS for lb", value=self.alb.alb.load_balancer_dns_name)