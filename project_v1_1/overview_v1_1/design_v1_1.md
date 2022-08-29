# Design for V1.1

## Assumptions
I have assumed that:
- The region this project has to be in is Europe Central.
- That the VPC's has to be in the same region because it wasn't specified and i think its better that way.
- Cost optimisation is priority #1 during this project, so i should always use the cheapest available but working services.
- That 1 subnet in each VPC is enough but the product owners already told me they really want 2 in each.
- I can use apache2 to run the webserver on.


## VPC's
- There are 2 VPC's.
    - Webserver VPC with CIDR 10.10.0.0/16.
    - Adminserver VPC with CIDR 10.20.0.0/16.
- Each VPC has 2 subnets. 1 private and 1 public.
    - Inside each VPC the subnets are in different AZ's.
- The VPC's have a peering connection so they can communicate without using the internet.
- In both VPC's there are security groups(SG's) and Network Access Control Lists(NACL's) for protection and security.


## EC2 instances
- There are 3 ec2 instances in the Web VPC and 1 in the Admin VPC.
- The private webserver instance is accessible:
    - only for private testing use
- The public webserver is accessible:
    - trough the loadbalancer DNS and will be split between 3 instances if needed
- The adminserver instance is accessible:
    - By the admin with RDP (port 3389) and SSH (port 22).
- The auto scaling instance runs on a launch template.
- The adminserver has port 80 and port 443 open so it can download OPENSSH.
- Both EC2 instances have an encrypted Root volume.
- The webserver is Linux instance.
- The adminserver is windows instance.
- The webserver and autoscale instances have user data that installs httpd.
- The adminserver instance has custom data to install and enable OPENSSH.
- The auto scaling instance gets a health check on daily basis, restarting the instance if the HC fails fails.


## Storage
- There is a encrypted S3 bucket to store post deployment scripts in. The bucket contains: 
    - The user data for the webserver.
    - The webpage files for the webserver.
- All instances have a EBS block storage volume of minimum 8 GB


## Backup
- AWS Backup makes a daily backup that gets stored in a vault for 7 days.

## Suggestions
It might be easier for the autoscaling group to work with a custom AMI instead of a launch template. I could spend some time to learn this and apply it later on.