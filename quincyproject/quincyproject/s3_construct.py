from aws_cdk import (
    aws_s3 as s3,
    Duration,
    RemovalPolicy,
    aws_s3_deployment as s3deploy,
)

from constructs import Construct


class s3_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)