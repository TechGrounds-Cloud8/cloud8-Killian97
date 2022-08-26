from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_backup as backup,
)

from constructs import Construct

# import seperate files
from quincyproject.vpc_construct import vpc_webserver_construct, vpc_managementserver_construct
from quincyproject.sg_construct import webvpc_sg_construct, managementvpc_sg_construct
from quincyproject.nacl_construct import nacl_construct
from quincyproject.s3_construct import s3_construct
from quincyproject.backup_construct import backup_construct
from quincyproject.asg_contruct import asg_construct
from quincyproject.lb_construct import lb_construct


class QuincyprojectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)



        ############################
        ###place both vpc's here###
        ############################

        self.vpc_webserver = vpc_webserver_construct(self, "VPC_1").vpc_webserver
        self.vpc_managementserver = vpc_managementserver_construct(self, "VPC_2").vpc_managementserver

        #################################################
        ###place Peering connection between the 2 VPC's##
        #################################################

        #This is where the VPC peering is enabled.
        VPC_Peering_connection = ec2.CfnVPCPeeringConnection(
            self, "VPCPeeringConnection",
            peer_vpc_id=self.vpc_managementserver.vpc_id,
            vpc_id=self.vpc_webserver.vpc_id,
        )

        #This is where the routing table for the adminserver is configured.
        for subnet in self.vpc_managementserver.public_subnets:
            ec2.CfnRoute(
                self, 
                id = f"{subnet.node.id} Managementserver Route Table",
                route_table_id = subnet.route_table.route_table_id,
                destination_cidr_block = "10.10.0.0/24", 
                vpc_peering_connection_id = VPC_Peering_connection.ref,
        )
        
        #This is where the routing table for the webserver is configured.
        for subnet in self.vpc_webserver.public_subnets:
            ec2.CfnRoute(
                self,
                id = f"{subnet.node.id} Webserver public subnet Route Table",
                route_table_id = subnet.route_table.route_table_id,
                destination_cidr_block = "10.20.0.0/24", 
                vpc_peering_connection_id = VPC_Peering_connection.ref,
        )

        #This is where the routing table for the private websever subnets is configured.
        for subnet in self.vpc_webserver.private_subnets:
            ec2.CfnRoute(
                self,
                id = f"{subnet.node.id} Webserver Private Subnet Route Table",
                route_table_id = subnet.route_table.route_table_id,
                destination_cidr_block = "10.20.0.0/24", 
                vpc_peering_connection_id = VPC_Peering_connection.ref,
        )

        #################################
        ###Adding NACL's to both VPC's###
        #################################

        self.nacl_construct = nacl_construct(
            self, "nacl",
            vpc_webserver=self.vpc_webserver,
            vpc_adminserver=self.vpc_managementserver,
        )

        ##########################
        ###Calling webserver SG###
        ##########################

        self.SG_webserver = webvpc_sg_construct(
            self, "webvpc_sg",
            vpc=self.vpc_webserver,
        )

        ##################################################################
        ###call webserver asg construct + alb construct + request count###
        ##################################################################

        self.auto_scaling_group = asg_construct(
            self, "Auto_Scaling_Group",
            vpc_webserver=self.vpc_webserver,
            security_group=self.SG_webserver.SG_webserver,
            role=iam.Role(
                self, "Web template Role for S3",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                description="Webserver role"
            ),    
        )

        self.alb = lb_construct(
            self, "Web server ALB",
            vpc=self.vpc_webserver,
            asg=self.auto_scaling_group.auto_scaling_group,
        )

        self.auto_scaling_group.auto_scaling_group.scale_on_request_count(
            "request count auto scaling",
            target_requests_per_minute=250,
        )

        ###############################
        ###create webserver instance###
        ###############################

        
        ######################################################
        ###Creating adminserver instance and calling the SG###
        ######################################################

        self.manegementvpc_sg = managementvpc_sg_construct(
            self, "managementvpc_sg",
            vpc=self.vpc_managementserver,
        )

        # install user data open SSH on admin server


        ########################
        ###call on S3 bucket####
        ########################


        #############################
        ###User data for webserver###
        #############################

        ###########################
        ###User data for ASGroup###
        ###########################

        #########################
        ##########Back up#######
        #########################

       
        ##################################
        ###Show ALB DNS after deploying###
        ##################################

        # CfnOutput(self, "DNS for lb", value=self.alb.alb.load_balancer_dns_name)