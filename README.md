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

## Hoe gebruik je het programma als CLI
- Download en unzip het bestand met alle scripts.
- Open je command prompt/powershell etc...
- ga naar het pad waar beide de dataset.json en de Program.py bestanden in staan met cd/map/map/... of kopieer het hele pad van de folder en plak het in de cmd
  
- Het ziet er ongeveer zo uit
- C:\Users\a>python C:\Users\a\OneDrive\Documenten\GitHub\SMP\SMP_Eindopdracht\SMP_Dataset_Tool\
- Vanaf nu kun je het script aanroepen met
- C:\Users\a>python C:\Users\a\OneDrive\Documenten\GitHub\SMP\SMP_Eindopdracht\SMP_Dataset_Tool\program.py
- Het zou moeten zeggen 'usage: program.py [-h] [--show-ips] [--threshold THRESHOLD] [--most-and-least] [--unique-hosts] file_name
- Je moet echter eerst de dataset aanroepen voordat je verder gaat, dit gaat zo **(klik niet op enter)**
- C:\Users\a>python C:\Users\a\OneDrive\Documenten\GitHub\SMP\SMP_Eindopdracht\SMP_Dataset_Tool\program.py dataset.json

- Vanaf hier kun je de 4 commando's uitvoeren

### C:\Users\a>python C:\Users\a\OneDrive\Documenten\GitHub\SMP\SMP_Eindopdracht\SMP_Dataset_Tool\program.py dataset.json --threshold THRESHOLD
- THRESHOLD wordt met een nummer verplaatst. so 1,2,3,4 etc... dat het bijvoorbeeld --threshold 2 maakt.
- Het laat in dit geval alle ip adressen zien van slachtoffers die 2 of meer pakketjes hebben binnengekregen per seconde en de aanvallers met hun ip-adressen en aantal verstuurde pakketjes.

### C:\Users\a>python C:\Users\a\OneDrive\Documenten\GitHub\SMP\SMP_Eindopdracht\SMP_Dataset_Tool\program.py dataset.json --most-and-least
- Laat top 5 meeste en minste hosts zien qua connecties met de webserver.

### C:\Users\a>python C:\Users\a\OneDrive\Documenten\GitHub\SMP\SMP_Eindopdracht\SMP_Dataset_Tool\program.py dataset.json --unique-hosts
- Laat aantal unieke hosts zien
  
### C:\Users\a>python C:\Users\a\OneDrive\Documenten\GitHub\SMP\SMP_Eindopdracht\SMP_Dataset_Tool\program.py dataset.json --unique-hosts --show-ips
- **Disclaimer: Kan alleen worden gebruikt door eerst --unique-hosts aan te roepen.**
- Laat alle ip-adressen zien van alle unieke hosts.

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

Er moet een script komen die een gebruiker een eigen drempelwaarde laat invullen voor pakketjes per seconden om zo te sorteren op een DDOS aanval. Een DDOS aanval is een aanval
waarbij iemand in enorm korte tijd misschien wel miljoenen pakketjes binnen kan krijgen. Omdat de dataset die wij gebruiken maar 3000 pakketjes binnenkrijgt over een tijd van 25 minuten
is het dus van belang dat de code dynamisch is en de gebruiker van het programma vrijheid geeft om te sorteren op waarden die ze zelf invullen. er komt een lijst met ip-adressen van 
slachtoffers en een lijst van ip-adressen met aanvallers. Bij de aanvallers zul je ook het aantal pakketten dat ze hebben verstuurd in dezelfde print terugzien.

### Script 3: Functionaliteit
**Disclaimer: in het geval van deze dataset zal je alleen bericht krijgen van een 'potentiele DDOS attack' als je 1 of 2 invult als drempelwaarde, in realiteit is dit vele malen groter**
- In de functie 'detect_ddos_attack' wordt gekeken hoeveel pakketten er binnenkomen per seconde en wordt er een drempelwaarde meegegeven.
- Er zijn lijsten en dictionaries van slachtoffers en attackers die worden gevuld door hun ip-adressen als de count gelijk of over de drempelwaarde is.
- Er wordt bijgehouden of dezelfde ip-adressen niet voorkomen in dezelfde aanval.
- Het totaal aantal aanvallen wordt bijgehouden na elke 'aanval' (zelfde aantal of hoger aantal pakketjes dan je drempelwaarde)
- Prints met aantal potentiele aanvallen in de dataset
- Prints met slachtoffers ip-adressen
- Prints met aanvallers ip-adressen (en hoeveel pakketten ze hebben verstuurd in de aanvallen)

## Test Sets 
- There are 2 testsets, one with positive and one with negative result.
- The goal of the tests was to see if I can properly search through a list of ip adresses and get results out of it
- I use PyTest for the tests so you have to use the following command to test it
- C:\Users\a\OneDrive\Documenten\GitHub\SMP\SMP_Eindopdracht\Tests> pytest file.py


