# Hier een script waarmee je sorteert op DDOS aanvallen.

import json


def amount_of_packets_per_timestamp(json_data):
    packet_counts = {}

    # Pakt json data en stelt een variabele frame_time gelijk aan de packet-frame time in de json dataset
    for packet in json_data:
        frame_time = packet['_source']['layers']['frame']['frame.time']

        # kijkt of de frame_time al in de dictionary zit anders wordt packet_counts +1 gedaan in de dictionary
        if frame_time not in packet_counts:
            packet_counts[frame_time] = 1
        else:
            packet_counts[frame_time] += 1

    return packet_counts

# Functie die de packet_counts out de eerdere dictionary pakt, de json data pakt en een threshold pakt
# De threshold geeft de minimale eis wanneer het aan een DDOS aanval doet (pakketjes/seconden)
def detect_ddos_attack(packet_counts, json_data, threshold=1):
    # Variabelen om te bepalen of er een aanval is, hoeveel aanvallen er zijn geweest
    attack_detected = False
    total_attempts = 0
    victims = set()
    attackers = {}

    # Als het aantal pakketjes gelijk of boven de gegeven threshold is wordt het ip van slachtoffer opgehaald
    # uit de json dataset
    for frame_time, count in packet_counts.items():
        if count >= threshold:
            victim_attacks = set()

            # Pakt de frame.time en de destionation/source ips uit de json dataset
            for packet in json_data:
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
                print(f"Potentiele DDOS aanval op: {frame_time} met {count} verstuurde pakketjes.")
                print(f"Slachtoffer IP: {victim_ip}")
                print(f"Aanvaller IPs: {', '.join(victim_attacks)}")
                victims.add(victim_ip)
                # Als het overeen komt met de threshold is er een aanval gedetecteerd en gaat de total counter omhoog
                attack_detected = True
                total_attempts += 1

    # Prints met het totaal aantal potentiele DDOS aanvallen met ips van slachtoffers en aanvallers
    if attack_detected:
        print(f"\nEr zijn in totaal {total_attempts} mogelijke DDOS aanvallen geweest in deze dataset.")
        print(f"\nDe slachtoffers zijn: {', '.join(victims)}")
        print("\nDe aanvallers zijn:")
        for attacker, count in attackers.items():
            if count >= threshold:
                print(f"{attacker}: {count} packets")
    else:
        print("Geen DDOS aanval gedetecteerd.")


def main():
    with open("dataset.json", "r") as file:
        data = json.load(file)

    packet_counts = amount_of_packets_per_timestamp(data)

    # Gebruiker mag zelf een threshold invullen over hoeveel pakketjes hun denken op te sorteren om te kijken
    # of het een potentiele DDOS aanval is.
    threshold = int(input("Geef een waarde weer van pakketjes/seconden waarop jij wilt checken op een DDOS aanval: "))
    detect_ddos_attack(packet_counts, data, threshold=threshold)

main()
