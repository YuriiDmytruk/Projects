import List
import Strategy
import Validator
import Observer


def check_strategy(func):
    def wraper(main_list, context, full, observer):
        if context == 0:
            print("First you should choose strategy")
        elif full == 0:
            print("First you should choose option 3 too full list")
        else:
            main_list, observer = func(main_list, observer)
        return main_list, observer
    return wraper


def start_menu():
    print("1 - Strategy 1 (Iterator)")
    print("2 - Strategy 2 (Read From File)")
    print("3 - Generation")
    print("4 - Delete in Position")
    print("5 - Delete in Range")
    print("6 - Sort")
    print("7 - Print")
    print("8 - Load Last Add")
    print("9 - Load Last Remove")
    print("10 - Exit")
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
    main_list = List.LinkedList.delete_element(main_list, i_d)
    copy = List.LinkedList.copy_list(main_list)
    Observer.Observer.notify(observer, "Remove", copy)
    return main_list, observer


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
    return main_list, observer


@check_strategy
def menu6(main_list, observer):
    List.LinkedList.sort(main_list)
    return main_list, observer


def menu7(main_list):
    List.LinkedList.list_print(main_list)


@check_strategy
def menu8(main_list, observer):
    history = Observer.Observer.return_add(observer)
    if history is not None:
        print("Last Add: ", end="")
        List.LinkedList.list_print(history)
        check = 0
        while check == 0:
            print("Confirm load: 1-Yes; 0-No")
            choose = input()
            if choose == "1":
                main_list = history
                check = 1
            elif choose == "0":
                check = 1
            else:
                print("Wrong key")
    else:
        print("No History Now")
    return main_list, observer


@check_strategy
def menu9(main_list, observer):
    history = Observer.Observer.return_remove(observer)
    if history is not None:
        print("Last Remove: ", end="")
        List.LinkedList.list_print(history)
        check = 0
        while check == 0:
            print("Confirm load: 1-Yes; 0-No")
            choose = input()
            if choose == "1":
                main_list = history
                check = 1
            elif choose == "0":
                check = 1
            else:
                print("Wrong key")
    else:
        print("No History Now")
    return main_list, observer


def main_menu():
    Strategy.text_start()
    main_list = List.LinkedList()
    observer = Observer.Observer()
    add = Observer.EventAdd()
    observer.attach(add)
    remove = Observer.EventRemove()
    observer.attach(remove)
    check = 1
    context = 0
    full = 0
    while check == 1:
        choose = start_menu()
        if choose == "1":
            context = Strategy.Context(Strategy.ConcreteStrategyA())
        elif choose == "2":
            context = Strategy.Context(Strategy.ConcreteStrategyB())
        elif choose == "3":
            if context != 0:
                full = 1
                main_list, observer = menu3(main_list, context, observer)
        elif choose == "4":
            main_list, observer = menu4(main_list, context, full, observer)
        elif choose == "5":
            main_list, observer = menu5(main_list, context, full, observer)
        elif choose == "6":
            main_list = menu6(main_list, context, full, observer)
        elif choose == "7":
            menu7(main_list)
        elif choose == "8":
            main_list, observer = menu8(main_list, context, full, observer)
        elif choose == "9":
            main_list, observer = menu9(main_list, context, full, observer)
        elif choose == "10":
            check = 0
            print("Bye")
        else:
            print("Wrong Key")


main_menu()
