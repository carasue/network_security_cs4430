import socket
from scapy.all import *
import base64
import os
import sys


if __name__ == '__main__':
    dst_ip = sys.argv[1]
    msg = sys.argv[2]

    bytes_msg = msg.encode('ascii')
    base64_bytes_msg = base64.b64encode(bytes_msg)
    payload = base64_bytes_msg
    pkg = IP(dst=dst_ip)/ICMP(type=15)/payload
    send(pkg)
    exit(0)
