K = 0b1001
IPAD = 0b0011
OPAD = 0b0101

def h(x):
    return ((x**2)%(2**8))

def hmac(K, x): 
    res = ((h(K ^ OPAD)<<8 | h(K ^ IPAD))<<8 | x)
    return "00" + bin(h(res))[2:]

msg = 0b0110
res = hmac(K, msg)
print(f"Task a:\nFull HMAC: {res}\nCenter 4 digits: {res[2:6]}")

msg_recieved = 0b0111
res2 = hmac(K, msg_recieved)
print(f"\nTask b:\nRecieved HMAC: 0100\nCalculated HMAC: {res2[2:6]}")
print("\nAt HMAC er ulike tyder på at avsenderen av meldingen ikke har samme hashfunksjon som oss.\nDette tyder på at meldingen ikke er autentisk.")
