# Vraag 3: Welke berichten zijn onderdeel van een DDOS-aanval

# In de screenshots hieronder vind je frames van het eerste en laatste pakketje. 

# De hele capture bedraagt 25 minuten / 1500 seconden.
# Er zijn 3001 pakketjes aanwezig, dus ongeveer 2 pakketjes per seconde.

# Om te sorteren op een DDOS aanval met deze dataset kan ik kijken welk 
# ip-adres de meeste pakketjes ontvangt in welke seconden.

# Dan kijk ik naar de ip-adressen die de berichten heeft gestuurd 
# naar het ip-adres(sen) die de meeste pakketjes heeft ontvangen
# Daarna pak ik die ip-adressen en kijk ik hoeveel pakketten ze versturen per seconden.

# Als er instanties komen dat bij een ip adres 10 of meer pakketjes worden 
# verstuurd per seconden kun je er van uit gaan dat je te maken hebt met een aanval.