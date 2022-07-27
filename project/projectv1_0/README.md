# README TG project V1.0

In this readme you will get to know what todo to get this project running for yourself.
This project is created with AWS CDK, if you have no experience with CDK, dont worry in the requirments steps you will learn the basics.


# Requirments for the project
- [A github account](https://github.com/)
- [Python installed (during installation add python to your PATH)](https://www.python.org/downloads/)
- [An AWS account and user](https://aws.amazon.com/)
- [NodeJS installed](https://nodejs.org/en/)
- [An IDE (VScode recommended)](https://code.visualstudio.com/)
- AWS cdk installed, follow the steps below:
    1. Open a terminal session and run the following command: 
    ```
    npm install -g aws-cdk
    ```

    2. Check if the installation was succesfull with the command: 
    ```
    cdk --version
    ```
- [Setup your CDK (if you dont know how follow the NEW PROJECT part of this workshop)](https://cdkworkshop.com/30-python/20-create-project.html)


# Editting the Files for your use
1. In the AWS console create a keypair and name it webmin_key_pair like in the picture below. (Remember where you store the key pair.)
![Keypair creation](../overview/Images/create_keypair.png)
2. In the top of the stack.py file edit the my_ip variable, this will allow on your PC to connect to the admin server.
3. Re deploy the project with: CDK deploy

# Connect via SSH

1. Open a bash terminal in the DIR where your key pair is stored.
2. Start the ssh agent with the command: '''