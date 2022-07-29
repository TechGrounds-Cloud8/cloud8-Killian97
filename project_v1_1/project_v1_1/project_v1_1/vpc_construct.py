from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct


my_ip="84.85.157.1/32"


class vpc_webserver_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ################################
        ###Creating the Webserver VPC###
        ################################

        # Create and configure webserver VPC with 2 subnets both being public.
        self.vpc_webserver = ec2.Vpc(
            self, "app-prd-vpc",
            cidr="10.10.10.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Web_VPC", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PUBLIC)
            ],
        )


class vpc_adminserver_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ##################################
        ###Creating the Adminserver VPC###
        ##################################

        # Create and configure adminserver VPC with 2 subnets both being public.
        self.vpc_adminserver = ec2.Vpc(
            self, "manage-prd-vpc",
            cidr="10.20.20.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Admin_VPC", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PUBLIC)
            ],
        )