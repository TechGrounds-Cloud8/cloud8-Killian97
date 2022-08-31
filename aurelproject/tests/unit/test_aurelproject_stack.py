import aws_cdk as core
import aws_cdk.assertions as assertions

from aurelproject.aurelproject_stack import AurelprojectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aurelproject/aurelproject_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AurelprojectStack(app, "aurelproject")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
