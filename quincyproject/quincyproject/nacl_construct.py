from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct


trusted_ip="84.85.157.1/32"


class nacl_construct(Construct):
    
    def __init__(self, scope: Construct, construct_id: str, vpc_webserver, vpc_managementserver, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        ##############################################
        ###Create NACL for webserver private subnet###
        ##############################################

        # create and configure NACL for webserver VPC
        NACL_webserver_private = ec2.NetworkAcl(
            self, "Webserver private NACL",
            vpc = vpc_webserver,
            subnet_selection = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PRIVATE_ISOLATED
            )
        )

        #This is where I add the inbound Ephemeral rule for the webserver NACL.
        NACL_webserver_private.add_entry(
            id = "Allow inbound Ephemeral traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound Ephemeral rule for the webserver NACL.
        NACL_webserver_private.add_entry(
            id = "Allow outbound Ephemeral traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound SSH rule for the webserver NACL.
        NACL_webserver_private.add_entry(
            id = "Allow inbound SSH traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )


        ##############################################
        ###Create NACL for webserver public subnet###
        ##############################################

        # create and configure NACL for webserver VPC
        NACL_webserver_public = ec2.NetworkAcl(
            self, "Webserver public NACL",
            vpc = vpc_webserver,
            subnet_selection = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PUBLIC
            )
        )

        #This is where I add the inbound HTTP rule for the webserver NACL.
        NACL_webserver_public.add_entry(
            id = "Allow inbound HTTP traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTP rule for the webserver NACL.
        NACL_webserver_public.add_entry(
            id = "Allow outbound HTTP traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound HHTPS rule for the webserver NACL.
        NACL_webserver_public.add_entry(
            id = "Allow HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTPS rule for the webserver NACL.
        NACL_webserver_public.add_entry(
            id = "Allow outbound HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound Ephemeral rule for the webserver NACL.
        NACL_webserver_public.add_entry(
            id = "Allow inbound Ephemeral traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound Ephemeral rule for the webserver NACL.
        NACL_webserver_public.add_entry(
            id = "Allow outbound Ephemeral traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound SSH rule for the webserver NACL.
        NACL_webserver_public.add_entry(
            id = "Allow inbound SSH traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )


        ######################################
        ###Create NACL for managementserver###
        ######################################

        # create and configure NACL for management server VPC
        #Create a NACL for the managementserver.
        NACL_managementserver = ec2.NetworkAcl(
            self, "Managementserver NACL",
            vpc = vpc_managementserver,
            subnet_selection = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PUBLIC
            )
        )

        # add inbound and outbound rules for the adminserver NACL
        #This is where I add the inbound SSH rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow inbound SSH traffic",
            cidr = ec2.AclCidr.ipv4(trusted_ip), 
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound SSH rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound SSH traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound Ephemeral for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow inbound Ephemeral",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 140,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound Ephemeral for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound Ephemeral",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 140,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound RDP for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow inbound RDP",
            cidr = ec2.AclCidr.ipv4(trusted_ip), 
            rule_number = 150,
            traffic = ec2.AclTraffic.tcp_port(3389),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound RDP for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound RDP",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 150,
            traffic = ec2.AclTraffic.tcp_port(3389),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound HTTP rule for the Managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow inbound HTTP traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 160,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTP rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound HTTP traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 160,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound HHTPS rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 170,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTPS rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 170,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )