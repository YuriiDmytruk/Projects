import random


def rand(a, b):
    x = random.randint(a, b)
    return x


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array


def move(array, a):
    if a == len(array) - 1:
        swap(array, a, 0)
        a = 0
    else:
        swap(array, a, a+1)
        a += 1
    return array


a = -10
b = 10

arr = []
N = int(input("N = "))

check = 0
while check <= N:
    x = rand(a, b)
    if x != 0:
      arr.append(x)
      check += 1
print("Початковий масив")
print(arr)

k = int(input("k = "))
k = 2
stop = 0
while stop < k:
    if arr[stop] < 0:
        move(arr, stop)
    stop += 1
print("Масив із зміщенними відємними членами на k позицій вправо")
print(arr)


z = 0
num_plus_elem = 0
while z < len(arr):
    if arr[z] > 0:
        num_plus_elem += 1
    z += 1

stop = num_plus_elem - 1
y = 1
while stop > 0:
    check = len(arr) - 1
    x = num_plus_elem - 1
    while x > 0:
        if arr[check] > 0 and arr[check - y] > 0:
            swap(arr, check, check - y)
            y = 1
            check -= 1
            x -= 1

        elif arr[check] > 0 and arr[check - y] < 0:
            y += 1

        elif arr[check] < 0 and arr[check - y] > 0:
            y = 1
            check -= 1

        elif arr[check] < 0 and arr[check - y] < 0:
            y += 1
            check -= 1
    num_plus_elem -= 1
    stop -= 1

print("Масив із записаними в реверсному порядку додатніми числами")
print(arr)
