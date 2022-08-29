### all demands for project v1.0

## Network/VPC
- the following IP ranges need to be used: 10.10.10.0/24 & 10.20.20.0/24
    VPC 1 = 10.10.10.0/24 Subnet 1 = 10.10.10.0/25 Subnet 2 = 10.10.10.0/25
    VPC 2 = 10.20.20.0/24 Subnet 1 = 10.20.20.0/25 Subnet 2 = 10.20.20.0/25

- all subnets need to be public

- Both VPC's need to be able to connect trough VPC peering

- the subnets need to be protected by a NACL.

- the instances also need to be protected by Security Groups.

- SSH connections with the webserver is only allowed when it comes from the management server, this can be done with security groups inbound rules by allowing the IP from the management server.

- the management server should only be accesable by me (my ip).

- the webserver needs to be accesable by everyone from all IP with HTTP and HTTPS


## Instances/EC2
- EC2 needs to install a webserver automatically trough user data.

- The instances need to be encrypted


## Backup/AWS backup
- - the webservers need to backed up daily and stored for 7 days

