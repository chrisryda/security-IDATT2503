def get_header(n):
    str = "{:<8}".format(" ")
    for i in range(1, n):
        str += "{:<8}".format(i)
    str += "\n"
    return str

def get_row(row_num, n):
    str = "{:<8}".format(row_num)
    for i in range(1, n):
        value = (i*row_num)%n
        if (value == 1 and (i*row_num) not in m_inverse):
            m_inverse.append(i*row_num)
        str += "{:<8}".format(value)
    return str

def get_table(n):
    header = get_header(n)
    rows = []
    for i in range(1, n):
        row = get_row(i, n)
        rows.append(row)
    return header, rows

def print_m_inverse():
    str = "Mulitplicative inverses of modulo {}: ".format(N)
    for i in range(len(m_inverse)):
        str += "{} ".format(m_inverse[i])
    print(str)

def task(n):
    m_inverse.clear()
    header, rows = get_table(n)
    print(header)
    for i in range(len(rows)):
        print(rows[i])
        
def brute_force(num, n_mod):
    i = 1
    for i in range(n_mod):
        value = (i*num)%n_mod
        if (value == 1):
            return i

m_inverse =  []
N = 12

print("Task a:\n")
task(N)

print("\nTask b:")
print_m_inverse()

N = 11
print("\nTask c:\n")
task(N)
print_m_inverse()

print("\nTask d:\nMulitplicative inverse of 11 modulo 29: " + str(brute_force(11, 29)))
