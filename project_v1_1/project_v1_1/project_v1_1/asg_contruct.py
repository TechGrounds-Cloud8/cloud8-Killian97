from aws_cdk import (
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
)

from constructs import Construct


class asg_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc_webserver, security_group, role, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
  
        self.user_data = ec2.UserData.for_linux()

        # create and configure launch Template
        self.launch_temp = ec2.LaunchTemplate(
            self, "Launch template",
            launch_template_name="web_server_template",
            instance_type=ec2.InstanceType("t3.nano"),
            key_name="webmin_key_pair",
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            role=role,
            user_data=self.user_data,
            security_group=security_group,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=True,    
                    )
                )
            ]    
        )

        # create and configure the auto scaling group
        self.as_group = autoscaling.AutoScalingGroup(
            self, "Auto_Scaling_Group",
            vpc=vpc_webserver,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT
            ),
            launch_template=self.launch_temp,
            min_capacity=1,
            max_capacity=3,
        )

        # scaling policy
        self.as_group.scale_on_cpu_utilization(
            "cpu auto scaling",
            target_utilization_percent=80,
        )