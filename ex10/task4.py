from math import sqrt, ceil

P = 41
ALPHA = 6
BETA = 3

def shanks_algorithm(p = P, alpha = ALPHA, beta = BETA):
    m = ceil(sqrt(p))
    dict = {}
    for j in range(m - 1):
        val = alpha**(m*j) % p 
        dict[val] = j
    for i in range(m - 1):
        val = beta * pow(alpha, -i, p) % p
        if val in dict:
            return m, dict[val], i 
    return dict

m, j, i = shanks_algorithm()
print(f"(m, j, i) = ({m}, {j}, {i})\na = m * j + i = {m * j + i}")
