alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def f(x):
    return (11*x - 5)%29

def f_inverse(y):
    return (8*y + 11)%29

def print_conversion():
    original =  "Original:  "
    encrypted = "Encrypted: "
    for i in range(29):
        original += "{:<4}".format(alphabet[i])
        encrypted += "{:<4}".format(alphabet[f(i)])
    
    print(original)
    print(encrypted)
    
def print_inverse():
    inverse =  "Inverse: "
    for i in range(29):
        inverse += "{:<4}".format(f_inverse(i))        
    print(inverse)

def encrypt(word):
    encrypted = ""
    for i in range(len(word)):
        letter_index = alphabet.index(word[i])
        encrypted += alphabet[f(letter_index)]        
    return encrypted

def decrypt(word):
    decrypted = ""
    for i in range(len(word)):
        letter_index = alphabet.index(word[i])
        decrypted += alphabet[f_inverse(letter_index)]
    return decrypted
    
print("Task a:")
print_conversion()

print("\nTask c:")
print_inverse()

print("\nTask d: alice -> " + encrypt("alice"))

print("\nTask e: SIØPBE -> " + decrypt("siøpbe"))
    