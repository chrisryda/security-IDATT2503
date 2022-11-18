
def task_a(x_max):
    for x in range(1, x_max + 1):
        for i in range(1, x_max):
            value = x**i
            if value == 1:
                return x, i

def task_b(z_star, n):
    order_of_elements = []
    for i in range(len(z_star)):
        for k in range(1, n):
            val = z_star[i]**k%n
            if val == 1 and (n-1)%k == 0:
                order_of_elements.append((z_star[i], k))
                break
    return order_of_elements

def get_z_star(n):
    z_star = []
    for r_n in range(1, n):
        for i in range(1, n):
            value = (i*r_n)%n
            if (value == 1 and (i*r_n) not in z_star):
                z_star.append(r_n)
    return z_star

def task_c(n):
    header, rows = get_table(n)
    print(header)
    for i in range(len(rows)):
        print(rows[i])

def get_table(n):
    header = get_header(n)
    rows = []
    for i in range(2, n):
        row = get_row(i, n)
        rows.append(row)
    return header, rows

def get_header(n):
    str = "{:<8}".format(" ")
    for i in range(1, n):
        str += "{:<8}".format(i)
    str += "\n"
    return str

def get_row(row_num, n):
    str = "{:<8}".format(row_num)
    for i in range(1, n):
        value = row_num**i%n
        if value == i:
            str += "{:<8}".format(value)
        else:
            str += "{:<8}".format("-")
    return str

print("Task a:")
x, i = task_a(10)
print(f"x^i = 1 when x = {x} and i = {i}")

print("\nTask b:")
z_star_11 = get_z_star(11)
print(f"z_star_11: {z_star_11}")
print(f"Order of z_star_11: {len(z_star_11)}")
print(f"Order of each element in z_star_11: {task_b(z_star_11, 11)}")
print("Fermat's little theorem, which says the order of all elements shoulde divide (11-1), is confirmed on line 14")

print("\nTask c:")
task_c(11)
