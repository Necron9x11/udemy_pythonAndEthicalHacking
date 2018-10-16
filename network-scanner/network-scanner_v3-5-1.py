#!/usr/bin/env python

# CREATE a 'details' function that will print detail/summary info using scapy's .show, .summary and .ls methods to
#  display info on the request frames/packets being generated. Use a CLI switch or switches that take multiple arguments
#  to define the info request by frame/packet type and detail depth for each. Allow for mixed detail levels between
#  frame/packet types.

import scapy.all as scapy


def print_summary(summary_text, scapy_object):
    # Formats and prints the output of the scapy .summary() method.
    # This is basic right now. The plan is to flesh it out with formatting options, etc.

    print("\n" + summary_text + "\n" + scapy_object.summary())


def print_fields_header(header_text, scapy_attribute):
    # Formats and prints the output of the scapy .ls() method.
    # This is basic right now. The plan is to flesh it out with formatting options, etc.

    # print("arp_packet = " + str(scapy_attribute))
    # print("\n" + scapy.ls(str(scapy_attribute))) + "\n"

    print("\n")
    scapy.ls(scapy_attribute)
    print("\n")


def scan(ip):
    # create the ARP request frame and display info about it
    arp_packet = scapy.ARP(pdst=ip)
    print_summary("scapy.ARP() packet summary (arp_packet object):", arp_packet)
    print_fields_header("scapy.ARP() fields:", arp_packet)

    # create the broadcast frame and display info about it
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    print_summary("scapy.Ether() packet summary (broadcast_packet object):", broadcast_packet)
    print_fields_header("scapy.Ether() fields:", broadcast_packet)

    # create the ARP request frame by combining the arp packet and the broadcast packet
    arp_request_packet = broadcast_packet/arp_packet
    # print_summary("")
    print("\nArp request frame (apr_request object):\n" + arp_request_packet.summary() + "\n")
    scapy.ls(arp_request_packet)

scan("192.168.1.0/24")
# scan("10.0.2.0/24")
# scan("10.30.1.0/24")
