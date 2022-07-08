import aws_cdk as core
import aws_cdk.assertions as assertions

from projectv1_0.projectv1_0_stack import Projectv10Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in projectv1_0/projectv1_0_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Projectv10Stack(app, "projectv1-0")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
