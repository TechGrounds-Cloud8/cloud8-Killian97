# IAM
Study IAM and apply your knowledge.


## Key terminology
- ***IAM(Identity Acces Management):*** Web service helps you secure your AWS resources. With IAM you can control authentication(who is signed in) and authorisation(what permissions does this user have).
- ***A principal:*** Is a person or application that can make a request for an action or operation on an AWS resource. The principal is authenticated as the AWS account root user or an IAM entity to make requests to AWS.
- ***IAM Resources:*** The user, group, role, policy, and identity provider objects that are stored in IAM. As with other AWS services, you can add, edit, and remove resources from IAM.
- ***IAM Identities:*** are the IAM resource objects that are used to identify and group. You can attach a policy to an IAM identity. These include users, groups, and roles.
- ***IAM Entities:*** are the IAM resource objects that AWS uses for authentication. These include IAM users and roles.
- ***Policy:*** A policy is an object in AWS that, when associated with an entity or resource, defines their permissions. AWS evaluates these policies when a principal, such as a user, makes a request. Permissions in the policies determine whether the request is allowed or denied. 
- ***AWS Organizations:*** Is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.
- ***SCP(Service Control Policie):*** Is a type of organization policy that you can use to manage permissions in your organization. SCP's offer central control over the maximum available permissions for all accounts in your organization.
- ***ABAC(Attribute-based access control):***  is an authorization strategy that defines permissions based on attributes. In AWS, these attributes are called tags. You can attach tags to IAM resources, including IAM entities (users or roles) and to AWS resources. 
- ***RBAC(role-based access control):*** Is the traditional authorization model. RBAC defines permissions based on a person's job function, known outside of AWS as a role. Within AWS a role usually refers to an IAM role, which is an identity in IAM that you can assume.

## What features does IAM offer?

***Shared access to your AWS account:***
You can grant other people permission to administer and use resources in your AWS account without having to share your password or access key.

***Granular permissions:***
You can grant different permissions to different people for different resources. For example, you might allow some users complete access to Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), Amazon DynamoDB, Amazon Redshift, and other AWS services. For other users, you can allow read-only access to just some S3 buckets, or permission to administer just some EC2 instances, or to access your billing information but nothing else.

***Secure access to AWS resources for applications that run on Amazon EC2:***
You can use IAM features to securely provide credentials for applications that run on EC2 instances. These credentials provide permissions for your application to access other AWS resources. Examples include S3 buckets and DynamoDB tables.

***Multi-factor authentication (MFA):***
You can add two-factor authentication to your account and to individual users for extra security. With MFA you or your users must provide not only a password or access key to work with your account, but also a code from a specially configured device.

***Identity federation:***
You can allow users who already have passwords elsewhere for example, in your corporate network or with an internet identity provider to get temporary access to your AWS account.

***Identity information for assurance:***
If you use AWS CloudTrail, you receive log records that include information about those who made requests for resources in your account. That information is based on IAM identities.

***PCI DSS Compliance:***
IAM supports the processing, storage, and transmission of credit card data by a merchant or service provider, and has been validated as being compliant with Payment Card Industry(PCI) Data Security Standard(DSS). 

***Integrated with many AWS services:***
IAM can work with basicly every single Service that AWS offers.

***Eventually Consistent:***
IAM, like many other AWS services, is eventually consistent. IAM achieves high availability by replicating data across multiple servers within Amazon's data centers around the world. If a request to change some data is successful, the change is committed and safely stored. However, the change must be replicated across IAM, which can take some time. Such changes include creating or updating users, groups, roles, or policies. We recommend that you do not include such IAM changes in the critical, high-availability code paths of your application. Instead, make IAM changes in a separate initialization or setup routine that you run less frequently. Also, be sure to verify that the changes have been propagated before production workflows depend on them. 

***Free to use:***
AWS Identity and Access Management (IAM) and AWS Security Token Service (AWS STS) are features of your AWS account offered at no additional charge. You are charged only when you access other AWS services using your IAM users or AWS STS temporary security credentials.

## Exercise
### Sources
1. [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
2. 


### Overcome challenges



### Practical Results







