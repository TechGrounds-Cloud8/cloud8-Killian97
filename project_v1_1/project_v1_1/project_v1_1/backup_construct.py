from aws_cdk import (
    Duration,
    RemovalPolicy,
    aws_backup as backup,
    aws_events as events,
)

from constructs import Construct


class backup_construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #########################
        ##########Back up#######
        #########################

        # create the back up vault
        self.back_up_vault = backup.BackupVault(
            self, "backup_vault",
            backup_vault_name="backup_vault",
            removal_policy=RemovalPolicy.DESTROY,
        )
        
        # create a back up plan
        self.back_up_plan = backup.BackupPlan(
            self, "backup_plan",
            backup_vault=self.back_up_vault,  
        )

        # add rules to the back up plan
        self.back_up_plan.add_rule(backup.BackupPlanRule(
            delete_after=Duration.days(7),
            enable_continuous_backup=True,
            schedule_expression=events.Schedule.cron(
                hour="17",
                minute="1",
            ))
        )