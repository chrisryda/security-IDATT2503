
def e(x):
    return (x + 3)%2**4

def cbc_mac(x):
    IV = 0b0
    y = [IV]
    for i in range(len(x)):
        y.append(e(y[i] ^ x[i]))
    return y[-1]

x = [0b1101, 0b1111, 0b1010, 0b0001]
print(bin(cbc_mac(x)))

x_marked = [0b0010, 0b1100, 0b0001, 0b1111]
print(bin(cbc_mac(x_marked)))