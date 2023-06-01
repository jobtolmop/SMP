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

    

def main():
    with open("dataset.json", "r") as file:
        data = json.load(file)

        most_and_least(data)

main()