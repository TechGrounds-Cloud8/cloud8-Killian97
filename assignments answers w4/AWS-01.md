# Global infrastructure
Get to understand some of the terms like Regions, zones and locations.


## Key terminology
- ***AWS Regions:*** In AWS a region is a physical location around the world with clusters of data centers. Each cluster of data centers is called a AZ, more about AZ's later. In every region multiple pf these az's are isolated and physically seperated. This is one big difference already with other cloud providers since most other providers often only have 1 data center in a region. AWS focuses highly on quality so AWS infrastructure Regions meet the highest levels of security, compliance, and data protection. AWS opens up new regions rapidly to ensure their customers are provided with global quality service.
- ***AZ(Availabilty Zone):*** Like explained before, an AZ is a cluster of data centers inside a region. The AZ's offers benefits and advantages to their customers for example: in every region every single AZ has indepentent power, cooling, physical security and are connected via redundant, ultra-low-latency networks. This makes it able that customers who want high availability can design their application to run in multiple AZ's to achieve even greater fault-tolerance. This makes it also way more scalable then for example a region with only one data center. All traffic between AZ's is encrypted. The network performance is enough to accomplish synchronous replication between AZ's. AZ's make partitioning applications for high availability very easy. If an application is partitioned across AZ's, companies are better isolated and protected from issues such as power outages, natural disasters and more. AZs are physically separated by a meaningful distance, kilometers away from any other AZ, although all are within 100 km of each other.
- ***Local Zone:*** AWS local zones are select AWS services close to the end user. Because it is close customers can easily run highly-demanding applications that require single-digit millisecond latencies to your end-users such as media & entertainment content creation, real-time gaming, reservoir simulations, electronic design automation, and machine learning. A local zone is an extension of a region, customers can run their latency sensitive application using AWS services like Amazon Elastic Compute Cloud and Amazon Virtual Private Cloud. The local zones also provide a high-bandwidth, secure connection between local workloads and those running in the AWS Region, allowing you to seamlessly connect to the full range of in-region services through the same APIs and tool sets. 
- ***Amazon Elastic Compute Cloud:*** 
-***Amazon Virtual Private Cloud:*** 












 













## Exercise
### Sources
1. [AWS](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)



### Overcome challenges


### Results
