from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct


trusted_ip="84.85.157.1/32"


class vpc_webserver_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc_webserver = ec2.Vpc(
            self, "VPC_1",
            cidr="10.10.0.0/16",
            max_azs=3,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="private", 
                    cidr_mask=24, 
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                ),
                ec2.SubnetConfiguration(
                    name ="public",
                    cidr_mask = 24,
                    subnet_type = ec2.SubnetType.PUBLIC
                )
            ]
        )



class vpc_managementserver_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc_managementserver = ec2.Vpc(
            self, "VPC_2",
            cidr="10.20.0.0/16",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public", 
                    cidr_mask=24, 
                    subnet_type=ec2.SubnetType.PUBLIC),
                ]
        )