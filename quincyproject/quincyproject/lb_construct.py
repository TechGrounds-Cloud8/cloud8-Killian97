from aws_cdk import (
    Duration,
    aws_elasticloadbalancingv2 as elbv2,
    aws_certificatemanager as acm
)

from constructs import Construct


class lb_construct(Construct):
    def __init__(self, scope: Construct, construct_id: str, vpc, asg, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.alb = elbv2.ApplicationLoadBalancer(
            self, "alb",
            vpc = vpc
            internet_facing = True,
        )

        self.alb.add_redirect()

        arn = "arn:aws:acm:eu-central-1:663303000432:certificate/7a324a63-01ba-438c-b7a6-95b6b4e4aecb"

        certificate = acm.Certificate.from_certificate_arn(self, "Certificate", arn)

        #This is the listener for HTTPS
        listener = self.alb.add_listener(
            "listener",
            port = 443,
            open = True, 
            certificates = [certificate],
            ssl_policy = elbv2.SslPolicy.FORWARD_SECRECY_TLS12,
        )

        target_group = listener.add_targets(
            "TG",
            port = 80,
            targets = [asg],
            health_check = elbv2.HealthCheck(
                port = "80",
                enabled = True,
            ),
            stickiness_cookie_duration = Duration.minutes(5),
            stickiness_cookie_name = "scn",
        )