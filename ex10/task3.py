P = 19
ALPHA = 13
A = 5
BETA = 14

def elgamal_encrypt(x, k, alpha = ALPHA,  beta = BETA, p = P):
    return (alpha**k % p, x * beta**k % p)

def elgamal_decrypt(y, a = A, p = P):
    return y[1] * pow(y[0] ** a, -1, p) % p

print(f"Task a\nOffentlig nøkkel (p, alpha, beta) = ({P}, {ALPHA}, {BETA})\nPrivat nøkkel (p, alpha, a) = ({P}, {ALPHA}, {A})")

x = 3
k = 6
print(f"\nTask b\nx = {x} kryptert med k = {k} -> {elgamal_encrypt(x, k)}")

y = (12, 11)
print(f"\nTask c\ny = {y} dekryptert med a = {A} -> {elgamal_decrypt(y)}")
