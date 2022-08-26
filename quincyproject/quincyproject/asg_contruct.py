from aws_cdk import (
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
)

from constructs import Construct


class asg_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc_webserver, security_group, role, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)