import List
import Class


def menu_start():
    master_list = List.LinkedList()
    List.LinkedList.read_from_file(master_list)
    List.LinkedList.check_date(master_list)
    print("If you want to ... click:")
    print("1 - Print file")
    print("2 - Add element")
    print("3 - Delete element by id")
    print("3 - Change element")
    print("5 - Search")
    print("6 - Sort")
    choose = input()
    choose = str(choose)
    return master_list, choose


def menu1(master_list):
    List.LinkedList.list_print(master_list)


def menu2(master_list):
    print("Create new element:")
    List.LinkedList.add_new_element(master_list)
    List.LinkedList.list_print(master_list)
    List.LinkedList.save_changes(master_list)


def menu3(master_list):
    print("Delete element")
    print("Input Id to delete:", end=' ')
    key = input()
    List.LinkedList.delete_element(master_list, key)
    List.LinkedList.list_print(master_list)
    List.LinkedList.save_changes(master_list)


def menu4(master_list):
    print("Element to change:")
    print("ID - 0; Title - 1; DirectorName - 2; PhoneNumber - 3; MonthlyBudget - 4;"
          " YearlyBudget - 5; WebsiteUrl - 6")
    key = input()
    key = int(key)
    print("Input Id to find:", end=' ')
    i_d = input()
    i_d = str(i_d)
    print("Input value:", end=' ')
    value = input()
    List.LinkedList.change_element(master_list, i_d, key, value)
    List.LinkedList.list_print(master_list)
    List.LinkedList.save_changes(master_list)


def menu5(master_list):
    print("Search")
    print("Input phrase to search:", end=' ')
    find = input()
    List.LinkedList.search_element(master_list, find)


def menu6(master_list):
    print("Sort by:")
    print("ID - 0; Title - 1; DirectorName - 2; PhoneNumber - 3; MonthlyBudget - 4;"
          " YearlyBudget - 5; WebsiteUrl - 6")
    key = input()
    key = int(key)
    List.LinkedList.sort_by_elements(master_list, key)
    List.LinkedList.list_print(master_list)
    List.LinkedList.save_changes(master_list)


def menu():
    check = '1'
    while check == '1':
        master_list, choose = menu_start()
        if choose == '1':
            menu1(master_list)
        elif choose == '2':
            menu2(master_list)
        elif choose == '3':
            menu3(master_list)
        elif choose == '4':
            menu4(master_list)
        elif choose == '5':
            menu5(master_list)
        elif choose == '6':
            menu6(master_list)
        else:
            print("Invalid option")
        stop = 1
        while stop == 1:
            print("Continue? Yes - 1 No - 0")
            check = input()
            if check == '1' or check == '0':
                stop = 0
            else:
                print("Invalid option")
                stop = 1
    if check == '0':
        print("Bye")


List.text_start()
menu()
x = Class.Date("12", "2", "2000")
print(Class.Date.get_full_value(x))

