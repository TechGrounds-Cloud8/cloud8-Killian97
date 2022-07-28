from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct


my_ip="84.85.157.1/32"


class vpc_webserver_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)