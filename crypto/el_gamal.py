import sys

# !python3 el_gamal.py "elGamalEncrypt" 65 3 809 89 "d"  
# !python3 el_gamal.py "elGamalDecrypt" 809 68 345 517
# !python3 el_gamal.py "elGamalEncrypt" 243983405776 173123 999999000001 89990 "hell0"   
# !python3 el_gamal.py "elGamalDecrypt" 999999000001  696969 412938073794 371661402186

def elGamalEncrypt(h, g, n, r, t):
    t = calculate_t_val(t)
    c1 = pow(g, r, n)
    c2 = t * (pow(h, r)) % n
    return c1, c2


def elGamalDecrypt(n, a, c1, c2):
    s = c1 ** a % n
    s_inv = pow(c1, n-a-1, n)
    m = c2 * s_inv % n
    # m = pow(c2, s_inv, n)
    init_bin_m = bin(m).replace("0b", "")
    if len(init_bin_m) % 8 != 0:
        bin_m = init_bin_m.zfill((len(init_bin_m)//8+1)*8)
    msg_chrs = []
    for i in range(0, len(bin_m), 8):
        ascii_ord = int(bin_m[i:i+8], 2)
        ascii_chr = chr(ascii_ord)
        msg_chrs.append(ascii_chr)
    return "".join(msg_chrs)


def calculate_t_val(t):
    char_bin_codes = []
    for char in t:
        char_ascii_code = ord(char)
        char_bin_code = bin(char_ascii_code).replace("0b", "").zfill(8)
        char_bin_codes.append(char_bin_code)
    str_bin_code = "".join(char_bin_codes)
    return int(str_bin_code, 2)

if __name__ == "__main__":
    try: 
        function_name = sys.argv[1]
        if function_name == "elGamalEncrypt":
            h = int(sys.argv[2])
            g = int(sys.argv[3])
            n = int(sys.argv[4])
            r = int(sys.argv[5])
            t = sys.argv[6]
            c1, c2 = elGamalEncrypt(h, g, n, r, t)
            print("{}, {}".format(c1, c2))
        if function_name == "elGamalDecrypt":
            n = int(sys.argv[2])
            a = int(sys.argv[3])
            c1 = int(sys.argv[4])
            c2 = int(sys.argv[5])
            message = elGamalDecrypt(n, a, c1, c2)
            print(message)
    except:
        print("ERROR")

