#!/usr/bin/env python3

import datetime
import itertools
import socket
import time


# we start querying at a random number to ensure that this cannot be predicted
domain = f"update-server.updateserver.corp"
while True:
    print(f"{datetime.datetime.now().isoformat()} Querying {domain}")
    try:
        ipaddr = {a[4][0] for a in socket.getaddrinfo(domain, 0, socket.AF_INET)}
        print(f"{datetime.datetime.now().isoformat()} Got answer {ipaddr} for {domain}")
    except Exception as e:
        print(f"{datetime.datetime.now().isoformat()} Got error {e} for {domain}")
    else:
        if "254.123.45.67" not in ipaddr:
            print(f"{datetime.datetime.now().isoformat()} Exploit succeeded!")
            break

    time.sleep(10)
