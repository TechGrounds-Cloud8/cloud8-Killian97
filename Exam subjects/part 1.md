## In these guides i will explain the subjects i came across in prep exam 1 and could not answer.



## keyterms
- ***AWS quick start:*** AWS Quick Starts are essentially reference architectures plus automation. that help customers deploy AWS-native services and products from AWS Partners.

- ***Loose coupling:*** a workload containing a lot of smaller jobs. this enabled parralel processing

- ***Monolithic apps:*** this is one workload working as 1 big process. this makes it that when 1 part has a spike or error the entire process suffers from it

- ***AWS Artifact:*** AWS Artifact is your go-to, central resource for compliance related information that matters to you. It provides on-demand access to AWS’ security and compliance reports and select online agreements

- ***AWS inspector:*** is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Amazon Inspector automatically assesses applications for exposure, vulnerabilities, and deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed list of security findings prioritized by level of severity.

- ***Scaling policy:*** 
    - ***target tracking policy:*** you select a scaling metric and set a target value. Amazon EC2 Auto Scaling creates and manages the CloudWatch alarms that trigger the scaling policy and calculates the scaling adjustment based on the metric and the target value.
    - ***Step scaling policy:*** When step adjustments are applied, and they increase or decrease the current capacity of your Auto Scaling group, the adjustments vary based on the size of the alarm breach. With step scaling the policy can continue to respond to additional alarms, even while a scaling activity or health check replacement is in progress. 
    - ***Simple scaling policy:*** The main issue with simple scaling is that after a scaling activity is started, the policy must wait for the scaling activity or health check replacement to complete and the cooldown period to end before responding to additional alarms. Cooldown periods help to prevent the initiation of additional scaling activities before the effects of previous activities are visible.

- ***Bare metal instances:*** you need nitro for this and this basicly is a very very good version of computing. Bare metal instances allow EC2 customers to run applications that benefit from deep performance analysis tools, specialized workloads that require direct access to bare metal infrastructure, legacy workloads not supported in virtual environments, and licensing-restricted business critical applications.

- ***IOPS:*** IOPS are a unit of measure representing input/output operations per second. measured in KiB. Works with EBS.

- ***Dedicated hosts:*** is a physical server with EC2 instance capacity fully dedicated to your use.

- ***Dedicated instances:*** Dedicated Instances are Amazon EC2 instances that run in a virtual private cloud (VPC) on hardware that's dedicated to a single customer. Dedicated Instances that belong to different AWS accounts are physically isolated at a hardware level, even if those accounts are linked to a single payer account.

- ***Reservered instances:***

    - ***Standard:*** These provide the most significant discount, but can only be modified. Standard Reserved Instances cannot be exchanged.
    - ***Convertible:*** These provide a lower discount than Standard Reserved Instances, but can be exchanged for another Convertible Reserved Instance with different instance attributes. Convertible Reserved Instances can also be modified.

- ***Elasticache:***  is a web service that makes it easy to set up, manage, and scale a distributed in-memory data store or cache environment in the cloud. It provides a high-performance, scalable, and cost-effective caching solution. At the same time, it helps remove the complexity associated with deploying and managing a distributed cache environment.

- ***Data pipeline:*** is a web service that you can use to automate the movement and transformation of data.

- ***Code pipeline:*** is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software.

- ***On premise:***  physical hosted software and hardware

- ***Elasticity:*** Elasticity is the ability to grow or shrink infrastructure resources dynamically as needed to adapt to workload changes in an autonomic manner, maximizing the use of resources. DIFFERENT THAN SCALABILITY.

- ***Redshift:***  is a fully managed, petabyte-scale data warehouse service in the cloud. You can start with just a few hundred gigabytes of data and scale to a petabyte or more. This enables you to use your data to acquire new insights for your business and customers.

- ***Cost allocation tags:*** organize your resource costs on your cost allocation report, to make it easier for you to categorize and track your AWS costs. 

- ***Consolidated billing:*** enables you to consolidate payment for multiple AWS accounts within your company by designating a single paying account. Consolidated Billing enables you to see a combined view of AWS costs incurred by all accounts in your department or company, as well as obtain a detailed cost report for each individual AWS account associated with your paying account. this also problably enables you to get "use more pay less"

- ***Cost explorer:*** AWS Cost Explorer is a tool that enables you to view and analyze your costs and usage.

- ***AWS macie:*** is a fully managed data security and data privacy service that uses machine learning and pattern matching to help you discover, monitor, and protect sensitive data in your AWS environment.

- ***AWS Guard duty:*** is a continuous security monitoring service that analyzes and processes the following data sources: AWS CloudTrail management event logs, AWS CloudTrail data events for S3, DNS logs, EKS audit logs, and VPC flow logs.

- ***AWS Detective:*** makes it easy to analyze, investigate, and quickly identify the root cause of security findings or suspicious activities. Detective automatically collects log data from your AWS resources.

- ***AWS batch:*** helps you to run batch computing workloads on the AWS Cloud. Batch computing is a common way for developers, scientists, and engineers to access large amounts of compute resources.

- ***Responsibility model:*** 
![SS](/00_includes/Prep%20exam%20examples/respondmodel.png)

- ***Code commit:*** alternative for GITHUB

- ***Code deploy:***  is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.

- ***Cloudtrail:*** is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. 

- ***AWS cost management console:*** The AWS Cost Management console is integrated closely with the Billing console. Using both together, you can manage your costs in a holistic manner. You can use Billing console resources to manage your ongoing payments, and AWS Cost Management console resources to optimize your future costs.

- ***Access keys:***  are long-term credentials for an IAM user or the AWS account root user. You can use access keys to sign programmatic requests to the AWS CLI or AWS API (directly or using the AWS SDK).

- ***Outposts:*** is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises. By providing local access to AWS managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs. AKA aws brings it to the customer.

- ***Amazon Workspace:*** is a cloud-based virtual desktop that can act as a replacement for a traditional desktop.

- ***Direct connect:*** links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an AWS Direct Connect router. With this connection, you can create virtual interfaces directly to public AWS services (for example, to Amazon S3) or to Amazon VPC, bypassing internet service providers in your network path.

- ***All pillars of “well architected framework”:***
