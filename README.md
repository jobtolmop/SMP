# System & Middleware Programming
## Job Tol - Klas IC 105

Als Cyber Security specialist moet je verschillende soorten gegevens kunnen doorzoeken. Om dit met de hand te doen is vrijwel onmogelijk, daarom worden er vaak tools gebruikt die dit voor ons doen. Deze tools zullen echter niet altijd de functionaliteiten hebben waar je naar zoekt, daarom moet je ook in staat zijn je eigen tools te schrijven.

De dataset die wordt behandeld bestaat uit opgevangen netwerk-traffic. Dit is traffic naar een webserver van een universiteit, en
de dataset bevat de pakketjes die je daarvan mag verwachten. Sommige hosts zijn verbonden met het
universiteitsnetwerk, en zitten daarom in hetzelfde subnet als de webserver, terwijl andere hosts vanaf een
andere locatie de website proberen te bezoeken. Hoewel de meeste hosts op de juiste manier
communiceren met de webserver, zijn er ook hosts in deze dataset die minder nobele doelen hebben: een
aantal proberen op de webserver in te breken, deze te overspoelen met verzoeken, of op een andere manier
de webserver uit de lucht te krijgen.

Voor deze opdracht ga ik met gemaakte programma's een dataset analyseren op potentieel interessante
informatie. Het programma levert vervolgens een rapportage op basis van deze analyse.

<br>
<br>

## Over Mijn Programma
## Main Script met alle functionaliteit: (Program.py)
in mijn programma heb ik voor de volgende 3 onderwerpen een script geschreven met een werkende Command Line Interface functionaliteit.
- Welke hosts communiceren het meest en minst met de webserver?
- Hoeveel verschillende hosts communiceren er met de webserver? (+ Functionaliteit van lijst met alle IP-adressen)
- Welke berichten zijn onderdeel van een DDOS aanval?

<br>
<br>


## Vraag 1: Hoeveel verschillende hosts communiceren er met de webserver?
Er moet een script worden geschreven die alle verschillende hosts uit de dataset worden gehaald. Het is hierbij belangrijk dat het geen dubbele gegevens bevat en het
zal hier dus op moeten checken. Verder om geen enorme lading aan data te creeeren zijn er functies te gebruiken in een CLI om of alleen het nummer van unieke hosts te laten
zien. Of een hele lijst met alle unieke hosts.

### Script 1: Functionaliteit
- In de functie **'amount_of_unique_hosts'** in het script **Program.py** wordt bepaald hoeveel verschillende hosts communiceren met de webserver.
- Eerst wordt er een lege lijst aangemaakt genaamd 'unique_hosts'
- Er wordt in een json dataset gekeken naar de ip-adressen van de 'source' en 'destination'
- Deze ip-adressen worden toegevoegd aan de lijst met unique_hosts
- Dubbele ip-adressen worden niet toegevoegd
- De lijst met uniquehosts wordt gereturned

<br>
<br>

## Vraag 2: Welke hosts communiceren het meest/minst met de webserver?
Er moet een script worden geschreven dat alle ip-adressen bijhoudt en hoeveel ze voorkomen in de dataset. Er moeten hierbij 2 prints komen, een met een top 5 van meest voorkomende
ip-adressen in de dataset en een print met de top 5 minst voorkomende ip-adressen in de dataset. Dezelfde ip-adressen mogen niet meerdere keren voorkomen in de prints.

### Script 2: Functionaliteit
- In de functie **'most_and_least'** in het script **Program.py** worden alle ip-source adressen verzameld.
- De connection_counter variabele houdt bij hoe vaak een ip-adres is gezien in de lijst van source adressen.
- Het pakt een top 5 van meeste en minste connecties met de variabelen most_connections & least_connections en returned deze waarden.
  
<br>
<br>

## Vraag 3: Welke berichten zijn onderdeel van een DDOS-aanval

- In de screenshots hieronder vind je frames van het eerste en laatste pakketje. De hele capture bedraagt 25 minuten / 1500 seconden.
- Er zijn 3001 pakketjes aanwezig, dus ongeveer 2 pakketjes per seconde.
- Om te sorteren op een DDOS aanval met deze dataset kan ik kijken welk ip-adres de meeste pakketjes ontvangt in welke seconden.
- Dan kijk ik naar de ip-adressen die de berichten heeft gestuurd naar het ip-adres(sen) die de meeste pakketjes heeft ontvangen
- Daarna pak ik die ip-adressen en kijk ik hoeveel pakketten ze versturen per seconden.
- Als er instanties komen dat bij een ip adres 10 of meer pakketjes worden verstuurd per seconden kun je er van uit gaan dat je te maken hebt met een aanval. 


