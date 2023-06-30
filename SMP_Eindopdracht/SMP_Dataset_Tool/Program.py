import argparse
import json
from collections import Counter
import os


class DataAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = None

    def load_data(self):
        # Pakt het pad van het scriptbestand
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, self.file_name)

        # Laad de dataset vanuit het pad
        with open(file_path, "r") as file:
            self.data = json.load(file)

    def most_and_least(self):
        # Functie om de IP-adressen met de meeste en minste connecties naar een webserver te tonen.
        ip_addresses = [entry['_source']['layers']['ip']['ip.src'] for entry in self.data]
        connection_counter = Counter(ip_addresses)

        most_connections = connection_counter.most_common(5)
        least_connections = connection_counter.most_common()[:-6:-1]

        return most_connections, least_connections

    def amount_of_unique_hosts(self):
        unique_hosts = []

        for packet in self.data:
            src_host = packet['_source']['layers']['ip']['ip.src_host']
            dst_host = packet['_source']['layers']['ip']['ip.dst_host']

            if src_host not in unique_hosts:
                unique_hosts.append(src_host)
            if dst_host not in unique_hosts:
                unique_hosts.append(dst_host)

        return unique_hosts

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

                # Als er een slachtoffer is, is er sprake van een aanval.
                # Print het IP-adres van het slachtoffer en de aanvallers.
                if len(victim_attacks) > 0:
                    victims.add(victim_ip)
                    attack_detected = True
                    total_attempts += 1

        # Print het totale aantal potentiele DDOS-aanvallen, slachtoffers en aanvallers.
        if attack_detected:
            print(f"Er zijn in totaal {total_attempts} mogelijke DDOS-aanvallen in deze dataset.")
            print(f"De slachtoffers zijn: {', '.join(victims)}")
            print("De aanvallers zijn:")
            for attacker, count in attackers.items():
                if count >= threshold:
                    print(f"{attacker}: {count} pakketten")
        else:
            print("Geen DDOS-aanval gedetecteerd.")

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


def main():
    parser = argparse.ArgumentParser(description="Data Analyzer Tool")
    parser.add_argument("file_name", help="Naam van het datasetbestand")
    parser.add_argument("--show-ips", action="store_true", help="Toon de lijst met IP-adressen")
    parser.add_argument("--threshold", type=int, help="Specificeer de drempelwaarde voor het aantal pakketten per seconde om DDOS-aanvallen te detecteren")
    parser.add_argument("--most-and-least", action="store_true", help="Toon de top 5 IP-adressen met de meeste en minste connecties")
    parser.add_argument("--unique-hosts", action="store_true", help="Toon het aantal unieke hosts")
    args = parser.parse_args()

    analyzer = DataAnalyzer(args.file_name)
    analyzer.load_data()

    if args.most_and_least:
        most_connections, least_connections = analyzer.most_and_least()
        print("IP adressen van de top 5 hosts die de meeste connecties maken met de webserver:")
        for host, count in most_connections:
            print(f"{host}: {count} connecties")

        print("\nIP adressen van de top 5 hosts die de minste connecties maken met de webserver:")
        for host, count in least_connections:
            print(f"{host}: {count} connecties")

    if args.unique_hosts:
        unique_hosts = analyzer.amount_of_unique_hosts()
        print("\nAantal unieke hosts:", len(unique_hosts))

        if args.show_ips:
            print("Lijst met alle IP-adressen:")
            for ip in unique_hosts:
                print(ip)

    if args.threshold:
        analyzer.detect_ddos_attack(threshold=args.threshold)


if __name__ == '__main__':
    main()
