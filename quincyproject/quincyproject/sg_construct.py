from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct


trusted_ip="84.106.100.87/32"


# redundant port 80 allow all on webserver

class webvpc_sg_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Create a security group for the webserver.
        self.SG_webserver = ec2.SecurityGroup(
            self, "Webserver SG",
            vpc=vpc,
            allow_all_outbound=True
        )

        #Create a rule that allow SSH from the admin server.
        self.SG_webserver.connections.allow_from(
            ec2.Peer.ipv4("10.20.0.0/16"), ec2.Port.tcp(22))


class managementvpc_sg_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Create a security group for the management server.
        SG_managementserver = ec2.SecurityGroup(
            self, "Managementserver SG",
            vpc=vpc,
            allow_all_outbound=True
        )

        #Create a rule that allows SSH connection from a trusted IP.
        SG_managementserver.add_ingress_rule(
            ec2.Peer.ipv4(trusted_ip),
            ec2.Port.tcp(22),
        )

        #Create a rule that allows RDP connection from a trusted IP.
        SG_managementserver.add_ingress_rule(
            ec2.Peer.ipv4(trusted_ip),
            ec2.Port.tcp(3389),
        )

        #Create a rule that allows HTTP traffic.
        SG_managementserver.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
        )

        #Create a rule that allows HTTPS traffic. 
        SG_managementserver.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),       
        )