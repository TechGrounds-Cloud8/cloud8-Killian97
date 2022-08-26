from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct


my_ip="84.106.100.87/32"


# redundant port 80 allow all on webserver

class webvpc_sg_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)