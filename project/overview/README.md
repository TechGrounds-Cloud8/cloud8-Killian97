To SSH to the admin server and from there forward to the webserver follow these steps:
    - Open a terminal and active ssh agent with the command: ssh-agent bash
    - Add the keypair to use for the servers with the command: $ ssh-add webmin_key_pair.pem
    - Connect to the admin server and allow for forwarding with the command: ssh -A ec2-user@"public IPv4 adress"
    - When in the admin server connect to the webserver with the command: ssh ec2-user@"private IPv4 adress"