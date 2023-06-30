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

            print(f"Potential DDoS attack detected at timestamp {frame_time} with {count} packets.")
            print(f"Victim IP: {victim_ip}")
            print(f"Attacker IPs: {', '.join(victim_attacks)}")
            victims.add(victim_ip)
            attack_detected = True
            total_attempts += 1

    if attack_detected:
        print(f"\nIn total, there were {total_attempts} DDoS attempts.")
        print(f"The victims are: {', '.join(victims)}")
        print(f"The attackers are: {', '.join(attackers)}")
    else:
        print("No DDoS attack detected.")

def main():
    with open("dataset.json", "r") as file:
        data = json.load(file)

    packet_counts = amount_of_packets_per_timestamp(data)
    detect_ddos_attack(packet_counts, data, threshold=2)

main()
