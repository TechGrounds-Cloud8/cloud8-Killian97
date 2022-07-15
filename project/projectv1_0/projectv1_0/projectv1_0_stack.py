from aws_cdk import (
    CfnOutput,
    RemovalPolicy,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_s3_assets as Asset,
)
from constructs import Construct


my_ip="84.85.157.1/32"


class Projectv10Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #######################################
        ###Everything for the Webserver VPC###
        #######################################

        # Create and configure webserver VPC with 2 subnets both being public.
        vpc_webserver = ec2.Vpc(
            self, "app-prd-vpc",
            cidr="10.10.10.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PUBLIC)
            ]
        )

        # Create and configure webserver Security Group
        webvpc_sg = ec2.SecurityGroup(
            self, "webvpc_sg",
            vpc=vpc_webserver,
            allow_all_outbound=True,
        )

        ## add inbound rules for the webvpc SG

        # add rule for allow all inbound HTTP traffic
        webvpc_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow all HTTP traffic from anywhere",
        )

        # add rule for allow all inbound HTTPS traffic
        webvpc_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow all HTTPS traffic from anywhere",
        )

        # add rule to allow inbound SSH, STILL NEED TO EDIT THAT ONLY THE ADMIN SERVER CAN CONNECT WITH SSH
        webvpc_sg.add_egress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="allow SSH inbound"
        )


        # Create and configure webserver ec2 instance
        web_instance = ec2.Instance(
            self, "Web-Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            vpc=vpc_webserver,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            security_group=webvpc_sg,
            key_name="webmin_key_pair",
        )


        # create and configure NACL for webserver VPC
        webvpc_nacl = ec2.NetworkAcl(
            self, "web NACL",
            vpc=vpc_webserver,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC        
            )
        )       

        # add inbound and outbound rules for the webserver NACL
        webvpc_nacl.add_entry(
            id="Allow all inbound HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow all outbound HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow all inbound HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow all outbound HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow Ephemeral inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow Ephemeral outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow SSH inbound from adminserver",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=130,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        
        
        #######################################
        ###Everything for the adminserver VPC##
        #######################################

        # Create and configure adminserver VPC with 2 subnets both being public.
        vpc_manageserver = ec2.Vpc(
            self, "manage-prd-vpc",
            cidr="10.20.20.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PUBLIC)
            ],
        )

        # Create and configure manageserver Security Group
        managevpc_sg = ec2.SecurityGroup(
            self, "managevpc_sg",
            vpc=vpc_manageserver,
            allow_all_outbound=True,
        )

        ## add inbound rules for the Managevpc SG

        # add rule for allow all inbound HTTP traffic
        managevpc_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow all SSH traffic from anywhere",
        )

        # Create and configure manage ec2 instance
        manage_instance = ec2.Instance(
            self, "Manage-Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            vpc=vpc_manageserver,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            security_group=managevpc_sg,
            key_name="webmin_key_pair",
        )



        # create and configure NACL for management server VPC
        managevpc_nacl = ec2.NetworkAcl(
            self, "Admin NACL",
            vpc=vpc_manageserver,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC        
            )
        )

        managevpc_nacl.add_entry(
            id="Allow SSH inbound from pc with keypair",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        managevpc_nacl.add_entry(
            id="Allow SSH outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        managevpc_nacl.add_entry(
            id="Allow Ephemeral inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        managevpc_nacl.add_entry(
            id="Allow Ephemeral outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

      



        ###########################################
        ###Peering connection between the 2 VPC's##
        ###########################################

        # create peering connection between the webserver VPC and the management server vpc
        vpc_peer_connection = ec2.CfnVPCPeeringConnection(
            self, "VPC_peer_connection",
            peer_vpc_id=vpc_manageserver.vpc_id,
            vpc_id=vpc_webserver.vpc_id,
        )

        #################
        ###S3 buckets####
        #################

        # create and configure S3 bucket for post depploy scriip
        postdeployments3 = s3.Bucket(
            self, "post depployment bucket",
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            public_read_access=True,
        )

        # upload files from post launch scripts folder into post deployment S3 bucket 
        userdata_upload = s3deploy.BucketDeployment(
            self, "postdeploy upload",
            destination_bucket=postdeployments3,
            sources=[s3deploy.Source.asset("./post_launch_scripts")],
        )

        web_userdata = web_instance.user_data.add_s3_download_command(
            bucket=postdeployments3,
            bucket_key="web_userdata.sh"
        )

        web_instance.user_data.add_execute_file_command(file_path=web_userdata)