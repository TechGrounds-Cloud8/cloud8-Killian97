from multiprocessing.sharedctypes import Value
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

with open("./post_launch_scripts/web_userdata.sh") as f:
    web_userdata = f.read()

class Projectv10Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #######################################
        ###Everything for the Webserver VPC###
        #######################################

        # Create VPC with 2 subnets both being public.
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
            user_data=ec2.UserData.custom(web_userdata)
        )

        web_instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80)
        )

        CfnOutput(self, "Output",
            value=web_instance.instance_public_ip
        )



        #######################################
        ###Everything for the adminserver VPC##
        #######################################

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
            ]
        )        
