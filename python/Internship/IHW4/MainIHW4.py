import iter
import random
import List


def rand(a, b):
    stop = 1
    while stop == 1:
        x = random.randint(a, b)
        if x > 0:
            return x


def generator(number, val):
   while number > 0:
       number -= 1
       yield val


def create_random_list(number, a, b, list):
    check = 0
    while check < number:
        value = rand(a, b)
        gen_iter = generator(number, value)
        element = next(gen_iter)
        List.LinkedList.add_to_end(list, element)
        check += 1
    return list


def validate_input_date():
    N, a, b = 0, 0, 0
    print("Веведіть кількість ПАР чисел:")
    stop = 0
    while stop == 0:
        N = int(input("N = "))
        if N > 0:
            stop = 1
        else:
            print("N має бути > 0")

    check = 0
    print("Введіть межі a і b")
    while check == 0:
        a = int(input("a = "))
        b = int(input("b = "))
        if a < b:
            check = 1
        else:
            print("b має бути більше за a!")
    return N, a, b


def validate_value():
    stop = 1
    while stop == 1:
        value = input("Value =")
        value = int(value)
        if value > 0:
            stop = 0
            return value
        else:
            print("Число має бути більше 0")


def create_list(number, list):
    check = 0
    while check < number:
        value = validate_value()
        gen_iter = generator(number, value)
        element = next(gen_iter)
        List.LinkedList.add_to_end(list, element)
        check += 1
    return list


def GCD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    x = a + b
    return x


def main(list):
    List.LinkedList.list_print(list)
    iterator = iter.Iterator(list)
    check = 0
    for i in iterator:
        if check == 0:
            x = i
            check = 1
        elif check == 1:
            y = i
            print(x, y)
            check = 0
            z = GCD(x, y)
            print("GCD", x, ",", y, "=", z)
        else:
            print("Eror")


def menu():
    stop = 1
    while stop == 1:
        main_list = List.LinkedList()
        List.LinkedList.add_to_end(main_list, 0)
        print("1 - Згенерувати список випадково")
        print("2 - Ввести значення вручну")
        print("3 - Вийти з програми")
        choose = input()
        choose = str(choose)
        if choose == '1':
            N, a, b = validate_input_date()
            main_list = create_random_list(N * 2, a, b, main_list)
            main(main_list)
        elif choose == '2':
            print("Веведіть кількість ПАР чисел:")
            check = 0
            while check == 0:
                N = int(input("N = "))
                if N > 0:
                    check = 1
                else:
                    print("N має бути > 0")
            main_list = create_list(N * 2, main_list)
            main(main_list)
        elif choose == '3':
            stop = 0
            print("Bye")
        else:
            print("Неправильно введений пункт меню")


menu()