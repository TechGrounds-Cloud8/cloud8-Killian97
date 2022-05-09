# Cron jobs 
Learn what cron is and create a cron job that runs on scheduled moments.

## Key terminology
 - ***crontab (crontable):*** a list with all the commands that have to be executed scheduled.
 - ***crontab -e:*** Met deze command edit je de crontable en kan je cronjobs toevoegen.
 - ***date:*** Met deze command 
 - ***df (Disk-Free):*** Met deze command check je de disk space van je current server.
 


## Exercise
### Sources
1. [crontabs](https://www.freecodecamp.org/news/cron-jobs-in-linux/)
2. a friend who works with servers and linux
3. [diskspace check](http://blog.imm.cnr.it/content/linux-check-disk-space-command-view-system-disk-usage-df-and-du)



### Overcome challenges
never ever heard from crontabs. had to ask a friend who is a server maintainer what it was cause i was talking with him while doing the assignment.
ik had ook wel struggles met de manier van de cron tab invullen met * * * * etcetc


### Results

1. Hier zie je mijn edit aan de crontab waar ik mijn gemaakte script elke minuut laat runnen.
![SS](../../00_includes/LNX-08/crontab.png)

2. Hier zie je dat mijn script heeft gewerkt en mijn date elke minuut word ge print en ge append naar date.txt
![SS](../../00_includes/LNX-08/datepm.png)

3. Hier voeg ik mijn volgende script toe om elke vrijdag de disk space van de remote server en dat word ook ge append naar diskspace.txt
![SS](../../00_includes/LNX-08/diskspace.png)
