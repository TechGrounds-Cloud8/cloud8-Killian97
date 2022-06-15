## In these guides i will explain the subjects i came across in prep exam 2 and could not answer.


## Keyterms

- ***ITSM(IT service management) tools:*** Most enterprise customers use IT service management (ITSM) tools to automate their on-premises operations. They need the same tools when they move to the cloud. The alternative—relearning operations without their ITSM tools—is costly and would delay migration. The following table shows the common integration patterns between ITSM tools and AWS.
![SS](/00_includes/Prep%20exam%20examples/itsm-landing-zone-integration.png)

- ***ITIL process:*** ITIL is a framework for effectively managing IT services throughout the entire service lifecycle. it has 5 stages.
![SS](/00_includes/Prep%20exam%20examples/itil.png)

- ***Managed services:*** AMS implements best practices and maintains your infrastructure to reduce your operational overhead and risk. AMS provides full-lifecycle services to provision, run, and support your infrastructure, and automates common activities such as change requests, monitoring, patch management, security, and backup services. AMS enforces your corporate and security infrastructure policies.

- ***AWS Health dashboard:*** The AWS Health Dashboard is the single place to learn about the availability and operations of ALL AWS services. you dont need to be logged in or even have a account.

- ***AWS datasync:*** AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between storage systems and services.

- ***AWS cloudHSM:*** AWS CloudHSM is a cryptographic service for creating and maintaining hardware security modules (HSMs) in your AWS environment. You can use AWS CloudHSM to offload SSL/TLS processing for web servers, protect private keys linked to an issuing certificate authority (CA), or enable Transparent Data Encryption (TDE) for Oracle databases.

- ***AWS KMS(Key Management Service):*** is a managed service that makes it easy for you to create and control the cryptographic keys that are used to protect your data. AWS KMS uses HSM  to protect your KMS keys

- ***AWS SMS:*** You can use Amazon SNS to send text messages, or SMS messages, to SMS-enabled devices. aka its a SMS

- ***AWS DMS(Database Migration Service):***  is a cloud service that makes it easy to migrate relational databases, data warehouses, NoSQL databases, and other types of data stores. You can use AWS DMS to migrate your data into the AWS Cloud or between combinations of cloud and on-premises setups.

- ***AWS Directory service:*** AWS Directory Service provides multiple ways to use Microsoft Active Directory (AD) with other AWS services.

- ***S3 storage classes:*** 
    - ***S3 Standard:*** The default storage class. If you don't specify the storage class when you upload an object, Amazon S3 assigns the S3 Standard storage class.
    - ***Reduced Redundancy:*** The Reduced Redundancy Storage (RRS) storage class is designed for noncritical, reproducible data that can be stored with less redundancy than the S3 Standard storage class.
    - ***S3 Standard-IA:*** Amazon S3 stores the object data redundantly across multiple geographically separated Availability Zones (similar to the S3 Standard storage class). S3 Standard-IA objects are resilient to the loss of an Availability Zone. This storage class offers greater availability and resiliency than the S3 One Zone-IA class.
    - ***S3 One Zone-IA:*** Amazon S3 stores the object data in only one Availability Zone, which makes it less expensive than S3 Standard-IA. However, the data is not resilient to the physical loss of the Availability Zone resulting from disasters, such as earthquakes and floods. The S3 One Zone-IA storage class is as durable as Standard-IA, but it is less available and less resilient.
    - ***S3 Glacier Instant Retrieval:*** Use for archiving data that is rarely accessed and requires milliseconds retrieval. Data stored in the S3 Glacier Instant Retrieval storage class offers a cost savings compared to the S3 Standard-IA storage class, with the same latency and throughput performance as the S3 Standard-IA storage class. S3 Glacier Instant Retrieval has higher data access costs than S3 Standard-IA. 
    - ***S3 Glacier Flexible Retrieval:*** Use for archives where portions of the data might need to be retrieved in minutes. Data stored in the S3 Glacier Flexible Retrieval storage class has a minimum storage duration period of 90 days and can be accessed in as little as 1-5 minutes using expedited retrieval. The retrieval time is flexible, and you can request free bulk retrievals in up to 5-12 hours. If you have deleted, overwritten, or transitioned to a different storage class an object before the 90-day minimum, you are charged for 90 days. 
    - ***S3 Glacier Deep Archive:*** Use for archiving data that rarely needs to be accessed. Data stored in the S3 Glacier Deep Archive storage class has a minimum storage duration period of 180 days and a default retrieval time of 12 hours. If you have deleted, overwritten, or transitioned to a different storage class an object before the 180-day minimum, you are charged for 180 days. 

- ***AWS shield:*** DDoS protection

- ***Transit gateway:*** is a network transit hub that you can use to interconnect your virtual private clouds (VPCs) and on-premises networks

- ***VPC peering:*** A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them using private IPv4 addresses or IPv6 addresses. Instances in either VPC can communicate with each other as if they are within the same network.

- ***Elastic IP address:*** An Elastic IP address is a static IPv4 address designed for dynamic cloud computing. An Elastic IP address is allocated to your AWS account, and is yours until you release it.

- ***TCO calculator:*** AWS Pricing Calculator allows you to explore AWS services based on your use cases and create a cost estimate. You can model your solutions before building them, explore the price points and calculations behind your estimate, and find the available instance types and contract terms that meet your needs. 

- ***AWS storage gateways:*** AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage.
    - ***Amazon S3 File Gateway:*** Amazon S3 File Gateway presents a file interface that enables you to store files as objects in Amazon S3 using the industry-standard NFS and SMB file protocols, and access those files via NFS and SMB from your data center or Amazon EC2, or access those files as objects directly in Amazon S3
    - ***Amazon FSx File Gateway:*** Amazon FSx File Gateway provides fast, low-latency on-premises access to fully managed, highly reliable, and scalable file shares in the cloud using the industry-standard SMB protocol. Customers can store and access file data in Amazon FSx with Windows-native compatibility including full NTFS support, shadow copies, and Access Control Lists (ACLs).
    - ***Tape Gateway:*** Tape Gateway presents an iSCSI-based virtual tape library (VTL) of virtual tape drives and a virtual media changer to your on-premises backup application. It is compatible with most leading backup applications, so you can continue using your tape-based backup workflows.

- ***AWS ETL(extract, transform, and load) (AWS glue):*** AWS Glue is a fully managed ETL (extract, transform, and load) service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams.

- ***ISO 27001:*** ISO 27001/27002 is a widely-adopted global security standard that sets out requirements and best practices for a systematic approach to managing company and customer information that’s based on periodic risk assessments appropriate to ever-changing threat scenarios. 

- ***HIPAA:*** The Health Insurance Portability and Accountability Act of 1996 (HIPAA) is legislation that is designed to make it easier for US workers to retain health insurance coverage when they change or lose their jobs. The legislation also seeks to encourage electronic health records to improve the efficiency and quality of the US healthcare system through improved information sharing.
 
- ***AWS SOC(System and Organization Controls):*** Reports are independent third-party examination reports that demonstrate how AWS achieves key compliance controls and objectives. The purpose of these reports is to help you and your auditors understand the AWS controls established to support operations and compliance. There are five AWS SOC Reports:
    1. AWS SOC 1 Report, available to AWS customers from AWS Artifact.
    2. AWS SOC 2 Security, Availability & Confidentiality Report, available to AWS customers from AWS Artifact.
    3. AWS SOC 2 Security, Availability & Confidentiality Report available to AWS customers from AWS Artifact (scope includes Amazon DocumentDB only).
    4. AWS SOC 2 Privacy Type I Report, available to AWS customers from AWS Artifact.
    5. AWS SOC 3 Security, Availability & Confidentiality Report, publicly available as a whitepaper. 

- ***AWS puppet:*** Puppet is a declarative, model-based configuration management solution from Puppet Labs that lets you define the state of your IT infrastructure, and automatically enforces that desired state on your systems.

- ***AWS Opsworks:*** is a configuration management service that helps you configure and operate applications in a cloud enterprise by using Puppet or Chef. AWS OpsWorks Stacks and AWS OpsWorks for Chef Automate let you use Chef cookbooks and solutions for configuration management, while OpsWorks for Puppet Enterprise lets you configure a Puppet Enterprise master server in AWS. Puppet offers a set of tools for enforcing the desired state of your infrastructure, and automating on-demand tasks.

- ***AWS Lightsail:*** Amazon Lightsail is a virtual private server (VPS) provider and is the easiest way to get started with AWS for developers, small businesses, students, and other users who need a solution to build and host their applications on cloud.

- ***AWS secrets manager:*** Secrets Manager enables you to replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. This helps ensure the secret can't be compromised by someone examining your code, because the secret no longer exists in the code. 

- ***AWS backup:*** is a fully managed backup service that makes it easy to centralize and automate the backing up of data across AWS services. With AWS Backup, you can create backup policies called backup plans. You can use these plans to define your backup requirements, such as how frequently to back up your data and how long to retain those backups.

- ***AWS connect:*** Amazon Connect is an omnichannel cloud contact center. You can set up a contact center in a few steps, add agents who are located anywhere, and start engaging with your customers.

- ***Elastic beanstalk:*** With Elastic Beanstalk, you can quickly deploy and manage applications in the AWS Cloud without having to learn about the infrastructure that runs those applications. Elastic Beanstalk reduces management complexity without restricting choice or control. You simply upload your application, and Elastic Beanstalk automatically handles the details of capacity provisioning, load balancing, scaling, and application health monitoring.

- ***Virtual private network:*** AWS Virtual Private Network solutions establish secure connections between your on-premises networks, remote offices, client devices, and the AWS global network.