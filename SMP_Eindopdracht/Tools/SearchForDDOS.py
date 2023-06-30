# In de screenshots hieronder vind je frames van het eerste en laatste pakketje. 
#De hele capture bedraagt 25 minuten / 1500 seconden.
# Er zijn 3001 pakketjes aanwezig, dus ongeveer 2 pakketjes per seconde.

# Om te sorteren op een DDOS aanval met deze dataset kan ik kijken welk ip-adres de meeste 
#pakketjes ontvangt in welke seconden.

# Dan kijk ik naar de ip-adressen die de berichten heeft gestuurd naar het ip-adres(sen) 
#die de meeste pakketjes heeft ontvangen

# Daarna pak ik die ip-adressen en kijk ik hoeveel pakketten ze versturen per seconden.

# Als er instanties komen dat bij een ip adres 10 of meer pakketjes worden verstuurd per 
# seconden kun je er van uit gaan dat je te maken hebt met een aanval.

import json

def amount_of_packets_per_timestamp(json_data):
    packet_counts = {}

    for packet in json_data:
        frame_time = packet['_source']['layers']['frame']['frame.time']

        if frame_time not in packet_counts:
            packet_counts[frame_time] = 1
        else:
            packet_counts[frame_time] += 1

    return packet_counts

def detect_ddos_attack(packet_counts, json_data, threshold=2):
    attack_detected = False
    total_attempts = 0
    victims = set()
    attackers = set()

    for frame_time, count in packet_counts.items():
        if count >= threshold:
            victim_ip = json_data[0]['_source']['layers']['ip']['ip.dst']
            victim_attacks = set()

            for packet in json_data:
                src_ip = packet['_source']['layers']['ip']['ip.src']
                dst_ip = packet['_source']['layers']['ip']['ip.dst']

                if dst_ip == victim_ip:
                    attackers.add(src_ip)
                    victim_attacks.add(src_ip)

            print(f"Potentiele DDOS aanval op: {frame_time} met {count} verstuurde pakketjes.")
            print(f"Slachtoffer IP: {victim_ip}")
            print(f"Aanvaller IPs: {', '.join(victim_attacks)}")
            victims.add(victim_ip)
            attack_detected = True
            total_attempts += 1

    if attack_detected:
        print(f"\nEr zijn in totaal {total_attempts} mogelijke DDOS aanvallen geweest in deze dataset.")
        print(f"De slachtoffers zijn: {', '.join(victims)}")
        print(f"De aanvallers zijn: {', '.join(attackers)}")
    else:
        print("Geen DDOS aanval gedetecteerd.")

def main():
    with open("dataset.json", "r") as file:
        data = json.load(file)

    packet_counts = amount_of_packets_per_timestamp(data)
    detect_ddos_attack(packet_counts, data, threshold=2)

main()
