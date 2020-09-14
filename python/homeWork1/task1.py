# послідовність простих чисел
def simple_check(x):
    i = 2
    j = 0
    while i ** 2 <= x and j != 1:
        if x % i == 0:
            j = 1
        i += 1
    if j == 0:
        print(x)


print("Введіть кількість простих чисел:")
number = 100
x = 1
while x < number:
    simple_check(x)
    x += 1
# послідовність чисел Мерсенна розмірності n
print("Числа Мерсена до 100")
y = 1


def mersena_check(y):
    i = 1
    j = 0
    while i != y and j != 1:
        if y == (2 ** i) - 1:
            j = 1
        i += 1
    if j == 1:
        print(y)


while y < number:
    mersena_check(y)
    y += 1
