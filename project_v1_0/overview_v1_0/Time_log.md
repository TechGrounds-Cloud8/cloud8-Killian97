# Log [05-07-2022]

## Day report
Today i did the first half of the CDK Workshop, i am not sure what i think of it as i feel like ilearn more from reading about it then actually doing the workshop.

## Challenges
None really, basicly all just typing over what it says.

## Solutions
None.

# Log [06-07-2022]

## Day report
Today i did the second half of the CDK workshop.

## Challenges
None.

## Solutions
None.

# Log [07-07-2022]

## Day report
Today i prepared my entire jira and made user stories&tasks. I also wanted to start on the project by creating the first VPC

## Challenges
Alot of stress because my entire CDK didnt work out of nowhere.

## Solutions
It turned out that in my stress i deleted every active resource in my AWS console, including the CDK s3 bucket. Even tho bootstrapping again it did not automatically create a new S3 bucket but it kept trying to find the deleted one. SO i had to destroy the CDK toolkit stack and re install CDK so it created a new stack and a new S3 bucket.

# Log [08-07-2022]

## Day report
Today i continued launching my VPC and did so succesfully. I also succesfully configurated and launched the EC2 instance needed in my webserver VPC.
I configured and succesfully tested my userdata for a test webserver by using HTTPD, but i found out i was storing my user data in the wrong way so i will have to redo this later when i have the S3 bucket ready for post launch scripts.

## Challenges
I struggled alot with how to configure what AMI i needed

## Solutions
After searching quite a while i found out i could use a ALI aswell, i was to fixated on AMI that i ignored ALI, when i tried a ALI it worked.

# Log [11-07-2022]

## Day report
Today i succesfully created and configured the security groups needed for both VPC's BUT i only did the HTTP and HTTPS rules, i still have fix the SSH rules for the admin server

## Challenges
How to fill in the parameters.

## Solutions
Read more carefully.

# Log [12-07-2022] 

## Day report
today i started with configuring user data and the NACL's.

## Challenges
i succesfully created the NACL's but i could no longer reach my webserver, i did not get to the userdata part

## Solutions
none, continue tommorow

# Log [13-07-2022]

## Day report
i succesfully created a S3 bucket to store user data in, read it and execute it. 

## Challenges
same as yesterday. and my S3 bucket is public, this cant stay like this but i will fix this in the end.

## Solutions
EPHEMERAL PORTS!!!

# Log [14-07-2022]

## Day report
today was a very bad day, i did nothing.

## Challenges
my home situation was very toxic and took all my focus.

## Solutions
i slept during the afternoon and got a good mood again.

# Log [15-07-2022]

## Day report
i started trying to fix the VPC peering because i could not ssh from the admin to the webserver.

## Challenges
i knew it had something todo with routing and route tables but i was having a hard time finding what i needed

## Solutions
Cfn routing with tokens.

# Log [18-07-2022]

## Day report
today in this heat i wanted to atleast fix the vpc peering, this was done succesfully together with aurel. and i will start with the backup feature. also fixed the S3 bucket no longer being public.

## Challenges
the heat, but we managed.

## Solutions
we had to untoken the token.

# Log [19-07-2022]

## Day report
today i am going to try to create my backup plan.

## Challenges
HEAT. and not really being able to test if it works without wasting money.

## Solutions
stop half way the day and continue in the cooler evening

# Log [20-07-2022]

## Day report
Today i planned on finishing the AWS backup. i did succesfully except not being able to delete the stack after the RP was made. i will try to fix this later on.

## Challenges
The warmt was still there and i slept very badly

## Solutions
stop half way the day and continue in the cooler evening

# Log [21-07-2022]

## Day report
Today i wanted to figure out how to encrypt the 2 servers itself. i did this succesfully

## Challenges
No idea what exactly to backup and where.

## Solutions
We had to attack RDS volumes to our server and encrypt those. So the server would be on those volumes and be encrypted.

# Log [22-07-2022]

## Day report
Today together with Aurel we fixed that our webserver shows our new index.html website instead of the default apache page that comes with installing apache.

## Challenges
Not being able to overwrite the apache page.

## Solutions


# Log [25-07-2022]

## Day report
Tried changing the webserver from a Linux server to a windows server and connecting to it trough RPD & SSH, did this succesfully.
Secondly i tried to SSH from my Admin server to my webserver like before but now from windows to Linnux, Did this succesfully.

## Challenges
Struggling with connecting to my windows server because it was so slow. and having no idea how todo the connect since it was not know by me how to

## Solutions
Use proxy jump to connect from my PC to the admin server and jump to the webserver with all SSH. and just use RDP for single connection from my PC to admin.

# Log [26-07-2022]

## Day report
I tried to fix the Recovry point error when deleting the vault when the RP was already created. 

## Challenges
I could not delete the stack when the RP was created. because the Vault cant be deleted with a resource inside. except manually.

## Solutions
After multiple tries during the day we asked our teachers and they said its possible but that its not smart todo it cause of safety reasons so i am going to let this be. A company later on that will use my code wont delete their stack so its not necesary and they could always do it manually in 10 seconds.

# Log [27-07-2022]

## Day report
Today i will finish up and finalize the documentation for V1.0. i did this succesfully.

## Challenges
None

## Solutions
None

# Log [28-07-2022]

## Day report


## Challenges


## Solutions

# Log [29-07-2022]

## Day report


## Challenges


## Solutions