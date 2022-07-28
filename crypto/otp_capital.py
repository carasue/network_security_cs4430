import sys
# python3 otp_capital.py "Encrypt me"

if __name__ == '__main__':
    one_time_chars=['B','H','Z','A','P','S','I','E','Z','S','L','A','G','V','C','E','X','L','E','U','F','X','X','X','G','O','F','J','L','D','H','S','O','S','C','O','Q','O','J','G','X','W','W','P','R','Z','X','D','M','M']
    try: 
        one_time_ords = list(map(lambda char: ord(char), one_time_chars))
        input_str = sys.argv[1]
        input_ords = list(map(lambda char: ord(char), input_str))
        cipher_ords = []
        for i in range(len(input_ords)):
            input_ord = input_ords[i]
            one_time_ord = one_time_ords[i]
            cipher_ord = input_ord ^ one_time_ord
            cipher_ords.append(hex(cipher_ord).replace("0x", "").zfill(2))
        print("".join(cipher_ords))
    except:
        print("Error")

        
