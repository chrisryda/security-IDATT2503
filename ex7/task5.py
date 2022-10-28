alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def vigenere(word, key):
    encrypted = "Encrypted: "
    key_len = len(key)
    
    for i in range(len(word)):
        key_index = alphabet.index(key[i%key_len])
        letter_index = alphabet.index(word[i])
        
        index = (key_index + letter_index)%29
        encrypted += alphabet[index].upper()
        
    print("Plain: " + word)
    print(encrypted + "\n")
    
def decrypt(word, key):
    print("Encrypted: " + word)
    decrypted = "Decrypted: "
    key_len = len(key)
    
    for i in range(len(word)):
        key_index = alphabet.index(key[i%key_len])
        letter_index = alphabet.index(word[i])
        
        index = letter_index - key_index
        decrypted += alphabet[index]
        
    print(decrypted)
    
# Task a
vigenere("snarthelg", "torsk")

# Task b
encrypted = "QZQOBVCAFFKSDC"
decrypt(encrypted.lower(), "brus")
