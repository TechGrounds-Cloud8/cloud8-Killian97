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


## Challenges
None.

## Solutions
None.