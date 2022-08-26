from aws_cdk import (
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
)

from constructs import Construct


class asg_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc_webserver, security_group, role, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.userdata_webserver = ec2.UserData.for_linux()

        self.launch_template = ec2.LaunchTemplate(
            self, "Launch template",
            launch_template_name="web_server_template",
            instance_type=ec2.InstanceType("t3.nano"),
            key_name="webmin_key_pair",
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            role=role,
            user_data=self.userdata_webserver,
            security_group=security_group,    
        )

        self.auto_scaling_group = autoscaling.AutoScalingGroup(
            self, "Autoscalinggroup",
            vpc = vpc_webserver,
            vpc_subnets = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PUBLIC
            ),
            min_capacity = 1,
            max_capacity = 3,
            launch_template=self.launch_template,
        )

        # define caling policy
        self.auto_scaling_group.scale_on_cpu_utilization(
            'CPU',
            target_utilization_percent = 75,
        )





