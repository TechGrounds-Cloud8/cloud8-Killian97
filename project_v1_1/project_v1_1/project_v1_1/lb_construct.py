from aws_cdk import (
    aws_elasticloadbalancingv2 as elbv2,
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

        # create a listener for HTTPS
        https_listener = self.alb.add_listener(
            "Listener for HTTPS",
            port=443,
            open=True,
            ssl_policy=elbv2.SslPolicy.FORWARD_SECRECY_TLS12,
        )

        # create target group for the https listener
        asg_target_group = https_listener.add_targets(
            "ASG webserver",
            port=80,
            targets=[asg],
            health_check=elbv2.HealthCheck(
                enabled=True,
                port=80,
            )
        )