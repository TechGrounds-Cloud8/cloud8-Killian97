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

        self.vault = backup.BackupVault(
            self, "Webserver_Backup_Vault",
            backup_vault_name = "Webserver_Backup_Vault",
            removal_policy = RemovalPolicy.DESTROY,
        )

        self.backup_plan = backup.BackupPlan(
            self, "Daily_Backup",
            backup_vault = self.vault,
        )

        self.backup_plan.add_rule(backup.BackupPlanRule(
            delete_after=Duration.days(7),
            enable_continuous_backup=True,
            schedule_expression=events.Schedule.cron(
                hour="17",
                minute="1",
            ))
        )