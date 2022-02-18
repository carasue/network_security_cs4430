import os

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
# 3. make eth1, eth2 ports of the new bridge
    os.system("sudo brctl addif {} {}".format(bridge_name, interface_1))
    os.system("sudo brctl addif {} {}".format(bridge_name, interface_2))
# 4. set the new bridge's id with argument
    os.system("sudo ip link set dev {} address {}".format(bridge_name, bridge_id))
# 5. set the new bridge's priority as low as possible
    os.system("sudo brctl setbridgeprio {} {}".format(bridge_name, bridge_priority))




    

    

