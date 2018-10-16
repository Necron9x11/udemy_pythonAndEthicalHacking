#!/usr/bin/env python3.5

import scapy.all as scapy


def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_request_packet, timeout=1)[0]

    # print(answered_list.summary())

    for element in answered_list:
        print(element[1].psrc)
        print(element[1].hwsrc)

        print("------------------------------")

scan("192.168.1.0/24")
# scan("10.0.2.0/24")
# scan("10.30.1.0/24")
