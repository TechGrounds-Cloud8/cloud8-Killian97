# Security groups
Study about AWS security.


## Key terminology
- ***Security group:*** A Security group act as a statefull virtual firewall, controlling the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance. It is important to know that the rules are always allow rules. Something that isnt allowed is automatically denied. An instance can have multiple security groups but also a security group can be assigned to multiple instances. When you create a rule for a security group it will be applied to all connected instances automatically. An intresting thing to know is that when you create a security group it will have 0 inbound rules, so nothing will be allowed. But that newly created security group will have 1 outbound rule that allows everything. So all outbound traffic is allowed.
- ***NACL(Network Acces Control List):*** A ACL is an optional layer of security for your VPC that acts as a stateless firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC. When you create a VPC it automatically comes with a modifiable default network ACL. By default, it allows all inbound and outbound IPv4 traffic and, if applicable, IPv6 traffic. Differently then the security groups you can associate a network ACL with multiple subnets. But, a subnet can be associated with only one network ACL.





## Exercise
### Sources
1. [SC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
2. [SC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
3. [DIFF](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html#VPC_Security_Comparison)
4. [ACL](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)



### Overcome challenges
None besides needing to google everything.

### Results