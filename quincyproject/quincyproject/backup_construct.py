from aws_cdk import (
    Duration,
    RemovalPolicy,
    aws_backup as backup,
    aws_events as events,
)

from constructs import Construct


class backup_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)