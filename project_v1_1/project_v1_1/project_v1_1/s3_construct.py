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

        #################
        ###S3 buckets####
        #################

        # create and configure S3 bucket for post depploy scriip
        self.postdeployments3 = s3.Bucket(
            self, "post_depployment_bucket",
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        # upload files from post launch scripts folder into post deployment S3 bucket 
        self.userdata_upload = s3deploy.BucketDeployment(
            self, "postdeploy upload",
            destination_bucket=self.postdeployments3,
            sources=[s3deploy.Source.asset("./post_launch_scripts")],
        )