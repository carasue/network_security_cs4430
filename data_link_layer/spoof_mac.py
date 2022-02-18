import sys                                                                                                         
import os

def generate_ICMP():
    stream = os.popen("ping -c 4 defender")
    try:
        ping_output_lines = stream.readlines()
        ping_result_line = ping_output_lines[-2]
        if "4 received" not in ping_result_line:
            raise RuntimeError("Error: failed to ping defender")
        else:
            print(
    """
    Got ICMP-reply to ICMP-echo - 1
    Got ICMP-reply to ICMP-echo - 2
    Got ICMP-reply to ICMP-echo - 3
    Got ICMP-reply to ICMP-echo - 4
    """
                    )
    except Exception as e:
        print("Error: failed to ping defender")
        

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Invalid arguments")
        exit(1)


    interface_name = sys.argv[1]
    mac_address = sys.argv[2]

    # 1. Turn off network card.
    os.system("ip link set dev {} down".format(interface_name))
    # 2. replace the old MAC address with specified one.
    os.system("ip link set dev {} address {}".format(interface_name, mac_address))
    # 3. Turn on network card again.
    os.system("ip link set dev {} up".format(interface_name))
    # 4. Ping the defender, generate ICMP echoes towards IP address 192.168.124.20
    generate_ICMP()  
