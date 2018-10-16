#!/usr/bin/env python

# CREATE a 'details' function that will print detail/summary info using scapy's .show, .summary and .ls methods to
#  display info on the request frames/packets being generated. Use a CLI switch or switches that take multiple arguments
#  to define the info request by frame/packet type and detail depth for each. Allow for mixed detail levels between
#  frame/packet types.

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)

    # alternate method of setting scapy object values.
    # arp_request.pdst=ip

    print("\nscapy.ARP() Request summary (arp_request):\n" + arp_request.summary())

    # list all possible fields we can set for scapy.ARP()
    print("\nscapy.ARP() fields:")
    scapy.ls(scapy.ARP())
    #print("\n")

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # alternate method of setting scapy object values.
    # broadcast.dst = "ff:ff:ff:ff:ff:ff"

    print("\nscapy.Ether() Request summary (broadcast):\n" + broadcast.summary())

    # list all possible fields we can set for scapy.Ether()
    print("\nscapy.Ether() fields:")
    scapy.ls(scapy.Ether())
    print("\n")


scan("192.168.1.0/24")
# scan("10.0.2.0/24")
# scan("10.30.1.0/24")
