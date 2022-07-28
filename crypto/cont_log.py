import math
import sys
import os

if __name__ == "__main__":
    try:
        h = float(sys.argv[1])
        g = float(sys.argv[2])
        print(math.log(h, g))
    except:
        print("ERROR")
