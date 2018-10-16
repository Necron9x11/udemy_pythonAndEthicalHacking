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


def print_header(header_text, scapy_attribute):
    # Formats and prints the output of the scapy .ls() method.
    # This is basic right now. The plan is to flesh it out with formatting options, etc.

    # print("\n" + scapy.ls(scapy_attribute)) + "\n"

    print("\n")
    scapy.ls(scapy_attribute)
    print("\n")


def scan(ip):
    # create the ARP request frame
    arp_request = scapy.ARP(pdst=ip)

    # alternate method of setting scapy object values
    # arp_request.pdst=ip

    # print a summary of the ARP request frame we are creating
    print_summary("scapy.ARP() Request summary (arp_request):", arp_request)

    # list all possible fields we can set for scapy.ARP()
    print_header("scapy.ARP() fields:", scapy.ARP())

    # create the broadcast frame
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # alternate method of setting scapy object values
    # broadcast.dst = "ff:ff:ff:ff:ff:ff"

    # print summary of the broadcast frame we are creating
    print_summary("scapy.Ether() Request summary (broadcast):", broadcast)

    # list all possible fields we can set for scapy.Ether()
    print_header("scapy.Ether() fields:", scapy.Ether)



scan("192.168.1.0/24")
# scan("10.0.2.0/24")
# scan("10.30.1.0/24")
