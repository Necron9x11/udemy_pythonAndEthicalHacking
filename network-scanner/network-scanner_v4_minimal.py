#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    # create the ARP request frame and display info about it
    arp_packet = scapy.ARP(pdst=ip)

    # create the broadcast frame and display info about it
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # create the ARP request frame by combining the arp packet and the broadcast packet
    arp_request_packet = broadcast_packet/arp_packet

    # make the arp request
    answered_pings, unanswered_pings = scapy.srp(arp_request_packet, timeout=1)

    # print(scapy.srp(arp_request_packet))
    print("answered:\n")
    print(answered_pings.summary())
    print("\n\nunanswered:\n")
    print(unanswered_pings.summary())

scan("192.168.1.0/24")
# scan("10.0.2.0/24")
# scan("10.30.1.0/24")
