import Class
import list


def menu_start():
    master_list = list.LinkedList()
    list.LinkedList.read_from_file(master_list)
    print("If you want to ... click:")
    print("Print file - 1")
    print("Add element - 2")
    print("Delete element by id - 3")
    print("Change element - 4")
    print("Search - 5")
    print("Sort - 6")
    choose = input()
    choose = Class.validate(0, choose, 1)
    return master_list, choose


def menu1(master_list):
    list.LinkedList.list_print(master_list)


def menu2(master_list):
    print("Create new element:")
    list.LinkedList.add_new_element(master_list)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)


def menu3(master_list):
    print("Delete element")
    print("Input Id to delete:", end=' ')
    key = input()
    key = Class.validate(0, key, 1)
    list.LinkedList.delete_element(master_list, key)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)


def menu4(master_list):
    print("Element to change:")
    print("ID - 0; Title - 1; DirectorName - 2; PhoneNumber - 3; MonthlyBudget - 4;"
          " YearlyBudget - 5; WebsiteUrl - 6")
    key = input()
    key = Class.validate(0, key, 1)
    key = int(key)
    print("Input Id to find:", end=' ')
    i_d = input()
    i_d = Class.validate(0, i_d, 1)
    i_d = str(i_d)
    print("Input value:", end=' ')
    value = input()
    list.LinkedList.change_element(master_list, i_d, key, value)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)


def menu5(master_list):
    print("Search")
    print("Input phrase to search:", end=' ')
    find = input()
    list.LinkedList.search_element(master_list, find)
    list.LinkedList.list_print(master_list)


def menu6(master_list):
    print("Sort by:")
    print("ID - 0; Title - 1; DirectorName - 2; PhoneNumber - 3; MonthlyBudget - 4;"
          " YearlyBudget - 5; WebsiteUrl - 6")
    key = input()
    key = Class.validate(0, key, 1)
    key = int(key)
    list.LinkedList.sort_by_elements(master_list, key)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)


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
            Class.validate(0, check, 1)
            if check == '1' or check == '0':
                stop = 0
            else:
                print("Invalid option")
                stop = 1
    if check == '0':
        print("Bye")


list.text_start()
menu()



