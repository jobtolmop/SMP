# Hier een script waarmee alle verschillende IP-adressen worden laten zien uit een json dataset.

import json

# Functie waarin de JSON data wordt gepakt en het false zetten van de parameter show_ips
# Lege lijst voor unieke hosts
def amount_of_unique_hosts(json_data, show_ips=False):
    unique_hosts = []

    # Voor de variabelen src host en dst host wordt hun IP adress gepakt uit de dataset
    for packet in json_data:
        src_host = packet['_source']['layers']['ip']['ip.src_host']
        dst_host = packet['_source']['layers']['ip']['ip.dst_host']

        # Alleen unieke IP's worden toegevoegd aan de unique_hosts lijst met een append.  
        if src_host not in unique_hosts:
            unique_hosts.append(src_host)
        if dst_host not in unique_hosts:
            unique_hosts.append(dst_host)

    # Als de gebruiker alle IP's wilt zien worden ze hier geprint (zie show_ip_adresses in main functie)
    if show_ips:
        print("Lijst met alle IP-adressen:")
        for ip in unique_hosts:
            print(ip)

    # Returnt lengte van unique_hosts lijst
    return len(unique_hosts)


# Main functie waarin ik de dataset open met 'r' (read) en een variabele data meegeef die ik gelijk 
# stel aan de json file data.
def main():
    with open("dataset.json", "r") as file:
        data = json.load(file)

    # Data uit de functie amount_of_unique_hosts wordt gezet in een nieuwe variabele
    num_unique_hosts = amount_of_unique_hosts(data)

    # Aantal unieke hosts wordt geprint
    print("Aantal unieke Hosts:", num_unique_hosts)

    # Extra optie, laat gebruiker van script alle aparte IP-adressen zien als ze 'ja/Ja/JA' typen
    show_ip_adresses = input("Wil je de lijst met IP adressen zien? (Ja / Nee): ")

    if show_ip_adresses.lower() == 'ja':
        amount_of_unique_hosts(data, show_ips=True)

main()


