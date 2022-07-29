from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct


my_ip="84.85.157.1/32"


class webvpc_sg_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create and configure webserver Security Group
        self.webvpc_sg = ec2.SecurityGroup(
            self, "webvpc_sg",
            vpc=vpc,
            allow_all_outbound=True,
        )

        ## add inbound rules for the webvpc SG

        # add rule for allow all inbound HTTP traffic
        self.webvpc_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow all HTTP traffic from anywhere",
        )

        # add rule for allow all inbound HTTPS traffic
        self.webvpc_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow all HTTPS traffic from anywhere",
        )

        # add rule to allow inbound SSH from only admin server,
        self.webvpc_sg.connections.allow_from(ec2.Peer.ipv4("10.20.20.0/24"), ec2.Port.tcp(22))


class adminvpc_sg_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create and configure manageserver Security Group
        self.adminvpc_sg = ec2.SecurityGroup(
            self, "adminvpc_sg",
            vpc=vpc,
            allow_all_outbound=True,
        )

        ## add inbound rules for the Managevpc SG

        # add rule for allow all inbound HTTP traffic
        self.adminvpc_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            connection=ec2.Port.tcp(22),
            description="Allow all SSH traffic from my IP",
        )

        self.adminvpc_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            connection=ec2.Port.tcp(3389),
            description="Allow all RDP traffic from my anywhere",
        )

        self.adminvpc_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow all HTTP traffic from my anywhere",
        )

        self.adminvpc_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow all HTTPS traffic from my anywhere",
        )