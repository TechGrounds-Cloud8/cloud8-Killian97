from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

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
                    subnet_type=ec2.SubnetType.PUBLIC),
            ]
        )

        web_instance = ec2.Instance(
            self, "Web-Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            vpc=vpc_webserver,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            )
            user_data=
        )
        # kan dingen later na de instance creation ook nog toevoegen
        # web_instance.add_user_data
