# EBS



## Key terminology
- ***LSBLK command:*** 
- ***file -s command:*** 
- ***mkfs -t ext4 command:*** 
- ***mf -h command:*** 
- ***File system:***





## Exercise
### Sources
1. [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html)
2. Classmate Aurel.
3. [YT](https://www.youtube.com/watch?v=VnO3Lz7Qr0U)




### Overcome challenges


### Results

## Exercise 1
1. Navigate to the EC2 menu.
2. Create a t2.micro Amazon Linux 2 machine with all the default settings.
3. Create a new EBS volume with the following requirements:
    - Volume type: General Purpose SSD (gp3)
    - Size: 1 GiB
    - Availability Zone: same as your EC2
4. Wait for its state to be available.

## Exercise 2
1. Attach your new EBS volume to your EC2 instance.
2. Connect to your EC2 instance using SSH.
3. Mount the EBS volume on your instance.
4. Create a text file and write it to the mounted EBS volume.

## Exercise 3
1. Create a snapshot of your EBS volume.
2. Remove the text file from your original EBS volume.
3. Create a new volume using your snapshot.
4. Detach your original EBS volume.
5. Attach the new volume to your EC2 and mount it.
6. Find your text file on the new EBS volume.
