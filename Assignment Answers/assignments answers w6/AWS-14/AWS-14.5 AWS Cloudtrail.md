# AWS Cloud Trail
Study AWS Cloud Trail


### Sources
1. [Cloudtrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

### Overcome challenges
None really, just alot of reading again.



## Theoretical part.

I think in a simple sentence AWS cloudtrail could be explained. Cloudtrail is the supervisor of your AWS account. A deeper explanation would be that Cloudtrail is a service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs. So when you do something (create activity) in your AWS account or someone else. Cloudtrail will record that. Cloud trail is automatically activated on account creation but if you want an ongoing record of activity and events in your AWS account, you can create a cloud trail yourself. Visibily and safety in your AWS account is a key aspect of security and operational best practices. Cloudtrail gives this oppurtunity because, You can use CloudTrail to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. You can identify who or what took which action, what resources were acted upon, when the event occurred, and other details to help you analyze and respond to activity in your AWS account.
There are 2 types of trails for a AWs account.
1. ***A trail that applies to all regions:*** When you create a trail that applies to all regions, CloudTrail records events in each region and delivers the CloudTrail event log files to an S3 bucket that you specify. If a region is added after you create a trail that applies to all regions, that new region is automatically included, and events in that region are logged. Because creating a trail in all regions is a recommended best practice, so you capture activity in all regions in your account, an all-regions trail is the default option when you create a trail in the CloudTrail console.
2. ***A trail that applies to one region:*** When you create a trail that applies to one region, CloudTrail records the events in that region only. It then delivers the CloudTrail event log files to an Amazon S3 bucket that you specify. You can only create a single-region trail by using the AWS CLI. If you create additional single trails, you can have those trails deliver CloudTrail event log files to the same Amazon S3 bucket or to separate buckets. This is the default option when you create a trail using the AWS CLI or the CloudTrail API.



### Practical Results
This exercize was a full theory assignment.














