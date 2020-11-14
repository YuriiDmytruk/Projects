import list
import momento


def main_menu(history):
    master_list = list.LinkedList()
    list.LinkedList.read_from_file(master_list)
    if momento.CareTaker.get_len(history) == 0:
        list.LinkedList.save_state(master_list, history)
    print("If you want to ... click:")
    print("1 - Print file")
    print("2 - Add element")
    print("3 - Delete element by id")
    print("4 - Change element")
    print("5 - Search")
    print("6 - Sort")
    print("7 - Undo")
    print("8 - Redo")
    print("9 - Show History")
    print("10 - Load from History by number")
    choose = input()
    choose = str(choose)
    return master_list, choose, history


def menu1(master_list):
    list.LinkedList.list_print(master_list)


def menu2(master_list, history):
    print("Create new element:")
    list.LinkedList.add_new_element(master_list)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)
    list.LinkedList.save_state(master_list, history)


def menu3(master_list, history):
    print("Delete element")
    print("Input Id to delete:", end=' ')
    key = input()
    list.LinkedList.delete_element(master_list, key)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)
    list.LinkedList.save_state(master_list, history)


def menu4(master_list, history):
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
    list.LinkedList.change_element(master_list, i_d, key, value)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)
    list.LinkedList.save_state(master_list, history)


def menu5(master_list):
    print("Search")
    print("Input phrase to search:", end=' ')
    find = input()
    list.LinkedList.search_element(master_list, find)


def menu6(master_list, history):
    print("Sort by:")
    print("ID - 0; Title - 1; DirectorName - 2; PhoneNumber - 3; MonthlyBudget - 4;"
          " YearlyBudget - 5; WebsiteUrl - 6")
    key = input()
    key = int(key)
    list.LinkedList.sort_by_elements(master_list, key)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)
    list.LinkedList.save_state(master_list, history)


def menu7(master_list, history):
    #Назад
    print("Undo")
    master_list, key = list.LinkedList.undo(master_list, history)
    if key == 1:
        list.LinkedList.list_print(master_list)
        list.LinkedList.save_changes(master_list)
    else:
        print("You are on the first step of history")


def menu8(master_list, history):
    # Вперед
    print("Redo")
    master_list, key = list.LinkedList.redo(master_list, history)
    if key == 1:
        list.LinkedList.list_print(master_list)
        list.LinkedList.save_changes(master_list)
    else:
        print("You are on the last step of history")


def menu9(history):
    momento.CareTaker.show_history(history)


def menu():
    history = momento.CareTaker()
    check = '1'
    while check == '1':
        master_list, choose, history = main_menu(history)
        if choose == '1':
            menu1(master_list)
        elif choose == '2':
            menu2(master_list, history)
        elif choose == '3':
            menu3(master_list, history)
        elif choose == '4':
            menu4(master_list, history)
        elif choose == '5':
            menu5(master_list)
        elif choose == '6':
            menu6(master_list, history)
        elif choose == '7':
            menu7(master_list, history)
        elif choose == '8':
            menu8(master_list, history)
        elif choose == '9':
            menu9(history)
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


list.text_start()
menu()
