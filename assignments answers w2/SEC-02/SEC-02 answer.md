# Firewalls
Install a web server and set your firewall to only allow SSH traffic

## Key terminology
- ***Web page:*** Is a document that can be displayed in a web browser, for example google chrome.
- ***Website:*** A collection of web pages.
- ***Web server:*** This is a machine(computer) that hosts a website on the internet.
- ***sudo ufw allow portID:*** With this command you can allow ports trough the firewall. Making it able to receive data trough that port.
- ***sudo ufw deny portID:*** With this command you can deny traffic trough a specific port.
- ***ufw(uncomplicated firewall):*** Is the basic firewall for Ubuntu, it is a easy to use firewall since you can edit it with your command line.
- ***Firewall:*** A Firewall is a network security that checks incoming and outgoing data with a set of rules. Data is moving in the form of packets. A firewall checks these packets based on those set rules. This way you can create a lets say shield around your network and protect it from unwanted data or even other users.
- ***Software Firewall:*** This is also known as the host firewall because it is installed on a hosts device. A host firewall is unique for that device its installed on, this allows the firewall to see the differences between programs while filtering traffic. This allows the firewall to deny acces to 1 program but allow that same data for another program. The disadvantage of this type of firewall is that all devices need their own firewall, and it takes up space on every device. 
- ***Hardware Firewall:*** If you know what hardware means you also know that a hardware firewall is a seperate device placed between your internal and external network. Unlike a software firewall that needs a host and needs the hosts resources a hardware firewall has his own recources. Hardware firewalls are easier to use for bigger companies since they can place lets say 2 firewalls to shield 20 computers. If they would use software firewalls they needed 20 firewalls and 20 times the resources.
- ***Packet filtering firewall:*** This is the most basic form of firewall. This firewall is attached to your router and filters the packets that come trough. This type of firewall decides whether a packet is allowed or denied access based on the header information. To do so, it inspects the protocol, source IP address, destination IP, source port, and destination port. A big disadvantage and security risc is that this firewall only checks the packet headers and not the payload.
- ***Circuit-Level Gateways:*** This firewall works at the session layer of the OSI model. It observes TCP connections and sessions and checks if the connection is actually safe. These firewalls are usually build in a other firewall or a software already installed. Similar to the firewall above (packet filter) this firewall does not check the payload but only the transaction information.
- ***Proxy firewall:*** A proxy firewall serves as an intermediate device between internal and external systems communicating over the Internet. It protects a network by forwarding requests from the original client and masking it as its own. When a client sends a request to access a web page, the message is intercepted by the proxy server. The proxy forwards the message to the web server, pretending to be the client. Doing so hides the client’s identification and geolocation, protecting it from any restrictions and potential attacks. The web server then responds and gives the proxy the requested information, which is passed on to the client.
- ***Next Generation Firewall:*** This firewall is a expensive combination of other firewalls, its a seperate device that combines packet, statefull, and deep packet inspection. Unlike traditional firewalls, the next-gen firewall inspects the entire transaction of data, including the TCP handshakes, surface-level, and deep packet inspection not just solely the header information.
- ***Cloud Firewall:*** A cloud firewall or firewall-as-a-service (Faas) is a cloud solution for network protection. Like other cloud solutions, it is maintained and run on the Internet by third-party vendors. Clients often utilize cloud firewalls as proxy servers, but the configuration can vary according to the demand. Their main advantage is scalability. They are independent of physical resources, which allows scaling the firewall capacity according to the traffic load.
- ***Statefull Firewall:*** A stateful firewall collects data regarding every connection made through it. All of these data points form profiles of “safe” connections. When a subsequent connection is attempted, it is checked against the list of attributes collected by the stateful firewall. If it has the qualities of a safe connection, it is allowed to proceed. If not, the data packets are discarded. A stateful firewall performs packet inspection, which checks the contents of packets to see if they pose threats.
Stateful firewalls can also integrate additional services, such as encryption or tunnels. These boost performance because they block malicious actors from reading the contents of communications, thereby making the connection safer through access control.
- ***Stateless Firewall:*** Is also known as an access control list (ACL), it does not store information on the connection state. Stateless ACLs are applicable to the network and physical layers, and sometimes the transport layer to find out the source and destination port numbers. When the sender sends a packet and it gets filtered through the firewall, the device checks for matches to any of the ACL rules that are configured in the firewall and then drops or rejects the packet accordingly. A big disadvantage of this is that these firewalls, in many instances need to be carefully configured by someone familiar with the kinds of traffic and attacks that impact the network. This will require extra time and energy to perform.




## Exercise
### Sources
1. [webserv](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Pages_sites_servers_and_search_engines)
2. [webserv2](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)
3. [ping](https://docs.microsoft.com/en-us/answers/questions/628271/problem-accessing-ports-443-and-80-on-a-ubuntu-vm.html)
4. [UFW](https://www.linode.com/docs/guides/configure-firewall-with-ufw/
)
5. [ufw](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
6. [firewall](https://www.forcepoint.com/cyber-edu/firewall)
7. [firewalls](https://phoenixnap.com/blog/types-of-firewalls)

### Overcome challenges
lots and lots of stress because i coudnt reach the default apache page. and not understanding why not. I solved or my LC solved this by explaining some things about inbound and outbound requests.

### Results
1. I already had apache installed so i tried to connect to the apache standard page, this didnt work and i got a error that the page wasnt reachable. When i tried to ping port 80 i noticed that port 80 was closed. After some heavy thinking and some tips from my learning coach i realised that with our entire class there was no way we could all use port 80. I found out that i had to use my unique port 55809. 
In this screenshot below you will see i reached the default page from my installed webserver. and for a fun thing i changed the title of the page in the HTML file.
![apachedef](../../00_includes/SEC-02/apdefpage.png)
In the screenshot below you can see i added a rule to the ufw that allowes incoming traffic from apache (my installed webserver).
![ufwap](../../00_includes/SEC-02/ufwap.png)

2. In the screenshot below you can see i added rules to ufw that allows SSH traffic but blocks web traffic. the result of this is that i cannot acces my default apache page anymore.

![httpblock](../../00_includes/SEC-02/httpblock.png)




