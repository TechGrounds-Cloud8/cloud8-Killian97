### all demands for project v1.0

- All VM discs need to be encrypted

- the webservers need to backed up daily and stored for 7 days
- the webserver needs to be deployed automatically
- the management server can be accesed with a public IP
- the management server can only be accesed from trusted locations
- the following IP ranges need to be used: 10.10.10.0/24 & 10.20.20.0/24
- all subnets need to be protected by a firewall on subnet level
- SSH or RDP connections with the webserver are only allowed when they come from the management server
- there need to be 2 VPC's in 2 different regions, with 2 public subnets each