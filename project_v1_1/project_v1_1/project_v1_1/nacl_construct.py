from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct


my_ip="84.85.157.1/32"


class nacl_construct(Construct):
    
    def __init__(self, scope: Construct, construct_id: str, vpc_webserver, vpc_adminserver, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ###############################
        ###Create NACL for webserver###
        ###############################

        # create and configure NACL for webserver VPC
        webvpc_nacl = ec2.NetworkAcl(
            self, "web NACL",
            vpc=vpc_webserver,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC        
            )
        )       

        # add inbound and outbound rules for the webserver NACL

        webvpc_nacl.add_entry(
            id="Allow all inbound HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow all outbound HTTP",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow all inbound HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow all outbound HTTPS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow Ephemeral inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow Ephemeral outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        webvpc_nacl.add_entry(
            id="Allow SSH inbound from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=130,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )


        #################################
        ###Create NACL for adminserver###
        #################################

        # create and configure NACL for management server VPC
        adminvpc_nacl = ec2.NetworkAcl(
            self, "Admin NACL",
            vpc=vpc_adminserver,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC        
            )
        )

        # add inbound and outbound rules for the adminserver NACL

        adminvpc_nacl.add_entry(
            id="Allow SSH inbound from pc with keypair",
            cidr=ec2.AclCidr.ipv4(my_ip),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        adminvpc_nacl.add_entry(
            id="Allow SSH outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        adminvpc_nacl.add_entry(
            id="Allow Ephemeral inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        adminvpc_nacl.add_entry(
            id="Allow Ephemeral outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        adminvpc_nacl.add_entry(
            id="Allow RDP inbound",
            cidr=ec2.AclCidr.ipv4(my_ip),
            rule_number=220,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        adminvpc_nacl.add_entry(
            id="Allow RDP outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=220,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        adminvpc_nacl.add_entry(
            id="Allow HTTP inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        adminvpc_nacl.add_entry(
            id="Allow HTTP outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        adminvpc_nacl.add_entry(
            id="Allow HTTPS inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=240,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW,
        )

        adminvpc_nacl.add_entry(
            id="Allow HTTPS outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=240,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )


