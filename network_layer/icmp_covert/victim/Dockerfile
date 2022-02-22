FROM ubuntu:20.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y iproute2 vim iputils-ping iptables tcpdump netcat iptables-persistent python3 python3-pip
COPY rules.v4 /etc/iptables/rules.v4
COPY accept-rules.v4 /etc/iptables/accept-rules.v4
