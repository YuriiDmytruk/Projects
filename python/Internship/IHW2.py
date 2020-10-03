import random


def rand(a, b):
    x = random.randint(a, b)
    return x


def create_random_array(arr):
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
    while check == 0:
        n = int(input("N = "))
        if n > 0:
            check = 1
        else:
            print("N має бути > 0")

    check = 0
    while check <= n:
        x = rand(a, b)
        if x != 0:
            arr.append(x)
            check += 1
    print("Початковий масив")
    print(arr)
    return arr


def plus_calculate():
    global calculate
    calculate += 1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        left_arr = []
        right_arr = []
        mid_arr = []
        for n in arr:
            plus_calculate()
            if n < q:
                left_arr.append(n)
            elif n > q:
                right_arr.append(n)
            else:
                mid_arr.append(n)

        return quick_sort(left_arr) + mid_arr + quick_sort(right_arr)


def bubble_sort(arr):
    cal = 0
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                cal += 1
        n += 1
    print(cal)


def main(arr, find):
    global calculate
    calculate = 0
    print("Кількість опрацій сортування бульбашкою:")
    bubble_sort(arr)
    print("Кількість опрацій швидким сортуванням:")
    quick_sort(arr)
    print(calculate)

    print("Посортований масив")
    print(arr)

    operations = 0
    right = len(arr) - 1
    left = 0
    middle = right - ((right - left)//2)
    check = 1
    if find == arr[0]:
        middle = 0
    else:
        while check == 1:
            middle = right - ((right - left) // 2)
            operations += 1
            if find < arr[middle]:
                right = middle
            elif find > arr[middle]:
                left = middle
            elif find == arr[middle]:
                check = 0
            if right - left == 1:
                check = 0

    if arr[middle] == find:
        print("Позиція шуканого елемента:", middle)
        print("Кількість оперецій для його виявлення:", operations)
        check = 1
        x = 1
        while check == 1:
            operations += 1
            if arr[middle - x] == find:
                print("Також шуканий елемент знаходиться на позиції:", middle - x)
            else:
                check = 0
            x += 1
        check = 1
        x = 1
        while check == 1:
            operations += 1
            if arr[middle + x] == find:
                print("Також шуканий елемент знаходиться на позиції:", middle + x)
            else:
                check = 0
            x += 1
        print("Кількість операцій з урахуванням пошуку одинакових елементів:", operations)
    else:
        print("Елемента:", find, "не існує в даному масиві")


array = []
create_random_array(array)
k = int(input("k = "))
main(array, k)
