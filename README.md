# System & Middleware Programming
## Job Tol - Klas IC 105

PROBLEEMSTELLING<br>
PROBLEEMSTELLING<br>
PROBLEEMSTELLING<br>
PROBLEEMSTELLING<br>
PROBLEEMSTELLING<br>

## Vraag 1:
**Hoeveel verschillende hosts communiceren er met de webserver**
- Hier moet een script voor worden geschreven en wordt gezocht op ip-adressen uit de meegekregen dataset.
- Verder moet er een for loop komen om geen zelfde IP adressen mee te tellen.
- Alle verschillende ip-adressen worden geprint met het aanroepen van de functie, en de laatste print zal bestaan uit ‘er zijn X aantal verschillende ip-adressen in de dataset’

**Hier komt een script van vraag 1 samen met documentatie**

## Vraag 2:
**Welke hosts communiceren het meest/minst met de webserver**
- Hier moet een script worden geschreven die alle ip adressen bijhoudt en hoeveel ze voorkomen in de dataset.
- Er komen 2 prints, een met een top 5 meeste communicatie met de webserver en een met top 5 minste communicatie met de webserver.
- Dezelfde ip-adressen mogen niet meerdere keren voorkomen in de prints.

**Hier komt een script van vraag 2 samen met documentatie**

## Vraag 3:
**Welke berichten zijn onderdeel van een DDOS-aanval**
- In de screenshots hieronder vind je frames van het eerste en laatste pakketje. De hele capture bedraagt 25 minuten / 1500 seconden.
- Er zijn 3001 pakketjes aanwezig, dus ongeveer 2 pakketjes per seconde.
- Om te sorteren op een DDOS aanval met deze dataset kan ik kijken welk ip-adres de meeste pakketjes ontvangt in welke seconden.
- Dan kijk ik naar de ip-adressen die de berichten heeft gestuurd naar het ip-adres(sen) die de meeste pakketjes heeft ontvangen
- Daarna pak ik die ip-adressen en kijk ik hoeveel pakketten ze versturen per seconden.
- Als er instanties komen dat bij een ip adres 10 of meer pakketjes worden verstuurd per seconden kun je er van uit gaan dat je te maken hebt met een aanval. 

**Hier komt een script van vraag 3 samen met documentatie**
