import math

def pollard(n, b):
    if n%2 != 0: a = 2
    g = a**(math.factorial(b))%n
    f = math.gcd(g-1, n)
    if f > 1 :
        return f
    else:
        return None
    
def pollard_unknown_b(n, b_max):
    if n%2 != 0: a = 2
    for i in range(1, b_max + 1):
        g = a**(math.factorial(i))%n
        f = math.gcd(g-1, n)
        if f > 1 :
            return f, i
        else:
            continue
    return None, None

n = 1829
b = 5
print(f"a)\nPollard utført med n = {n} og B = {b}\nFunnet primfaktor: {pollard(n, b)}")

print(f"\nb)\nUt ifra det jeg kan finne fra ressurser på nett, fungerer Pollard-angrep hvis:\n1) (p-1) deler B!\n2) (q-1) har en primfaktor > B\n3) Primfaktorene til (p-1) er < B")
print("\nFaktorer til 18779: {89, 211}\nFaktorer til (p-1) = 210 = {2, 3, 5, 7}\nFaktorer til (q-1) = 88 = {2, 11}")
print("Vi kan derfor anta at B = 8 vil fungere, da dette oppfyller alle kravene.")

print("\nFaktorer til 42583: {97, 439}\nFaktorer til (p-1) = 96 = {2, 3}\nFaktorer til (q-1) = 438 = {2, 3, 73}")
print("Vi kan derfor anta at B = 8 vil fungere, da dette oppfyller alle kravene.")

n = 6319
b_max = 10
found_prime, b =  pollard_unknown_b(n, b_max)
print(f"\nc)\nPollard utført med n = {n} og B = [1, {b_max}]\nFunnet primfaktor: {found_prime} med B = {b}")
