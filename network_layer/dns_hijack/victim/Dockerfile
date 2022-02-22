FROM ubuntu:20.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python3 dnsutils net-tools

COPY application.py /opt/application.py
RUN chmod +x /opt/application.py
