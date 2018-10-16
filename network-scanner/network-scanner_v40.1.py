#!/usr/bin/env python3.5
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import scapy.all as scapy


def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_request_packet, timeout=60, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


scan_result = scan("192.168.1.0/24")
print_result(scan_result)
# scan("10.0.2.0/24")
# scan("10.30.1.0/24")
