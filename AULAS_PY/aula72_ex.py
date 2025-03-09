def multiplica(*args):
    tot = 1
    
    for arg in args:
        tot *= arg
    
    return tot

num = multiplica(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(num)

def e_par(num):
    return num % 2 == 0

par = e_par(num)
print(f"O número {num} é {"par" if par else "impar"}")