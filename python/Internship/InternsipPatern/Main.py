import List
import Strategy
import Validator


def check_strategy(func):
    def wraper(main_list, context, full):
        if context == 0:
            print("First you should choose strategy")
        elif full == 0:
            print("First you should choose option 3 too full list")
        else:
            main_list = func(main_list)
        return main_list
    return wraper


def start_menu():
    Strategy.text_start()
    print("1 - Strategy 1 (Iterator)")
    print("2 - Strategy 2 (Read From File)")
    print("3 - Generation")
    print("4 - Delete in Position")
    print("5 - Delete in Range")
    print("6 - Sort")
    print("7 - Print")
    print("8 - Exit")
    choose = input()
    return choose


def menu3(main_list, context):
    if context != 0:
        print("Start Generation")
        Strategy.Context.full_list(context, main_list)
    else:
        print("Choose Strategy")
    return main_list


@check_strategy
def menu4(main_list):
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
    return main_list


@check_strategy
def menu5(main_list):
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
    return main_list


@check_strategy
def menu6(main_list):
    List.LinkedList.sort(main_list)
    return main_list


def menu7(main_list):
    List.LinkedList.list_print(main_list)


def main_menu():
    main_list = List.LinkedList()
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
                menu3(main_list, context)
        elif choose == "4":
            menu4(main_list, context, full)
        elif choose == "5":
            menu5(main_list, context, full)
        elif choose == "6":
            menu6(main_list, context, full)
        elif choose == "7":
            menu7(main_list)
        elif choose == "8":
            check = 0
            print("Bye")
        else:
            print("Wrong Key")


main_menu()
