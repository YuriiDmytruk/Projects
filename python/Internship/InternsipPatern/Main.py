import List
import Strategy
import Validator
import Observer
import threading

def create_list():
    list = List.LinkedList()
    observer = Observer.Observer()
    add = Observer.EventAdd()
    observer.attach(add)
    remove = Observer.EventRemove()
    observer.attach(remove)
    arr = []
    arr.append(list)
    arr.append(observer)
    return arr


def on_start():
    Strategy.text_start()
    check = 1
    context = 0
    full = 0
    return check, context, full


def delete(list, id, check, observer):
    print("Thread:", check, "Start")
    if 0 < id < List.LinkedList.return_len(list):
        List.LinkedList.delete_element(list, id)
        copy = List.LinkedList.copy_list(list)
        Observer.Observer.notify(observer, "Remove", copy)
    else:
        print("Element with this Id not exist")
    print("Thread:", check, "End")
    return list


def check_strategy(func):
    def wraper(main_list, context, full, observer):
        if context == 0:
            print("First you should choose strategy")
        elif full == 0:
            print("First you should choose option 3 too full list")
        else:
            main_list = func(main_list, observer)
        return main_list
    return wraper


def start_menu():
    print("1 - Strategy 1 (Iterator)")
    print("2 - Strategy 2 (Read From File)")
    print("3 - Generation")
    print("4 - Delete in Position")
    print("5 - Delete in Range")
    print("6 - Sort")
    print("7 - Print")
    print("10 - Create new list")
    print("11 - Set list")
    print("12 - Delete by position in all lists")
    print("13 - Print All")
    print("14 - Exit")
    choose = input()
    return choose


def menu3(main_list, context, observer):
    if context != 0:
        print("Start Generation")
        Strategy.Context.full_list(context, main_list)
        copy = List.LinkedList.copy_list(main_list)
        Observer.Observer.notify(observer, "Add", copy)
    else:
        print("Choose Strategy")
    return main_list, observer


@check_strategy
def menu4(main_list, observer):
    i_d = None
    while i_d is None:
        print("Input id:", end=" ")
        i_d = input()
        z = Validator.Validator(i_d)
        z = Validator.Validator.check_number(z)
        if z is not None and int(z) > 0:
            i_d = int(i_d)
        else:
            print("Value should be integer")
    List.LinkedList.delete_element(main_list, i_d)
    copy = List.LinkedList.copy_list(main_list)
    Observer.Observer.notify(observer, "Remove", copy)
    return main_list


@check_strategy
def menu5(main_list, observer):
    start = None
    stop = None
    check = 0
    while check == 0:
        start = None
        stop = None
        while start is None:
            print("Input start id:", end=" ")
            start = input()
            z = Validator.Validator(start)
            z = Validator.Validator.check_number(z)
            if z is not None and int(z) >= 0:
                start = int(start)
            else:
                start = None
                print("Value should be integer")
        while stop is None:
            print("Input stop id:", end=" ")
            stop = input()
            z = Validator.Validator(stop)
            z = Validator.Validator.check_number(z)
            if z is not None and int(z) > 0:
                stop = int(stop)
            else:
                stop = None
                print("Value should be integer")
        if start < stop:
            check = 1
        else:
            print("Stop must be > start")
    main_list = List.LinkedList.delete_in_range(main_list, start, stop)
    copy = List.LinkedList.copy_list(main_list)
    Observer.Observer.notify(observer, "Remove", copy)
    return main_list


@check_strategy
def menu6(main_list, observer):
    List.LinkedList.sort(main_list)
    return main_list, observer


def menu7(main_list):
    List.LinkedList.list_print(main_list)


def menu10(arr_list):
    arr = create_list()
    arr_list.append(arr)
    return arr_list


def menu11(arr_list, index):
    print("Curent list : ", end=" ")
    List.LinkedList.list_print(arr_list[index][0])
    check = 0
    print("Your Lists:")
    while check < len(arr_list):
        print(check, " : ", end=" ")
        List.LinkedList.list_print(arr_list[check][0])
        check += 1
    print("Insert id:", end=" ")
    index = input()
    index = int(index)
    return index


def menu12(arr_list):
    i_d = None
    while i_d is None:
        print("Input id:", end=" ")
        i_d = input()
        z = Validator.Validator(i_d)
        z = Validator.Validator.check_number(z)
        if z is not None and int(z) > 0:
            i_d = int(i_d)
        else:
            print("Value should be integer")

    check = 0
    while check < len(arr_list):
        threading.Thread(target=delete, args=[arr_list[check][0], i_d, check, arr_list[check][1]]).start()
        check += 1
    return arr_list


def menu13(arr_list):
    check = 0
    while check < len(arr_list):
        List.LinkedList.list_print(arr_list[check][0])
        check += 1


def main_menu():
    check, context, full = on_start()
    arr_list = []
    arr_list.append(create_list())
    list_index = 0
    while check == 1:
        main_list = arr_list[list_index][0]
        observer = arr_list[list_index][1]
        choose = start_menu()
        if choose == "1":
            context = Strategy.Context(Strategy.ConcreteStrategyA())
        elif choose == "2":
            context = Strategy.Context(Strategy.ConcreteStrategyB())
        elif choose == "3":
            if context != 0:
                full = 1
                main_list = menu3(main_list, context, observer)
        elif choose == "4":
            main_list = menu4(main_list, context, full, observer)
        elif choose == "5":
            main_list = menu5(main_list, context, full, observer)
        elif choose == "6":
            main_list = menu6(main_list, context, full, observer)
        elif choose == "7":
            menu7(main_list)
        elif choose == "10":
            arr_list = menu10(arr_list)
        elif choose == "11":
            arr_list[list_index][0] = main_list
            arr_list[list_index][1] = observer
            list_index = menu11(arr_list, list_index)
            main_list = arr_list[list_index][0]
            observer = arr_list[list_index][1]
        elif choose == "12":
            arr_list = menu12(arr_list)
        elif choose == "13":
            menu13(arr_list)
        elif choose == "14":
            check = 0
            print("Bye")
            open("History.txt", "w").close()
        else:
            print("Wrong Key")


main_menu()
