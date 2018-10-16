#!/usr/bin/env python3.5

import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)


scan("192.168.1.0/24")
# scan("10.0.2.0/24")
# scan("10.31.1.0/24")
