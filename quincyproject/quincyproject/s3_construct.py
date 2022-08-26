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

        self.bucket = s3.Bucket(
            self, "Bucket with scripts",
            enforce_ssl = True,
            encryption = s3.BucketEncryption.S3_MANAGED,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects = True,
        )

        self.user_data_upload = s3deploy.BucketDeployment(
            self, "Deploy_assets_dir",
            destination_bucket = self.bucket,
            sources = [s3deploy.Source.asset("./Assets")],
        )