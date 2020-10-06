import random


def rand(a, b):
    x = random.randint(a, b)
    return x


def input_validate(name):
    check = 0
    while check == 0:
        print(name, end=' = ')
        x = int(input())
        if x > 0:
            check = 1
        else:
            print(name, " має бути > 0")
    return x


def create_rand_array():
    check = 0
    print("Введіть межі a і b")
    while check == 0:
        a = int(input("a = "))
        b = int(input("b = "))
        if a < b:
            check = 1
        else:
            print("b має бути більше за a!")

    arr = []

    N = input_validate("N")

    check = 0
    while check <= N:
        x = rand(a, b)
        if x != 0:
            arr.append(x)
            check += 1
    return arr


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
    return array


def num_elem_in_array(arr, sign):
    if sign < 0:
        z = 0
        num_elem = 0
        while z < len(arr):
            if arr[z] < 0:
                num_elem += 1
            z += 1
    else:
        z = 0
        num_elem = 0
        while z < len(arr):
            if arr[z] > 0:
                num_elem += 1
            z += 1

    return num_elem


def num_to_begin(arr, x):
    num_elem = num_elem_in_array(arr, x)
    check = len(arr) - 1
    x = num_elem - 1
    if x == 0:
        while x > 0:
            if arr[check] < 0 and arr[check - y] < 0:
                swap(arr, check, check - y)
                y = 1
                check -= 1
                x -= 1

            elif arr[check] < 0 and arr[check - y] > 0:
                y += 1

            elif arr[check] > 0 and arr[check - y] < 0:
                y = 1
                check -= 1

            elif arr[check] > 0 and arr[check - y] > 0:
                y += 1
                check -= 1
    return arr


def info(arr, x, check, y):
    print(arr)
    print("X = ", x)
    print("Last = ", arr[check])
    print("Change = ", arr[check - y])


def slide_one_time(arr, x, check, y, sign):
    if arr[check] < 0 and arr[check - y] < 0:
        if sign < 0:
            swap(arr, check, check - y)
            y = 1
            check -= 1
            x -= 1
        else:
            y += 1
            check -= 1
    elif arr[check] < 0 and arr[check - y] > 0:
        if sign < 0:
            y += 1
        else:
            y = 1
            check -= 1
    elif arr[check] > 0 and arr[check - y] < 0:
        if sign < 0:
            y = 1
            check -= 1
        else:
            y += 1
    elif arr[check] > 0 and arr[check - y] > 0:
        if sign < 0:
            y += 1
            check -= 1
        else:
            swap(arr, check, check - y)
            y = 1
            check -= 1
            x -= 1
    return arr, x, check, y


def move_minus(arr, k):
    y = 1
    stop = 0
    while stop < k:
        num_elem = num_elem_in_array(arr, -1)
        check = len(arr) - 1
        x = num_elem - 1
        while x > 0:
            arr, x, check, y = slide_one_time(arr, x, check, y, -1)
        stop += 1
    print("Масив із зміщеними на k позицій відємними числами масиву")
    print(arr)
    return arr


def move_plus(arr):
    num_plus_elem = num_elem_in_array(arr, 1)
    stop = num_plus_elem - 1
    y = 1
    while stop > 0:
        check = len(arr) - 1
        x = num_plus_elem - 1
        y = 1
        while x > 0:
            arr, x, check, y = slide_one_time(arr, x, check, y, 1)
        num_plus_elem -= 1
        stop -= 1
    print("Масив із записаними в реверсному порядку додатніми числами")
    print(arr)
    return arr


array = create_rand_array()
print("Початковий масив")
print(array)

k = input_validate("k")
move_minus(array, k)
move_plus(array)
