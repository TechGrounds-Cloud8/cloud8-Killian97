# Processes 
Install telnet, find information about tellnet on your machine and close tellnet

## Key terminology
 - ***apt install packagename:*** Met deze command kan je iets instaleren
 - ***systemct1 status servicename:*** Met deze command kan je de status checken van een service
 - ***PID:*** Betekend Process ID.
 - ***kill PID:*** Hiermee kill je een process met het aangeven PID.
 - ***killall name*** Hiermee kill je alle processen met die naam.
 - ***Daemon:*** Een daemon is een process dat runt in de background.
 


## Exercise
### Sources
1. [tellnet install, PID check, memory check](https://www.howtoforge.com/how-to-install-and-use-telnet-on-ubuntu/)
2. [kill telnet](https://itsfoss.com/how-to-find-the-process-id-of-a-program-and-kill-it-quick-tip/)
3. [kill](https://www.geeksforgeeks.org/kill-command-in-linux-with-examples/?ref=lbp)




### Overcome challenges
moest leren over telnet en wat het was. Elke keer als we telnet killde kwam er een nieuw process met een andere PID.


### Results

1. Hier installeer ik een daemon en daarna check ik de status van die daemon.
![SS](../../00_includes/LNX-06/instaltellnet.png)

2. Hier zie je het onderste stukje van results 1 en check ik de PID en zie ik de use of memory.
![SS](../../00_includes/LNX-06/PID.png)

3. Hier kill ik alle processen van de inet daemon
![SS](../../00_includes/LNX-06/killtelnet.png)

