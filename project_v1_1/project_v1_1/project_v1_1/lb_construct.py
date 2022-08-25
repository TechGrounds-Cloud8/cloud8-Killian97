from aws_cdk import (
    Duration,
    aws_elasticloadbalancingv2 as elbv2,
    aws_certificatemanager as acm,
    aws_acmpca as acmpa
)

from constructs import Construct


class lb_construct(Construct):
    def __init__(self, scope: Construct, construct_id: str, vpc, asg, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #create and configure the Application Load Balancer
        self.alb = elbv2.ApplicationLoadBalancer(
            self, "Application Load Balancer",
            vpc=vpc,
            internet_facing=True,       
        )

        # redirect all incoming port 80 http to port 443 https ( http to https = default)
        self.alb.add_redirect()

        # call for the cert arn
        arn = "arn:aws:acm:eu-central-1:663303000432:certificate/7a324a63-01ba-438c-b7a6-95b6b4e4aecb"

        # call the certificate itself
        certificate = acm.Certificate.from_certificate_arn(self, "Certificate", arn)
        

        # create a listener for HTTPS
        https_listener = self.alb.add_listener(
            "Listener for HTTPS",
            port=443,
            open=True,
            ssl_policy=elbv2.SslPolicy.FORWARD_SECRECY_TLS12,
            certificates=[certificate],
        )

        # create target group for the https listener
        asg_target_group = https_listener.add_targets(
            "ASG webserver",
            port=80,
            targets=[asg],
            health_check=elbv2.HealthCheck(
                enabled=True,
                port="80",
            ),
            stickiness_cookie_duration=Duration.minutes(5),
            stickiness_cookie_name="pbc",
        )