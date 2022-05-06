# Users and Groups
Create a new user with permissions and locate that new user in the users file

## Key terminology
 - ***Hash:*** Hiermee kun je een wachtwoord encrypten, een hashed password kan niet meer gelezen worden.
 - ***usermod -a -g:*** Met deze command kun je een bestaande user aan een group toevoegen.
 - ***sudo:*** Als een user Sudo rechten heeft kan die user met de command sudo dingen doen in bestanden waar hij eigenlijk geen permissie toe heeft.
 - ***useradd name:*** Met deze command kan je een nieuwe user aanmaken. 

 


## Exercise
### Sources
1. [add user to group](https://phoenixnap.com/kb/how-to-create-sudo-user-on-ubuntu)
2. [hoe lees ik passwd file](https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/)




### Overcome challenges
moeite hebben met het lezen van de bestanden, puur mijn dislexie zorgt er voor dat bijvoorbeeld het mapje passws door me kaar gaat als ik het probeer te lezen.
dit kost mij gewoon extra tijd en ook wat energie maar het lukt wel.


### Results

1. Hier laat ik zien dat mijn nieuwe user Nova in de Sudo group zit en in de Admin group.
![SS](../../00_includes/LNX-04/newusr.png)

2. Hier laat ik zien dat ik de files heb gevonden die de users passwords en groups opslaat, en het bestand waar de echte passwords staan opgeslagen en ge hashed.
![SS](../../00_includes/LNX-04/pwproof.png)