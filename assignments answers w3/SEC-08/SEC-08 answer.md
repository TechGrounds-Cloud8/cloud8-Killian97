# Detection, response and analysis


## Key terminology
- ***Network based IPS and IDS:*** These are security systems that analyze network traffic. 2 examples below. A advantage of networked based systems is that you can protect multiple devices in one go. A disadvantage is that it cannot see something that already is ON the device, so if a attacker is already on your device trying to get in the IPS and IDS wont notice it.
- ***Network based IDS(Intrusion Detection System):*** This gets installed on the network and it makes copies of data and scans them, when it sees a malware or a attack it will send of a alert. AKA is detects the treat but it can't stop it because it scans a copy and its inside the network.
- ***Network based IPS(Intrusion Prevention System):*** This gets installed between for example a router and device, this way any traffic coming from or going towards that device gets scanned and if the IPS finds a treat it will stop it. AKA is prevents it. A dis advantage for this is that IPS can maybe block good data because it thinks its a treat while its not. This will have a negative impact on your network.
- ***Host based IPS and IDS:*** These are versions of IPS and IDS installed ON a device, its a software that runs on a host. This way every single host on a network will have his personal security. This has a big advantage but that comes at a cost. Think about a company with 1000 hosts, will be costly because of the licenses needed and the space the software needs.
  - in the picture below you can see the different locations of IPS and IDS.
  ![SS](../../00_includes/SEC-08/ipsids.png)
- ***Signature match:*** This is one of the ways for IPS and IDS to identify malicious data. This means that for example a vendor has given us a database with over a 1000 dangerous signatures, the IPS/IDS will use that database to compare the signatures from the data transmissions. When it finds a match it will sound the alarm.
- ***Anomaly Detection:*** This is another of the ways for IPS and IDS to identify malicious data. Like the name kinda says this way of detecting is based on a basis. For example a network has 30 TCP sessions running at the same time. This will be the avarage, AKA the normal amount. When out of nowhere there will be 300 TCP sessiions this will be seen as a anomaly because it exceeds the basis. When this happens the IPS/IDS will sound the alarm.
- ***IRP(Incident Response Plan):*** Is the documentation of a predetermined set of instructions or procedures to detect, respond to, and limit consequences of a malicious cyber attacks against an organization’s information systems. In this plan a few things really need to be documented:
  - Prioritize what kind incidents need immediate respons and what can wait.
  - There needs to be structure, roles and responsibilities for each member of a response team.
  - The organisation needs to provide and allow the team to operate on full efficiency.
  - There need to be procedures for responses.
  - It has to be known that some kinds of attacks need to be reported to higher authorities.

  ### The steps of a good IRP:
  1. ***The detection phase***:, this is the most important phase. Very simple because if you cant detect a threat you cant stop it. At this step you decide what kinda of response is necesary.
  2. ***The response phase:*** In this phase you need to learn about what is happening and contain it.
  3. ***The Mitigation phase:*** This is the step where you need to stop the attack or detach the hacker.
  4. ***The reporting phase:*** This is where you need to report to your "management", you need to tell them what happened and what you did to stop it.
  5. ***The recovery phase:*** The name says it already but this step means that you need to recover your system to the pre attack status and is secured again.
  6. ***The Remediation & report phase:*** This is a very important phase in my opinion. This step means you need to protect the data that has been leaked and that you need to report to the people who have been affected by the data leak, or even the higher authorities/goverment.
  7. ***The lessons learned phase:*** This is the "look back" moment. What happened, how did it happen, how did we deal with it, and how are we gonna prevent it from happening again.

- ***RPO(Recovery point objective):***  This this is the maximum acceptable amount of data loss after an unplanned data-loss incident, expressed as an amount of time. This is usually reffered to as the point in time before the data loss event at which data can be successfully recovered.
- ***RTO(Recovery Time Objective):*** This is the maximum acceptable amount of time for restoring a network or application and regaining access to data after an unplanned disruption. Loss of revenue and the extent to which a disrupted process impacts business continuity can both have an impact on RTO.
- ***CERT:*** The Computer Emergency Response Team. This is the team that works with the IRP.
- ***System Hardening:*** Systems hardening is a collection of tools, techniques, and best practices to reduce vulnerability in technology applications, systems, infrastructure, firmware, and other areas. The goal of systems hardening is to reduce security risk by eliminating potential attack vectors and condensing the system’s attack surface. By removing superfluous programs, accounts functions, applications, ports, permissions, access, etc. attackers and malware have fewer opportunities to gain a foothold within your IT ecosystem.
There are multiple types of hardening and i will explain some below.
Although the principles of system hardening are universal, specific tools and techniques do vary depending on the type of hardening you are carrying out.
  - ***Application hardening:*** App hardening makes the application immune to both static and dynamic analysis. Static analysis refers to an attack where the hacker tries to decompile applications on a local machine. Dynamic attacks on the other hand manipulate apps by using a debugger tool or hooking frameworks.
  - ***OS Hardening(Operating system hardening):*** It involves patching and applying advanced system security procedures to secure the server's OS. Automatically installing updates, patches, and service packs are some of the most effective methods to harden the OS.
  An OS hardening is similar to application hardening in that the OS is a type of software. Operating system hardening provides basic software that grants those applications access to specific activities on your server.
  - ***Server hardening:*** Put all servers in a secure datacenter, never test hardening on production servers, always harden servers before connecting them to the internet or external networks, avoid installing unnecessary software on a server, segregate servers appropriately and ensure superuser and administrative shares are properly set up, and that the least privilige principle is set up correctly.
  - ***Database hardening:*** The purpose of database security hardening is to secure a database system, including its software and hardware components. This includes database client and server software, physical database server hosting machine, client machines, and firewalls. By reducing the attack surface of the systems, we can decrease the vulnerability. The attack surface can be reduced by eliminating redundant functionality and setting up the features securely and by creating a baseline of system functionality and security.
  - ***Network hardening:*** Ensure your firewall is properly configured and that all rules are regularly audited, secure remote access points and users, block/close any unused or unneeded open network ports, disable and remove unnecessary protocols and services, implement access lists and encrypt network traffic.
- ***DR(Disaster Recovery):*** Is an essential part of keeping data safe and maintaining business continuity. Its an organization’s method of regaining access and functionality to its IT infrastructure after events like a natural disaster, cyber attack, or any business disruption. A variety of disaster recovery (DR) methods can be part of a disaster recovery plan. The 5 most important elements of a good DR plan are:
1. Disaster recovery team
2. Risk evaluation
3. Business-critical asset identification
4. Backups
5. Testing and optimization.

Below i will talk about 4 of the top types of DR.
  - ***Data Center Disaster Recovery:*** In this approach, the disaster recovery plan is not just limited to the computing facility it’s housed in. The entire building plays a large role in data center DR. Features and tools within the building, such as physical security, support personnel, backup power, HVAC, utility providers, and fire suppression all have an effect on data center DR. In the event of any sort of outage, these elements within the building must be in working order. With these components working, your data is at a lower risk against intruders and cybercriminals. However, even if everything is functioning correctly, your data center can still be susceptible to a natural disaster.
  - ***Cloud-Based Disaster Recovery:*** When using a cloud-based approach, you’re able to cut costs by using a cloud provider’s data center as a recovery site, rather than spending more on your own data center’s facilities, personnel, and systems. Users also benefit from the competition between cloud providers, as they continue to attempt to best each other in the market. But before committing to this method, determine the challenges that providers may have with your business’ backup and recovery. The provider may be able to assist you in fixing those problems before the cloud becomes a part of your DR plan.
  - ***Virtualization Disaster Recovery:*** Virtualization negates the need to reconstruct a physical server in the event of a disaster. You are also able to achieve your targeted RTO more easily by placing a virtual server on reserve capacity or the cloud.
  - ***DRAAS(Disaster Recovery as a Service:)*** While Disaster Recovery as a Service (DRaaS) is often based in the cloud, it is not strictly cloud-based. Some DRaaS providers offer their solutions as a site-to-site service, in which they host and run a secondary hot site. Additionally, providers can rebuild and ship servers to an organization’s site as a server replacement service. On the other hand, cloud-based DRaaS enables users to failover applications immediately, orchestrate failback to rebuilt servers, and reconnect users through VPN or Remote Desktop Protocol.


## Exercise
### Sources
1. [YT](https://www.youtube.com/watch?v=rvKQtRklwQ4)
2. [YT2](https://www.youtube.com/watch?v=PhROeWMPBqU)
3. [app](https://www.appsealing.com/application-hardening/#:~:text=Application%20hardening%20is%20the%20process,large%20number%20of%20cyber%20attacks.)
4. [OS](https://www.javatpoint.com/operating-system-hardening)
5. [DB](https://security.berkeley.edu/education-awareness/database-hardening-best-practices)
6. [DR1](https://www.vmware.com/topics/glossary/content/disaster-recovery.html#:~:text=Disaster%20recovery%20is%20an%20organization's,of%20a%20disaster%20recovery%20plan.)
7. [DR2](https://solutionsreview.com/backup-disaster-recovery/top-three-types-of-disaster-recovery-plans/)


### Overcome challenges
Did not really understand everything that well, really had to re read alot of information.
This subject is one of the biggest time sinks ive ever seen and im very vulnerable for that. i had to force myself to stay focused a bit.
Not finding respone strategies.

### Results
#### A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?
In this example the RPO is 24 hours. They make a daily back up, so the maximum data loss is 24 hours.

#### An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?
In this example the RTO is 8 minutes, if the actual version of the web server would go down it would take the backup server 8 minutes to boot.