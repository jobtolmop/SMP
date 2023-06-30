import json
from collections import Counter


class DataAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    def load_data(self):
        # Functie om de dataset in te laden vanuit het JSON-bestand.
        with open(self.file_name, "r") as file:
            self.data = json.load(file)

    def most_and_least(self):

        # Functie om de IP-adressen met de meeste en minste connecties naar een webserver te tonen.
        ip_addresses = [entry['_source']['layers']['ip']['ip.src'] for entry in self.data]
        connection_counter = Counter(ip_addresses)

        most_connections = connection_counter.most_common(5)
        print("IP adressen van de top 5 hosts die de meeste connecties maken met de webserver:")
        for host, count in most_connections:
            print(f"{host}: {count} connecties")

        least_connections = connection_counter.most_common()[:-6:-1]
        print("\nIP adressen van de top 5 hosts die de minste connecties maken met de webserver:")
        for host, count in least_connections:
            print(f"{host}: {count} connecties")

    def amount_of_unique_hosts(self, show_ips=False):
        # Functie om het aantal unieke hosts in de dataset te bepalen.
        # Optioneel kan de lijst met IP-adressen worden weergegeven.
        unique_hosts = []

        for packet in self.data:
            src_host = packet['_source']['layers']['ip']['ip.src_host']
            dst_host = packet['_source']['layers']['ip']['ip.dst_host']

            if src_host not in unique_hosts:
                unique_hosts.append(src_host)
            if dst_host not in unique_hosts:
                unique_hosts.append(dst_host)

        if show_ips:
            print("Lijst met alle IP-adressen:")
            for ip in unique_hosts:
                print(ip)

        return len(unique_hosts)

    def amount_of_packets_per_timestamp(self):
        # Functie om het aantal pakketten per tijdstempel te bepalen.
        packet_counts = {}

        for packet in self.data:
            frame_time = packet['_source']['layers']['frame']['frame.time']

            if frame_time not in packet_counts:
                packet_counts[frame_time] = 1
            else:
                packet_counts[frame_time] += 1

        return packet_counts

    def detect_ddos_attack(self, threshold=1):
        # Functie om DDOS-aanvallen te detecteren op basis van het aantal pakketten per tijdstempel.
        # Een optionele drempelwaarde kan worden opgegeven om te bepalen wanneer er sprake is van een aanval.
        packet_counts = self.amount_of_packets_per_timestamp()
        attack_detected = False
        total_attempts = 0
        victims = set()
        attackers = {}

        for frame_time, count in packet_counts.items():
            if count >= threshold:
                victim_attacks = set()

                for packet in self.data:
                    frame_time_packet = packet['_source']['layers']['frame']['frame.time']
                    dst_ip = packet['_source']['layers']['ip']['ip.dst']
                    src_ip = packet['_source']['layers']['ip']['ip.src']

                    if frame_time_packet == frame_time:
                        victim_ip = dst_ip

                        if src_ip not in attackers:
                            attackers[src_ip] = 1
                        else:
                            attackers[src_ip] += 1

                        victim_attacks.add(src_ip)
                # Als er een victim is is er sprake van een aanval, print met het ip van slachtoffer/aanvaller
                if len(victim_attacks) > 0:
                    print(f"Potentiële DDOS-aanval op: {frame_time} met {count} verstuurde pakketten.")
                    print(f"Slachtoffer IP: {victim_ip}")
                    print(f"Aanvaller IPs: {', '.join(victim_attacks)}")
                    victims.add(victim_ip)
                # Als het overeen komt met de threshold is er een aanval gedetecteerd en gaat de total counter omhoog
                    attack_detected = True
                    total_attempts += 1

        # Prints met het totaal aantal potentiele DDOS aanvallen met ips van slachtoffers en aanvallers
        if attack_detected:
            print(f"\nEr zijn in totaal {total_attempts} mogelijke DDOS-aanvallen geweest in deze dataset.")
            print(f"\nDe slachtoffers zijn: {', '.join(victims)}")
            print("\nDe aanvallers zijn:")
            for attacker, count in attackers.items():
                if count >= threshold:
                    print(f"{attacker}: {count} pakketten")
        else:
            print("Geen DDOS-aanval gedetecteerd.")


def main():
    analyzer = DataAnalyzer("dataset.json")
    analyzer.load_data()

    analyzer.most_and_least()

    num_unique_hosts = analyzer.amount_of_unique_hosts()
    print("\nAantal unieke Hosts:", num_unique_hosts)

    show_ips = input("Wil je de lijst met IP-adressen zien? (Ja/Nee): ")
    if show_ips.lower() == 'ja':
        analyzer.amount_of_unique_hosts(show_ips=True)

    threshold = input("\nGeef een waarde weer van pakketjes/seconden waarop je wilt checken op een DDOS-aanval: ")
    try:
        threshold = int(threshold)
        analyzer.detect_ddos_attack(threshold=threshold)
    except ValueError:
        print("Voer een geheel getal in alstublieft.")


if __name__ == '__main__':
    main()
