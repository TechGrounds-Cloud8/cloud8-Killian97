# Files app services, CDN, DNS & Database
Study and try to apply: EB, Cloudfront, Route53, EFS and RDS/aurora.

I will change my way of creating my answers from now on. Instead of having a key term part and a result part i will create a Theory block where i talk and explain theory parts and then i will also have a practical part. In the theory part i will answer the same questions for every subject and have a general piece of information. So basicly im changing the names but i want to restructure my answering a bit because the exercizes are also changing.

### Sources
1. Aurel my classmate.
2. [EB](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
3. [ALTS](https://stackshare.io/aws-elastic-beanstalk/alternatives)
4. [VS](https://www.justaftermidnight247.com/insights/cloudformation-vs-elastic-beanstalk-aws-paas-and-iac-services/#:~:text=Beanstalk%20is%20PaaS%20(platform%20as,has%20a%20lot%20to%20offer.)
5. [CloudfrontandS3](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/)
6. [ALTS2](https://www.g2.com/products/amazon-cloudfront/competitors/alternatives)
7. 

### Overcome challenges
This was the first assignment in a new way of "learning" and doing the assignments so i was a bit nervous on how do it. But after talking with aurel we mostly agreed on how to tackle the new form of assigments.

## Theoretical part.

I will answer these 4 quesions for every subject:
  
  1. What is "subject" for?
  2. What does "subject" replace compared to how it was done before?
  3. Can i and how to combine "subject" with other services?
  4. What is the difference between "subject" and other similar services. 

### ***Elastic Beanstalk(EB).***

1. Elastic beanstalk makes you able to launch, deploy and manage your applications in the AWS cloud without the needs to learn how the infrasctructure works and HOW the managing works. But it does not limit you to certain management decisions, you still have full control. For example you can deploy your newly made app and EB will handle the details of capacity provisioning, load balancing, scaling, and application health monitoring. This way you can focus a 100% on managing your app and your customers. EB makes managing your applications less complex. 
2. There was no service like EB before. Before hand if you wanted to deploy your app you needed to learn how to manage it. How to build the infrastructure and how to manage and gather enough resources. Many times this would end up in under or over provisioning or not having enough focus on the app itself because manegement needs time, and most important it would cost alot of money. If you want to read about the history of EB itself i recommend you to go here: [EB history](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platform-history.html)

3. EB is connected to alot of other AWS services because it needs/uses them. When you launch a new application, EB will launch an environment and gather/provide the resources it needs, for example you tell EB you want to launch a web application, EB will then provide an EC2 instance for you. This way EB automatically combines and uses alot of different AWS resources, as a customer you dont need to worry about this because it happens automatically.
4. There are quiet some alternatives for EB, most not in AWS itself but some are. I will list the top 8 alternatives and explain 1 of the alternatives in AWS itself. 

   - Google app engine.
   - Docker.
   - Azure App Serive.
   - Kubernetes.
   - Heroku.
   - Apollo.
   - AWS CodeDeploy.
   - AWS CloudFormation. (i will compare this one with EB)

**Elastic Beanstalk VS CloudFormation:**
Both services essentially have the same goal, deploying your applications. But they approach this very differently. EB is PaaS(platform as a service) and CF is IaC(infrastructure as code). The most important difference is that EB handles deployment and provisioning, so it makes it easier and more comfortable for you While CloudFormation needs alot of imput, So giving you alot of control. 
![EBvsCF](../../../00_includes/AWS-13/ebvscf.png)

So what is EB good for?
Beanstalk can be great for teams who dont have time and resources to invest in the cloud itself. EB is simply said the easier way
CF will be good for? Teams who have the knowlegde about the cloud or when they really need full control. CF is simply said the harder way.
  
### ***Cloudfront.***

1. Cloudfront is a service that peeds up distribution of your static and dynamic web content, For example html and css files. Cloudfront does this by using edge locations. When a user requests your HTML page and you serve it with cloudfront, that request will be routed to the nearest edge location, this way the user will have te shortest delivery time and the best performance. By using edge locations Cloudfront can be used globally and requests can be delivered globally in seconds. Cloudfront is a CDN(Content Delivery Network.)
2. Before Cloudfront, Content needed to be stored locally. For example If you wanted your content that is stored in a S3 bucket to be delivered with the lowest latency as possible, it would mean that you needed to create a physical data center close to the user and store your content there aswell. Cloudfront is used to speed this all up. So before cloudfront you just needed to wait a little longer when surfing the WEB.
3. Yes you can combine Cloudfront with other services. Cloudfront uses the backbone of the AWS network itself. One of the best combinations by AWS ever is Cloudfront + S3 buckets. This is because when you store your static web content in a S3 bucket you no longer need to worry about scaling, S3 does this for you. S3 is serverles, So no more worries about patching and updating. S3 gives you the option to use OAI(Origin Access Identity), so you can secure your content by creating acces restrictions. So when you combine S3 with the Cloudfront delivery you can have cheap, efficient, automatic and secure content delivery to your web users. AWS calls this: A match made in heaven.
4. AWS cloudfront has quiet some competitors, I will list some below and explain the differences from 1 of them.

    - Cloudflare CDN (I will compare this one to Cloudfront)
    - Fastly
    - Azure CDN
    - Varnish Software
    - Imperva App Protect
    - KeyCDN
    - Sucuri
    - Akamai

**Cloudfront VS CloudFlare:**
The key differences in these services is that cloudfront is purely focused on speeding up content delivery while cloudflare also offers DDos protection and a WAF. Another big and important difference is that Cloudflare works like a DNS for your website while cloudfront works directly with your network so it can deliver content instantly.

### ***Route 53.***

1. Route 53 is a highly scalable DNS web service, it has 3 main functions that you can use in any combination you want. These 3 are Domain registration, DNS routing and health checking. When you decide to use all three functions you do need to apply them in a certain order.
    
   1. Register Domain name.
   2. Route internet traffic to the resources for your domain.
   3. Check the health of your resources.




## Practical part.



### Results

