# Shared Responsibility Model
Study The shared responsibility model of AWS.


## Key terminology
All will be explained under results.




## Exercise
### Sources
1. [Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
 


### Overcome challenges
None actually, remembered from the assesment week. 

### Results

Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden as AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided security group firewall. Customers should carefully consider the services they choose as their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations. The nature of this shared responsibility also provides the flexibility and customer control that permits the deployment. The model simply said is split into 2 parts:

1. Security “of” the Cloud (This part is AWS)
2. Security “in” the Cloud (This part is the customer)

AWS is responsible for the security OF the cloud, meaning that they are responsible for the infrastructure. For example all the hardware, the software, the facilities ofcourse. Everything that is needed to run their services is also their own responsibility.

The customer it self is responsible for the security IN the cloud, This will always differ with what package and what services the customer picks. Some services need more configuration than others. Lets take EC2 and S3 as examples

1. ***EC2:*** When a customer want to launch a EC2 instance they themselves need to do the configuration and management tasks. They need to manage their guest operating system and also take care of updates and litteral security patches and settings. Every app/software a customer installs on that same instance has the same "rules", they need to configure it themselves and mananage it, again including updates and security etc. The customer is also responsible for the Security groups, this is a firewall delivered by AWS itself but the customer needs to configure it themselves. 
2. ***S3:*** In my opinion this one sounds a lot simpler and very logical, S3 is a storage services. So AWS is responsible for the infrastructure of this storage, the operating system, the hardware, the software and everything needed to make those buckets do their work. But the customer itself will be responsible for their own data inside the buckets. This includes things like encrypting and classifying assets. IAM tools are also the customers responsbility here, They need to set permissions etc.

Below here i will Show you a visualisation that will explain it visualy and in a good way.
![SS](../../../00_includes/AWS-09/Shared_Responsibility_Model.png)

There are also shared controls, these are controls which apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services. Examples include:

- ***Patch Management:*** AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
- ***Configuration Management:*** AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest OS, databases, and applications.
- ***Awareness & Training:*** AWS trains AWS employees, but a customer must train their own employees.

Customer specific responsiblities exist aswell. 1 example for this is:
- Service and Communications Protection or Zone Security which may require a customer to route or zone data within specific security environments.