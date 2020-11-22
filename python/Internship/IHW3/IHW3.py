"""
Завдання повинно бути виконано з мінімальною кількістю операцій та з використанням функцій.
Передбачити можливість 2 варіанти введення масивів:
ввести кількість елементів та згенерувати рандомні елементи,
або ввести сам масив. Користувач має мати право вибирати безліч разів один чи інший варіант


Задано масив цілих чисел розмірності .
Здійснити циклічний зсув його від’ємних
елементів на k позицій вправо. Додатні елементи масиву записати в оберненому порядку.
Наприклад, -2 5 6 -3 -4 3 -1. k = 2 Результат: -4 3 6 -1 -2 5 -3.
"""
import Class


def menu_start():
    linked_list = Class.LinkedList()
    print("0 - Написати масив в ручну")
    print("1 - Згенерувати випадково")
    print("2 - Вийти")
    choose = input()
    choose = str(choose)
    return linked_list, choose


def menu_rand(linked_list):
    Class.LinkedList.create_random_list(linked_list)
    output(linked_list)


def menu_manual(linked_list):
    print("Введіть кількість елементів")
    check = 0
    n = 0
    while check == 0:
        n = int(input("N = "))
        if n > 0:
            check = 1
        else:
            print("N має бути > 0")
    check = 0
    while check < n:
        print(check + 1, "Element = ", end=" ")
        new = input()
        new = int(new)
        Class.LinkedList.add_to_end(linked_list, new)
        check += 1
    output(linked_list)


def output(linked_list):
    print("Введіть зсув на k елементів")
    check = 0
    k = 0
    while check == 0:
        k = int(input("K = "))
        if k > 0:
            check = 1
        else:
            print("K має бути > 0")
    print("Початковий масив")
    Class.LinkedList.list_print(linked_list)
    Class.LinkedList.move_elements(linked_list, -1, k)
    print("Масив із зміщеними відємними елементами")
    Class.LinkedList.list_print(linked_list)
    Class.LinkedList.move_elements(linked_list, 1, k)
    print("Масив із зміщеними додатніми елементами")
    Class.LinkedList.list_print(linked_list)


check = 0
while check == 0:
    linked_list, choose = menu_start()
    if choose == "0":
        menu_manual(linked_list)
    elif choose == "1":
        menu_rand(linked_list)
    elif choose == "2":
        print("Bye")
        check = 1
    else:
        print("Ivalid key")
    stop = "0"
    if choose != "2":
        while stop == "0":
            print()
            print("0 - Продовжити; інше - Вийти")
            stop = input()
            stop = str(stop)
            if stop != "0":
                check = 1
                print("Bye")





    """
Class.LinkedList.create_random_list(linked_list)
check = 0
k = 0
while check == 0:
    k = int(input("K = "))
    if k > 0:
        check = 1
    else:
        print("N має бути > 0")
Class.LinkedList.list_print(linked_list)
Class.LinkedList.move_elements(linked_list, -1, k)
Class.LinkedList.list_print(linked_list)
Class.LinkedList.move_elements(linked_list, 1, k)
Class.LinkedList.list_print(linked_list)
"""