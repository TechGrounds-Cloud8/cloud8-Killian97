To SSH to the admin server and from there forward to the webserver follow these steps:
    - Open a terminal and active ssh agent with the command: ssh-agent bash
    - Add the keypair to use for the servers with the command: ssh-add webmin_key_pair.pem
    - Connect to the admin server and allow for forwarding with the command: ssh -A ec2-user@"public IPv4 adress"
    - When in the admin server connect to the webserver with the command: ssh ec2-user@"private IPv4 adress"

To server jump from the microsoft admin server to the linux webserver use the commands below
    - as a first step go to the AWS console and click the admin server, Click on connect and follow the instructions to generate a password, via the SSH client button.
    - Open a terminal and active ssh agent with the command: ssh-agent bash
    - Add the keypair to use for the servers with the command: ssh-add webmin_key_pair.pem
    - ssh -A -J Administrator@<admin.server.public.ip> ec2-user@<web.server.private.ip>