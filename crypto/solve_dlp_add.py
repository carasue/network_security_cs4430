import sys

if __name__ == "__main__":
    try:
        h = int(sys.argv[1])
        g = int(sys.argv[2])
        n = int(sys.argv[3])
        the_sum = 0
        for i in range(n):
            the_sum += g
            if the_sum % n == h:
                print(i+1)
    except:
        print("ERROR")



