import scapy.all as scapy

def sniff_packets(interface):
    scapy.sniff(iface="MediaTek Wi-Fi 6 MT7921 Wireless LAN Card", store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        destination_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        print(f"[*] Source IP: {source_ip} --> Destination IP: {destination_ip} Protocol: {protocol}")

        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"[*] Payload: {payload}")

interface = "MediaTek Wi-Fi 6 MT7921 Wireless LAN Card"  # Change this to your Wi-Fi interface name
sniff_packets(interface)