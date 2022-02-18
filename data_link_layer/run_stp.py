
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Error, wrong arguments.")
        exit(1)

#  python3 run_stp.py eth1 eth2 CA:F2:5D:EB:D6:9C 1
    interface_1 = sys.argv[1]
    interface_2 = sys.argv[2]
    bridge_id = sys.argv[3]
    bridge_priority = sys.argv[4]
    bridge_name = "br0"

# 1. create a new bridge
    os.system("sudo brctl addbr {}".format(bridge_name))
# 2. turn on the stp of the new bridge
    os.system("sudo brctl stp {} on".format(bridge_name))
# 3. turn on the network interfaces and bridge
    os.system("sudo ip link set {} up".format(interface_1))
    os.system("sudo ip link set {} up".format(interface_2))
    os.system("sudo ip link set {} up".format("eth0"))
    os.system("sudo ip link set dev {} up".format(bridge_name))
# 4. make eth1, eth2 ports of the new bridge
    os.system("sudo brctl addif {} {}".format(bridge_name, interface_1))
    os.system("sudo brctl addif {} {}".format(bridge_name, interface_2))
    os.system("sudo brctl addif {} {}".format(bridge_name, "eth0"))
# 5. add the interface to bridge by setting its master to the new bridge
    os.system("sudo ip link set {} master {}".format("eth0", bridge_name))
    os.system("sudo ip link set {} master {}".format(interface_1, bridge_name))
    os.system("sudo ip link set {} master {}".format(interface_2, bridge_name))
# 6. set the new bridge's id with argument
    os.system("sudo ip link set dev {} address {}".format(bridge_name, bridge_id))
# 7. set the new bridge's priority as low as possible
    os.system("sudo brctl setbridgeprio {} {}".format(bridge_name, bridge_priority))




    

    

