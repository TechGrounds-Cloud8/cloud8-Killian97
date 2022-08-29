from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_backup as backup,
)

from constructs import Construct

# import seperate files
from quincyproject.vpc_construct import vpc_webserver_construct, vpc_managementserver_construct
from quincyproject.sg_construct import webvpc_sg_construct, managementvpc_sg_construct
from quincyproject.nacl_construct import nacl_construct
from quincyproject.s3_construct import s3_construct
from quincyproject.backup_construct import backup_construct
from quincyproject.asg_contruct import asg_construct
from quincyproject.lb_construct import lb_construct

trusted_ip="84.85.157.1/32"

class QuincyprojectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)



        ############################
        ###place both vpc's here###
        ############################

        self.vpc_webserver = vpc_webserver_construct(self, "VPC_1").vpc_webserver
        self.vpc_managementserver = vpc_managementserver_construct(self, "VPC_2").vpc_managementserver

        #################################################
        ###place Peering connection between the 2 VPC's##
        #################################################

        #This is where the VPC peering is enabled.
        VPC_Peering_connection = ec2.CfnVPCPeeringConnection(
            self, "VPCPeeringConnection",
            peer_vpc_id=self.vpc_managementserver.vpc_id,
            vpc_id=self.vpc_webserver.vpc_id,
        )

        #This is where the routing table for the adminserver is configured.
        for subnet in self.vpc_managementserver.public_subnets:
            ec2.CfnRoute(
                self, 
                id = f"{subnet.node.id} Managementserver Route Table",
                route_table_id = subnet.route_table.route_table_id,
                destination_cidr_block = "10.10.0.0/16", 
                vpc_peering_connection_id = VPC_Peering_connection.ref,
        )
        
        #This is where the routing table for the webserver is configured.
        for subnet in self.vpc_webserver.public_subnets:
            ec2.CfnRoute(
                self,
                id = f"{subnet.node.id} Webserver public subnet Route Table",
                route_table_id = subnet.route_table.route_table_id,
                destination_cidr_block = "10.20.0.0/16", 
                vpc_peering_connection_id = VPC_Peering_connection.ref,
        )

        #This is where the routing table for the private websever subnets is configured.
        for subnet in self.vpc_webserver.private_subnets:
            ec2.CfnRoute(
                self,
                id = f"{subnet.node.id} Webserver Private Subnet Route Table",
                route_table_id = subnet.route_table.route_table_id,
                destination_cidr_block = "10.20.0.0/16",
                vpc_peering_connection_id = VPC_Peering_connection.ref,
        )

        #################################
        ###Adding NACL's to both VPC's###
        #################################

        '''
        self.nacl_construct = nacl_construct(
            self, "nacl",
            vpc_webserver=self.vpc_webserver,
            vpc_managementserver=self.vpc_managementserver,
        )
        '''
        

        ##########################
        ###Calling webserver SG###
        ##########################

        self.SG_webserver = webvpc_sg_construct(
            self, "webvpc_sg",
            vpc=self.vpc_webserver,
        )

        ##################################################################
        ###call webserver asg construct + alb construct + request count###
        ##################################################################

        self.auto_scaling_group = asg_construct(
            self, "Auto_Scaling_Group",
            vpc_webserver=self.vpc_webserver,
            security_group=self.SG_webserver.SG_webserver,
            role=iam.Role(
                self, "Web template Role for S3",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                description="Webserver role"
            ),    
        )

        self.alb = lb_construct(
            self, "Web server ALB",
            vpc=self.vpc_webserver,
            asg=self.auto_scaling_group.auto_scaling_group,
        )

        self.auto_scaling_group.auto_scaling_group.scale_on_request_count(
            "request count auto scaling",
            target_requests_per_minute=250,
        )

        ###############################
        ###create webserver instance###
        ###############################

         #This is where the webserver is deployed. 
        instance_webserver = ec2.Instance(
            self, "Webserver",
            instance_type=ec2.InstanceType("t3.nano"),
            vpc = self.vpc_webserver,
            vpc_subnets = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PRIVATE_ISOLATED
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            security_group = self.SG_webserver.SG_webserver,
            key_name = "webmin_key_pair",
            role=iam.Role(
                self, "Role for S3",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                description="Webserver role"
            ),
            block_devices = [
                ec2.BlockDevice(
                    device_name = "/dev/xvda",
                    volume = ec2.BlockDeviceVolume.ebs(
                        volume_size = 8,
                        encrypted = True,
                        delete_on_termination = True,
                    )
                )
            ]
        )

        ######################################################
        ###Creating managementserver instance and calling the SG###
        ######################################################

        self.SG_managementserver = managementvpc_sg_construct(
            self, "managementvpc_sg",
            vpc=self.vpc_managementserver,
        )

        instance_managementserver = ec2.Instance(
            self, "Managementserver",
            instance_type= ec2.InstanceType("t3.nano"),
            vpc = self.vpc_managementserver,
            vpc_subnets = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PUBLIC
            ),
            machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
            security_group = self.SG_managementserver.SG_managementserver,
            key_name = "webmin_key_pair",
            block_devices = [
                ec2.BlockDevice(
                    device_name = "/dev/xvda",
                    volume = ec2.BlockDeviceVolume.ebs(
                        volume_size = 30,
                        encrypted = True,
                        delete_on_termination = True,
                    )
                )
            ]
        )

        # install user data open SSH on admin server
        instance_managementserver.user_data.for_windows()
        instance_managementserver.add_user_data(
            "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0",
            "Start-Service sshd",
            "Set-Service -Name sshd -StartupType 'Automatic'",
            "New-NetFirewallRule -Name sshd -DisplayName 'Allow SSH' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22",
        )

        ########################
        ###call on S3 bucket####
        ########################

        self.bucket = s3_construct(self, "Bucket with scripts")

        #############################
        ###User data for webserver###
        #############################
        
        file_script_path = instance_webserver.user_data.add_s3_download_command(
            bucket = self.bucket.bucket,
            bucket_key = "webserver.sh",            
        )

        instance_webserver.user_data.add_execute_file_command(file_path = file_script_path)

        instance_webserver.user_data.add_s3_download_command(
            bucket = self.bucket.bucket,
            bucket_key = "index.html",
            local_file = "/tmp/index.zip",
        )

        instance_webserver.user_data.add_commands("chmod 755 -R /var/www/html/")

        instance_webserver.user_data.add_commands("unzip /tmp/index.zip -d /var/www/html/")

        self.bucket.bucket.grant_read(instance_webserver)
        

        ###########################
        ###User data for ASGroup###
        ###########################

        # download the userdata for the auto scaling group instance
        asg_userdata = self.auto_scaling_group.user_data.add_s3_download_command(
            bucket=self.bucket.bucket,
            bucket_key="webserver.sh"
        )

        # execute the userdata file
        self.auto_scaling_group.user_data.add_execute_file_command(file_path=asg_userdata)

        # download the webpage folder for the asg instance
        self.auto_scaling_group.user_data.add_s3_download_command(
            bucket=self.bucket.bucket,
            bucket_key="index.zip",
            local_file="/tmp/index.zip",
        )

        # add command for the CLI so the html folder of apache can be overwritten
        self.auto_scaling_group.user_data.add_commands("chmod 755 -R /var/www/html/")
        # add command for the CLI to unzip the website.zip in the s3 bucket into the html folder we just allowed to be overwritten
        self.auto_scaling_group.user_data.add_commands("unzip /tmp/index.zip -d /var/www/html/")

        # give the web instance acces to read the s3 bucket
        self.bucket.bucket.grant_read(self.auto_scaling_group.auto_scaling_group)


        #########################
        ##########Back up#######
        #########################

        backup_plan = backup_construct(
            self, "backup_plan",
        )

        backup_plan.backup_plan.add_selection(
            "webserver_instance",
            resources=[backup.BackupResource.from_ec2_instance(instance_webserver)],
            allow_restores=True,
        )

       
        ##################################
        ###Show ALB DNS after deploying###
        ##################################

        CfnOutput(self, "DNS for lb", value=self.alb.alb.load_balancer_dns_name)