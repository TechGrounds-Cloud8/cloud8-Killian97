from aws_cdk import (
    Duration,
    aws_elasticloadbalancingv2 as elbv2,
    aws_certificatemanager as acm
)

from constructs import Construct


class lb_construct(Construct):
    def __init__(self, scope: Construct, construct_id: str, vpc, asg, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)