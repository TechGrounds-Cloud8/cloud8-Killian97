#!/bin/bash

# new user data
sudo yum update -y
sudo yum install -y httpd.x86_64
sudo systemctl start httpd.service
sudo systemctl enable httpd.service

# killian user data
# yum update -y
# yum install -y httpd.x86_64
# systemctl start httpd.service
# systemctl enable httpd.service

# quincy user data
# sudo yum -y install httpd
# sudo systemctl enable httpd
# sudo systemctl start httpd