
P = 0b1000011101101011
Q = 0b1000000000001111
N = P*Q
E = 3
PHI = (P-1)*(Q-1)

def extended_euclidean(a, n):
    t, new_t = 0, 1
    r, new_r = n, a
    
    while new_r > 0:
        quotient = r // new_r
        t, new_t = new_t, (t - quotient*new_t)
        r, new_r = new_r, (r - quotient*new_r)
    
    if r > 1: return "a is not invertible"
    if t < 0: return (t + n)
    return t

D = extended_euclidean(E, PHI)

def e(m, e, n):
    return square_and_multiply(m, e, n)

def d(c, d, n):
    return square_and_multiply(c, d, n)

def square_and_multiply(x: int, y: int, n: int):
    z = 1
    for i in range(len(bin(y)) - 1, -1, -1):
        z = z ** 2 % n
        if ((y >> i) & 1) == 1:
            z = (z * x) % n
    return z

print("b)\nKriterier for valg av p og q:\nJeg valgte 16-bit p og q, passet på at (p-1) og (q-1) ikke bare hadde lave faktorer, og valgte to verdier\njeg håper ikke er for nærme hverandre, samt tilfeldige nok")

print(f"\nc)\nOffentlig nøkkel: (n = {N}, e = {E})")

D = extended_euclidean(E, PHI)
print(f"\nd)\nPrivat nøkkel: (p, q) = ({P}, {Q}), d = {D}")

msg = 12345
c = e(msg, E, N)
print(f"\ne)\nE({msg}) -> {c}")
m = d(c, D, N)
print(f"D({c}) -> {m}")
