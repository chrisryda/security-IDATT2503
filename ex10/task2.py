def task_a(z_star, n):
    primitive_elements = []
    for i in range(len(z_star)):
        for k in range(1, n):
            val = z_star[i]**k%n
            if val == 1:
                if k == (n-1):
                    primitive_elements.append(z_star[i])
                break
    return primitive_elements

def get_z_star(n):
    z_star = []
    for r_n in range(1, n):
        for i in range(1, n):
            value = (i*r_n)%n
            if (value == 1 and (i*r_n) not in z_star):
                z_star.append(r_n)
    return z_star

print("Task a & c:")
z_star_17 = get_z_star(17)
print(f"Primitive elements in z_star_17: {task_a(z_star_17, 17)}")
    
