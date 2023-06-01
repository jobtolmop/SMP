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

## Vraag 1: Hoeveel verschillende hosts communiceren er met de webserver
- Hier moet een script voor worden geschreven en wordt gezocht op ip-adressen uit de meegekregen dataset.
- Verder moet er een for loop komen om geen zelfde IP adressen mee te tellen.
- Alle verschillende ip-adressen worden geprint met het aanroepen van de functie, en de laatste print zal bestaan uit ‘er zijn X aantal verschillende ip-adressen in de dataset’

**Hier komt een script van vraag 1 samen met documentatie**

<br>
<br>

## Vraag 2: Welke hosts communiceren het meest/minst met de webserver
- Hier moet een script worden geschreven die alle ip adressen bijhoudt en hoeveel ze voorkomen in de dataset.
- Er komen 2 prints, een met een top 5 meeste communicatie met de webserver en een met top 5 minste communicatie met de webserver.
- Dezelfde ip-adressen mogen niet meerdere keren voorkomen in de prints.

**Script Vraag 2: MostAndLeast.py**


```py
# Hier een script waarmee ik de meeste en minste connecties naar een webserver pak uit de dataset.json
# De counter Module wordt gebruikt om de ips op te slaan en weer te geven hoevaak ze voorkomen.

import json
from collections import Counter

def most_and_least(data): 

    # Maak een variabele waarin je de ip adressen en hun source pakt van uit de JSON file
    ip_addresses = [entry['_source']['layers']['ip']['ip.src'] for entry in data]

    # Verzamel connecties gesorteerd op ip.
    connection_counter = Counter(ip_addresses)

    # Pak de top 5 hosts die de meeste connecties met de webserver maken
    most_connections = connection_counter.most_common(5)
    print("IP adressen van de top 5 hosts die de meeste connecties maken met de webserver:")
    for host, count in most_connections:
        print(f"{host}: {count} connections")

    # Pak de top 5 hosts die de minste connecties met de webserver maken
    least_connections = connection_counter.most_common()[:-6:-1]
    print("\nIP adressen van de top 5 hosts die de minste connecties maken met de webserver:")
    for host, count in least_connections:
        print(f"{host}: {count} connections")

# Main functie waarin ik de dataset open met 'r' (read) en een variabele data meegeef die ik gelijk 
# stel aan de json file data.

def main():
    with open("dataset.json", "r") as file:
        data = json.load(file)

        most_and_least(data)

main()
```

**Hier komt documentatie van kleine stukjes code**

<br>
<br>

## Vraag 3: Welke berichten zijn onderdeel van een DDOS-aanval
- In de screenshots hieronder vind je frames van het eerste en laatste pakketje. De hele capture bedraagt 25 minuten / 1500 seconden.
- Er zijn 3001 pakketjes aanwezig, dus ongeveer 2 pakketjes per seconde.
- Om te sorteren op een DDOS aanval met deze dataset kan ik kijken welk ip-adres de meeste pakketjes ontvangt in welke seconden.
- Dan kijk ik naar de ip-adressen die de berichten heeft gestuurd naar het ip-adres(sen) die de meeste pakketjes heeft ontvangen
- Daarna pak ik die ip-adressen en kijk ik hoeveel pakketten ze versturen per seconden.
- Als er instanties komen dat bij een ip adres 10 of meer pakketjes worden verstuurd per seconden kun je er van uit gaan dat je te maken hebt met een aanval. 

**Hier komt een script van vraag 3 samen met documentatie**
