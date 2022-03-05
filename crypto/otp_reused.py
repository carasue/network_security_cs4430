
def from_hex_str_to_msg(hex_str):
    the_l = len(hex_str)
    ascii_chrs = []
    for i in range(0, the_l, 2):
        ascii_ord = int(hex_str[i:i+2], 16)
        ascii_chr = chr(ascii_ord)
        # print("hex_2_c ={}, ascii_ord ={}, ascii_chr ={}".format(hex_str[i:i+2], ascii_ord, ascii_chr))
        ascii_chrs.append(ascii_chr)
    return "".join(ascii_chrs)
        
def from_msg_to_hex_str(msg):
    msg_chrs = []
    for ascii_chr in msg:
        ascii_ord = ord(ascii_chr)
        msg_chr = hex(ascii_ord).replace("0x", "").zfill(2)
        msg_chrs.append(msg_chr)
    return "".join(msg_chrs)

def calculate_another_d_hex_str(c_hex_str_1, c_hex_str_2, d_msg_1):
    d_hex_str_1 = from_msg_to_hex_str(d_msg_1)
    xor_c_hex_str_1_and_2 = xor(c_hex_str_1, c_hex_str_2)
    d_hex_str_2 = xor(xor_c_hex_str_1_and_2, d_hex_str_1)
    return d_hex_str_2


def calculate_key_hex_str(c_hex_str, d_hex_str):
    key_hex_str =  xor(c_hex_str, d_hex_str)
    return key_hex_str

def encrpyt_hex_str(key_hex_str, d_hex_str):
    c_hex_str = xor(key_hex_str, d_hex_str)
    return c_hex_str


def decrypt_hex_str_to_msg(key_hex_str, e_hex_str):
    # print("key_hex_str={},e_hex_str={}".format(key_hex_str, e_hex_str))
    d_hex_str = xor(key_hex_str, e_hex_str)
    d_msg = from_hex_str_to_msg(d_hex_str)
    return d_msg

def xor(hex_str_1, hex_str_2):
    the_l = len(hex_str_1)
    hex_str_chrs = []
    for i in range(0, the_l, 2):
        # print("i={},hex_str_1[i:i+2]={},hex_str_2[i:i+2]={}".format(i, hex_str_1[i:i+2], hex_str_2[i:i+2]))
        ascii_ord_1 = int(hex_str_1[i:i+2], 16)
        ascii_ord_2 = int(hex_str_2[i:i+2], 16)
        ascii_ord_xor = ascii_ord_1  ^ ascii_ord_2 
        hex_str_chr = hex(ascii_ord_xor).replace("0x", "").zfill(2)
        hex_str_chrs.append(hex_str_chr)
    return "".join(hex_str_chrs)
        
def window_crib_the_word(word, hex_str_1, hex_str_2, index_1, index_2):
    l_1 = len(hex_str_1)
    l_2 = len(hex_str_2)
    l_min = l_1 if l_1 < l_2 else l_2
    THE_MSG = word
    THE_L = len(THE_MSG)*2
    i = 0
    d_msg_2_arr = []
    with open("output.txt", "a") as f:
        while i + THE_L <= l_min:
            c_hex_str_1 = hex_str_1[i:i+THE_L]
            c_hex_str_2 = hex_str_2[i:i+THE_L]
            d_hex_str_2 = calculate_another_d_hex_str(c_hex_str_1, c_hex_str_2, THE_MSG)
            d_msg_2 = from_hex_str_to_msg(d_hex_str_2)
            line = "i = {}, index_1 = {}, index_2 = {}, c_hex_str_1 = {}, c_hex_str_2 = {}, d_hex_str_2 = {}, d_msg_2 = {} \n".format(i, index_1, index_2, c_hex_str_1, c_hex_str_2, d_hex_str_2, d_msg_2)
            f.write(line)
            i += 1
    return d_msg_2_arr


"""

# 1. I am using the crib-dragging algorithm, and try the typical " the " word to see if there is any meaningful word when I am crib-dragging the word(use " the " as an decryted piece and extract the same-lenght word of two sentences at the same position, if " the " is the decyoted piece of one of them, then a meaningful word would show up).
# 2. I find i = 18, index_1 = 12, index_2 = 14, c_hex_str_1 = 7425233561, c_hex_str_2 = 7425233561, d_hex_str_2 = 2074686520, d_msg_2 =  the  
# 3. which means that the 5 chars of the sentences starting from 18 whose index=12 and index=14 might be " the "
word = "Geography"
with open("otp_ciphertexts.txt") as f:
    c_lines = f.readlines()
    c_hex_strs = []
    for c_line in c_lines:
        c_hex_str = c_line.replace("\n", "")
        c_hex_strs.append(c_hex_str)
    c_hex_strs_len = len(c_hex_strs)
    for i in range(c_hex_strs_len):
        for j in range(i+1, c_hex_strs_len):
            d_msg_2_arr =  window_crib_the_word(word, c_hex_strs[i], c_hex_strs[j], i, j)

# 4. Then I can crack the piece[20:38] of key by 
key_hex_str = calculate_key_hex_str("252335612729233f2c","746865206361706974")

# 5. Try to get some meaningful word from these two piece of key
with open("otp_ciphertexts.txt") as f:
    c_lines = f.readlines()
    c_hex_strs = []
    for c_line in c_lines:
        c_hex_str = c_line.replace("\n", "")
        c_hex_strs.append(c_hex_str)
    c_hex_strs_len = len(c_hex_strs)
    with open("partial_msg.txt", "a") as output:
        for index, c_hex_str in enumerate(c_hex_strs):
            if len(c_hex_str) < 20+2*len(word):
                continue
            c_hex_str_partial= c_hex_str[20:20 + 2*len(word)]
            msg_partial = decrypt_hex_str_to_msg(key_hex_str, c_hex_str_partial)
            line = "index = {}, for 20-38, msg = {}\n".format(index, msg_partial)
            output.write(line)

# 6. From the output, I see another meaningful words like: times, never, air, does, all, Geog. And I try to extend and do the crib-draggin again with these words, repeating the 1-6

# For example, I extend the "Geog" as "Geography" 
# And I get 

# i = 20, index_1 = 2, index_2 = 13, c_hex_str_1 = 3524353264263c2278, c_hex_str_2 = 162e3f263629233e21, d_hex_str_2 = 646f6573206e6f7420, d_msg_2 = does not  

# i = 20, index_1 = 4, index_2 = 13, c_hex_str_1 = 712a3c2d643b3c242c, c_hex_str_2 = 162e3f263629233e21, d_hex_str_2 = 20616c6c20736f7274, d_msg_2 =  all sort 


# i = 20, index_1 = 5, index_2 = 13, c_hex_str_1 = 396a70322c2d733d36, c_hex_str_2 = 162e3f263629233e21, d_hex_str_2 = 682120736865206b6e, d_msg_2 = h! she kn 

# i = 20, index_1 = 9, index_2 = 13, c_hex_str_1 = 6b6b362e313a732231, c_hex_str_2 = 162e3f263629233e21, d_hex_str_2 = 3a20666f7572207469, d_msg_2 = : four ti 

# i = 20, index_1 = 10, index_2 = 13, c_hex_str_1 = 38263532643b36203d, c_hex_str_2 = 162e3f263629233e21, d_hex_str_2 = 696d65732073657665, d_msg_2 = imes seve 

# i = 20, index_1 = 11, index_2 = 13, c_hex_str_1 = 343d3533642f362278, c_hex_str_2 = 162e3f263629233e21, d_hex_str_2 = 657665722067657420, d_msg_2 = ever get  

# i = 20, index_1 = 12, index_2 = 13, c_hex_str_1 = 25233561093d3f2231, c_hex_str_2 = 162e3f263629233e21, d_hex_str_2 = 746865204d756c7469, d_msg_2 = the Multi 

# i = 20, index_1 = 13, index_2 = 14, c_hex_str_1 = 162e3f263629233e21, c_hex_str_2 = 252335612729233f2c, d_hex_str_2 = 746865206361706974, d_msg_2 = the capit 

# i = 20, index_1 = 13, index_2 = 15, c_hex_str_1 = 162e3f263629233e21, c_hex_str_2 = 226b24292168303728, d_hex_str_2 = 732074686520636170, d_msg_2 = s the cap 


# i = 20, index_1 = 13, index_2 = 16, c_hex_str_1 = 162e3f263629233e21, c_hex_str_2 = 7c6b3f29642c36372a, d_hex_str_2 = 2d206f682064656172, d_msg_2 = - oh dear 

# i = 20, index_1 = 13, index_2 = 19, c_hex_str_1 = 162e3f263629233e21, c_hex_str_2 = 272e7023212d3d763b, d_hex_str_2 = 7665206265656e2063, d_msg_2 = ve been c 

# using these and calculate the key and find the msg in position 20 - 38
"""
"""
index = 0, for 20-38, msg = r?H*¦ÉÚz<
index = 1, for 20-38, msg = ir goes i
index = 2, for 20-38, msg = does not 
index = 3, for 20-38, msg = djso4@7}j
index = 4, for 20-38, msg =  all sort
index = 5, for 20-38, msg = h! she kn
index = 6, for 20-38, msg = she£ÅÐd>x
index = 7, for 20-38, msg = ?eou{;>c
index = 8, for 20-38, msg = 7{dkf%7vd
index = 9, for 20-38, msg = : four ti
index = 10, for 20-38, msg = imes seve
index = 11, for 20-38, msg = ever get 
index = 12, for 20-38, msg = the Multi
index = 13, for 20-38, msg = Geography
index = 14, for 20-38, msg = the capit
index = 15, for 20-38, msg = s the cap
index = 16, for 20-38, msg = - oh dear
index = 19, for 20-38, msg = ve been c
"""
# And further extend these meaningful words , until I got one sentence:  (it is actually from Alice wonderlands after I googled)
# For line 13: 
# e_hex_str: 2f27226a307a203b3f74162e3f263629233e21
# d_msg:let's try Geography
# d_hex_str: 
e_hex_str = "2f27226a307a203b3f74162e3f263629233e21"
d_hex_str = from_msg_to_hex_str("let's try Geography")
# k: 4342564d435a54494654514b50414448535658 (38 long)

# as our msg is (60 long) we need more

# And use this key, we got more longer sentences
# like line 19:
# e_hex_str: 630b7620362920692e35272e7023212d3d763b24332f343126752a3c36780f3c26352023312d63 (78 long)
# d_msg: I must have been changed for Mabel! 
e_hex_str = "630b7620362920692e35272e7023212d3d763b24332f343126752a3c36780f3c26352023312d63"

d_msg = " I must have been changed for Mabel! I'"
d_hex_str = from_msg_to_hex_str(d_msg)
k = calculate_key_hex_str(e_hex_str, d_hex_str)
to_decrypt = "222c326d2535213b662038263532643b3a2e78252161273c2b2738362136"
k = k[:len(to_decrypt)]

msg =  decrypt_hex_str_to_msg(k, to_decrypt)
print(msg)
# Thus I got the answer 
# and four times six is thirteen
