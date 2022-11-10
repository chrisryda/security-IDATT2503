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
hmac_recieved = 0b0100
res2 = hmac(K, msg_recieved)
print(f"\nTask b:\nRecieved HMAC: {bin(hmac_recieved)}\nCalculated HMAC: {res2}")
print("\nHMAC er riktig, så meldingen kan være autentisk. Mtp at vi har blokklengde 4 er det\nmulighet for kollisjon i hashfunksjonen vår, f.eks. kan meldingen ha vært 0110.")
