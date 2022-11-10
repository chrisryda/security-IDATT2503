import math

def rsa_attack(n):
    t = math.ceil(math.sqrt(n))
    while True:
        k = t**2 - n
        if k > 0:
            s = math.sqrt(k)
            if s**2 + n == t**2:
                return t+s, t-s
        t += 1

p, q = rsa_attack(152416580095517)        
print(f"p = {int(p)}, q = {int(q)}")
    