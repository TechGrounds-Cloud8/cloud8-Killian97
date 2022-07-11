from multiprocessing.sharedctypes import Value
from pickle import TRUE
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct



class Projectv10Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #######################################
        ###Everything for the Webserver VPC###
        #######################################

        # Create and configure webserver VPC with 2 subnets both being public.
        vpc_webserver = ec2.Vpc(
            self, "app-prd-vpc",
            cidr="10.10.10.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PUBLIC)
            ]
        )

        # Create and configure webserver ec2 instance
        web_instance = ec2.Instance(
            self, "Web-Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            vpc=vpc_webserver,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
        )

        # Create and configure webserver Security Group
        webvpc_sg = ec2.SecurityGroup(
            self, "webvpc_sg",
            vpc=vpc_webserver,
            allow_all_outbound=TRUE,
        )

        ## add inbound rules for the webserver vpc SG

        # add rule for allow all inbound HTTP traffic
        webvpc_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow all HTTP traffic from anywhere",
        )

        # add rule for allow all inbound HTTPS traffic
        webvpc_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "Allow all HTTPS traffic from anywhere",
        )

        #######################################
        ###Everything for the adminserver VPC##
        #######################################

        # Create and configure adminserver VPC with 2 subnets both being public.
        vpc_manageserver = ec2.Vpc(
            self, "manage-prd-vpc",
            cidr="10.20.20.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PUBLIC)
            ]
        )        


        ###########################################
        ###Peering connection between the 2 VPC's##
        ###########################################

        # create peering connection between the webserver VPC and the management server vpc
        vpc_peer_connection = ec2.CfnVPCPeeringConnection(
            self, "VPC_peer_connection",
            peer_vpc_id=vpc_manageserver.vpc_id,
            vpc_id=vpc_webserver.vpc_id,
        )