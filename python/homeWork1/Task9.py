import random

def rand(a, b):
    x = random.randint(a, b)
    return x

def GCD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    x = a + b
    return x

print("Веведіть кількість ПАР чисел:")
N = int(input("N = "))

check = 0
print("Введіть межі a і b")
while check == 0:
    a = int(input("a = "))
    b = int(input("b = "))
    if a < b:
        check = 1
    else:
        print("b має бути більше за a!")

check = 0
while check < N:
    x = rand(a, b)
    y = rand(a, b)
    z = GCD(x, y)
    print("GCD",x,",",y,"=",z)
    check += 1
