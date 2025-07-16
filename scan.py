import scapy.all as scapy
import time

def detect_arp_poisoning():
    print("[*] Détection ARP spoofing...")
    old_mac = None

    while True:
        arp_req = scapy.ARP(pdst="192.168.1.1")  # Remplace par ta passerelle
        answered = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / arp_req, timeout=2, verbose=False)[0]

        for sent, received in answered:
            if old_mac and received.hwsrc != old_mac:
                print("[ALERTE] Changement de MAC détecté ! Possible attaque ARP.")
                return
            old_mac = received.hwsrc
        time.sleep(5)

detect_arp_poisoning()
