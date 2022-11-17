
#Bob's RSA-setup
P = 23
Q = 19
A = 61

N = P * Q
B = 13

#Alice's RSA-setup 
P_A = 17
Q_A = 43
A_A = 19

N_A = P_A * Q_A
B_A = 283

def rsa_encrypt(m, e, n):
    return m**e % n

def rsa_decrypt(c, d, n):
    return c**d % n

def known_msg_attack(msg_sign1, msg_sign2, n):
    return msg_sign1[0] * msg_sign2[0] % n, msg_sign1[1] * msg_sign2[1] % n 

msg_sign1 = (78, 394)
msg_sign2 = (123, 289)
print(f"Task a\nMessage 1: msg = {msg_sign1[0]}, signature = {msg_sign1[1]}, calculated msg = {rsa_encrypt(msg_sign1[1], B, N)}")
print(f"Message 2: msg = {msg_sign2[0]}, signature = {msg_sign2[1]}, calculated msg = {rsa_encrypt(msg_sign2[1], B, N)}")
print("Seeing as the signatures match the messages, we can assume these messages are authentic.")

print("\nTask b")
msg = 55
false_sign = rsa_decrypt(msg, A, N)
print(f"False msg_sign = ({msg}, {false_sign})\nValid: {msg == rsa_encrypt(false_sign, B, N)}")

print("\nTask c")
msg_sign1 = (38, 171)
msg_sign2 = (97, 337)
false_msg_sign = known_msg_attack(msg_sign1, msg_sign2, N)
print(f"False msg_sign = {false_msg_sign}\nValid: {false_msg_sign[0] == rsa_encrypt(false_msg_sign[1], B, N)}")

print("\nTask d")
msg = 109
sign = rsa_decrypt(msg, A_A, N_A)

msg_encrypted = rsa_encrypt(msg, B, N)
sign_encrypted = rsa_encrypt(sign, B, N)

msg_sign = msg_encrypted, sign_encrypted
print(msg_sign)
