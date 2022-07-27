# Design for V1.0

## Assumptions
I have assumed that:
- The region this project has to be in is Europe Central.
- That the VPC's has to be in the same region because it wasn't specified and i think its better that way.
- Cost optimisation is priority #1 during this project, so i should always use the cheapest available but working services.
- That 1 subnet in each VPC is enough but the product owners already told me they really want 2 in each.
- I can use apache2 to run the webserver on.


## VPC's
- There are 2 VPC's.
    - Webserver VPC with CIDR 10.10.10.0/24.
    - Adminserver VPC with CIDR 10.20.20.0/24.
- Each VPC has 2 subnets. 1 in use and 1 extra.
    - Inside each VPC the subnets are in different AZ's.
- The VPC's have a peering connection so they can communicate without using the internet.
- In both VPC's there are security groups(SG's) and Network Access Control Lists(NACL's) for protection and security.


## EC2 instances
- There are 2 ec2 instances 1 in the Web VPC and 1 in the Admin VPC.
- The webserver instance is accesible:
    - Through port 80 and 443.
    - By the admin server with a SSH connection, only by the admin IP.
- The adminserver instance is accesible:
    - By the admin with RDP (port 3389) and SSH (port 22).
- The adminserver has port 80 and port 443 open so it can download OPENSSH.
- Both EC2 instances have an encrypted Root volume.
- The webserver is Linux instance.
- The adminserver is windows instance.
- The webserver instance has user data that installs apache2.
- The adminserver instance has custom data to install and enable OPENSSH.


## Storage
- There is a encrypted S3 bucket to store post deployment scripts in. The bucket contains: 
- The user data for the webserver.
- The webpage files for the webserver.


## Backup
- AWS Backup makes a daily backup that gets stored in a vault for 7 days.



## Suggestions
I only have 1 suggestion and that is still to only use 1 subnet in each VPC's. This makes it cheaper and faster. And if you want more you can always add more later.