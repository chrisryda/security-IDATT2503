alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def autokey_encrypt(plain, autokey):
    cipher = []
    key = alphabet[autokey] + plain[:-1]
    for i in range(len(plain)):
        index = (alphabet.index(plain[i]) + alphabet.index(key[i]))%29
        cipher.append(index)
        
    return cipher

def autokey_decrypt(cipher, autokey):
    plain = ""
    key = str(alphabet[autokey])
    for i in range(len(cipher)):
        index = (cipher[i] - alphabet.index(key[i]))%29
        letter = alphabet[index]
        key += letter
        plain += letter
        
    return plain
    
print(autokey_encrypt("goddag", 17))
print(autokey_decrypt([23, 8, 23, 12, 21, 2, 4, 3, 17, 13, 19], 5))
