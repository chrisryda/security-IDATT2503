alphabet = " abcdefghijklmnopqrstuvwxyzæøå,."

def e(x):
    return (x+3)%32

def d(x):
    return (x-3)%32

def cbc_encrypt(plain, init_vec):
    cipher = ""
    c_prev = init_vec 
    for i in range(len(plain)):
        p = alphabet.index(plain[i])
        
        c = e(p ^ c_prev)
        cipher += alphabet[c]
        c_prev = c
         
    return cipher

def cbc_decrypt(cipher, init_vec):
    plain = ""
    c_prev = init_vec
    for i in range(len(cipher)):
        c = alphabet.index(cipher[i])
        
        p = d(c) ^ c_prev
        plain += alphabet[p]
        c_prev = c

    return plain

print(cbc_encrypt("aaaaaa", 13))
print(cbc_encrypt("dette er en test", 13))

print(cbc_decrypt("qvxæyy hkgdgk,,oqhdnc", 13))
    