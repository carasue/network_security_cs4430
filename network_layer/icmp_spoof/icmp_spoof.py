from scapy.all import *
import os
import sys

# python3 icmp_spoof.py 192.168.124.20 192.168.124.10 22
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: wrong arguments")
        exit(1)

    dst_ip = sys.argv[1]
    src_ip = sys.argv[2]
    pk_len = int(sys.argv[3])
    payload = bytes("#"*pk_len, 'utf-8')

    pkg = IP(dst=dst_ip, src=src_ip)/ICMP(type=8)/payload
    send(pkg, count=2)

