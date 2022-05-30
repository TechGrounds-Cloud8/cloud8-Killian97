# VPC
Learn how to create and edit VPC's


## Key terminology
- ***EIP(Elastic IP addresses):*** An Elastic IP address is a static IPv4 address designed for dynamic cloud computing. An Elastic IP address is allocated to your AWS account, and is yours until you release it. By using an Elastic IP address, you can mask the failure of an instance or software by rapidly remapping the address to another instance in your account. Alternatively, you can specify the Elastic IP address in a DNS record for your domain, so that your domain points to your instance. For more information, see the documentation for your domain registrar, or Set up dynamic DNS on Your Amazon Linux instance.
- ***Accelerator:*** Global Accelerator is a global service that supports endpoints in multiple AWS Regions.




## Exercise
### Sources
1. Previous assignments about subnetting, masks and VPC's.
2. [EIP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)


### Overcome challenges
For the start i was a bit scared of not understanding it, because last time i had to work with subnets it took me a long while to understand it all.

### Results

##Exercise 1
1. Allocate an Elastic IP address to your account.
2. Use the Launch VPC Wizard option to create a new VPC with the following requirements:
    - Region: Frankfurt (eu-central-1)
    - VPC with a public and a private subnet
    - Name: Lab VPC
    - CIDR: 10.0.0.0/16
3. Requirements for the public subnet:
    - Name: Public subnet 1
    - CIDR: 10.0.0.0/24
    - AZ: eu-central-1a
4. Requirements for the private subnet:
    - Name: Private subnet 1
    - CIDR: 10.0.1.0/24
    - AZ: eu-central-1a

Below you can see me creating my VPC.
![SS](../../../00_includes/AWS-10/vpcreated2.png)

Below you can see that the creation was completed.
![SS](../../../00_includes/AWS-10/vpcmade.png)

Below you will see 2 screenshots where you can see i explicitly associated my public subnets to the public route table and my private subnets to the private route table.
![SS](../../../00_includes/AWS-10/privateroute1.png)
![SS](../../../00_includes/AWS-10/publicroute1.png)



