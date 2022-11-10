K = 0b1001
IPAD = 0b0011
OPAD = 0b0101

def h(x):
    return ((x*x % 2**8) & 0b00111100) >> 2

def hmac(K, x):
    res = h((K ^ OPAD)<<8 | h((K ^ IPAD)<<8 | x))
    return bin(res)

msg = 0b0110
res = hmac(K, msg)
print(f"Task a:\nHMAC: {res}")

msg_recieved = 0b0111
res2 = hmac(K, msg_recieved)
print(f"\nTask b:\nRecieved HMAC: {bin(msg_recieved)}\nCalculated HMAC: {res2}")
print("\nAt HMAC er ulike tyder på at avsenderen av meldingen ikke har samme hashfunksjon som oss.\nDette tyder på at meldingen ikke er autentisk.")
