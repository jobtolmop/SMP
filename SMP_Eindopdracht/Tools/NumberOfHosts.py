# Vraag 1: Hoeveel verschillende hosts communiceren er met de webserver

# Hier moet een script voor worden geschreven en wordt gezocht op ip-adressen 
# uit de meegekregen dataset.

# Verder moet er een for loop komen om geen zelfde IP adressen mee te tellen.

# Alle verschillende ip-adressen worden geprint met het aanroepen van de functie, 
# en de laatste print zal bestaan uit ‘er zijn X aantal verschillende ip-adressen in de dataset’

import json
from collections import Counter

def amount_of_unique_hosts(json_data):
    unique_hosts = []

    for packet in json_data:
        src_host = packet['_source']['layers']['ip']['ip.src_host']
        dst_host = packet['_source']['layers']['ip']['ip.dst_host']

        if src_host not in unique_hosts:
            unique_hosts.append(src_host)
        if dst_host not in unique_hosts:
            unique_hosts.append(dst_host)

    return len(unique_hosts)

def main():
    with open("dataset.json", "r") as file:
        data = json.load(file)

    num_unique_hosts = amount_of_unique_hosts(data)
    print("Amount of different hosts:", num_unique_hosts)

main()

