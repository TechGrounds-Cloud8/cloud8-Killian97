# IP adresses
Study Forms of Ip adresses, NAT and static and dynamic adresses. apply this knowledge to find and change the adresses of some devices

## Key terminology
- ***IP Adress (Internet Protocol):*** A IP is a unique adress that i dentifies a device on the Internet or LAN. A IP adress is a string of numbers seperated by periods and every number can go from 0-255 so the full range is from 0.0.0.0 to 255.255.255.255.
- ***Private IP adress:*** A private IP adress is a adress given by your router to every device in your home network. Every device gets a unique private IP adress. This way a router can identify the devices seperately.
- ***Public IP adress:*** A public IP adress is the main IP adress for your entire home network. Your devices still have their own private IP adress but are also included in this Public IP adress. Your public IP address is provided to your router by your ISP. Typically, ISPs have a large pool of IP addresses that they distribute to their customers. Your public IP address is the address that all the devices outside your internet network will use to recognize your network.
- ***Dynamic Adress:*** Dynamic adresses change automatically and are assigned by ISP's, ISP's change the adresses to save costs. For example when someone moves they dont need to change their adress manually since it happens anyway. Adress that get taken away can be re applied to a different customer. Changing adresses also increases security since hackers cant focus on 1 IP adress.
- ***Static adress:*** In contrast to dynamic IP addresses, static addresses remain the same Once the network assigns an IP address, it remains the same. Most individuals and businesses do not need a static IP address, but for businesses that plan to host their own server, it is very important to have one. This is because a static IP address makes sure that websites and email addresses tied to it will have a consistent IP address, this is vital if you want other devices to be able to find them consistently on the web.
- ***IPv4:*** IPv4 is the first version of IP to identify devices on a network. It uses a 32bit scheme to store more then 4 billion adresses. Still the world ran out of adresses and IPv6 was born.
- ***IPv6:*** Pv6 is the most recent version of the Internet Protocol. This new IP address version is being deployed to fulfill the need for more Internet addresses. The goal was to resolve issues that are associated with IPv4. With 128-bit address space, it allows 340 undecillion unique addresses.
- ***NAT(network address translation):*** The nat makes you able to google for example. When you google for a banana picture on your PC you send a request to your router wich sends it onto the web but the web doesnt know where to send it back to. This gets solved by NAT because NAT makes your router change the private IP adress into your networks Public IP adress. This is a adress the web can find so it will send the banana picture there and it will end up on your device.



## Exercise
### Sources
1. [IP](https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address)
2. [IPV](https://www.guru99.com/difference-ipv4-vs-ipv6.html)
3. [NAT](https://www.comptia.org/content/guides/what-is-network-address-translation#:~:text=NAT%20stands%20for%20network%20address,as%20do%20most%20home%20routers.)


### Overcome challenges


### Results
1.  The public adress of my laptop and my phone are the same. This question is kinda of a trap. Read my Public IP Key term for explanation.
2. The Private IP of my Laptop and my phone are different because my router gives all devices in our network a UNIQUE ip adress. ranging from our sound system to our electric timed Coffee machine.

## Change the Private IP from your phone to the Private IP from your laptop what happens?

## Change the Private IP from your phone to a IP outside your local network

Both Assignments aren't doable for me, i dont have the option to change IP adresses in my router. What i can do is set the range for my DCHP start and end IP adress.