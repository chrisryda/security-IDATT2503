alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def decrypt(k_max, word):
    for k in range(1, k_max+1):
        decrypted = "Decrypted for k={} :".format(k) 
        for i in range(len(word)):
            index = alphabet.index(word[i])
            shifted_index = index + k
            if (shifted_index > 28):
                shifted_index %= 29
            decrypted += alphabet[shifted_index]
        print(decrypted)
        
decrypt(29, "yævfbvbvfråvbv")
    