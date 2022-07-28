from scapy.all import *
import base64

def extract_payload(pkt):
    payload = pkt[IP][ICMP].payload.load
    base64_bytes_msg = payload
    bytes_msg = base64.b64decode(base64_bytes_msg)
    msg = bytes_msg.decode('ascii')
    print(msg)


if __name__ == '__main__':

    while True:
        sniffed_pkts = sniff(filter="icmp", prn=extract_payload)

