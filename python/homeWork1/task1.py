def check(x): #перевірка на просте число і якщо так то -> перевірка на марсена
    i = 2
    j = 0
    while i ** 2 <= x and j != 1:
        if x % i == 0:
            j = 1
        i += 1
    if j == 0:
        mersena_check(x)
def mersena_check(y): #перевірка на марсена і виведення числа
    i = 1
    j = 0
    while i != y and j != 1:
        if y == (2 ** i) - 1:
            j = 1
        i += 1
    if j == 1:
        print(y)

number = 100# Кількість чисел які перевіряються
x = 1
while x < number: # Перебір усіх чисел до number
    check(x)
    x += 1





