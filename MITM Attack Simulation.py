from scapy.all import sniff, IP, TCP

def packet_sniffer(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        print(f"Captured Packet: {packet[IP].src} -> {packet[IP].dst}")
        print(f"Payload: {bytes(packet[TCP].payload)}")

# Uncomment to sniff packets in a live environment
# sniff(filter="tcp", prn=packet_sniffer, count=5)
print("MITM Simulation: Uncomment sniff() call to run the test.")
