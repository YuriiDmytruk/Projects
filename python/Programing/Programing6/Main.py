import list
import momento

def menu_start():
    history = momento.CareTaker()
    master_list = list.LinkedList()
    list.LinkedList.read_from_file(master_list)
    print("If you want to ... click:")
    print("1 - Print file")
    print("2 - Add element")
    print("3 - Delete element by id")
    print("4 - One Step Back")
    #choose = input()
    choose = 4
    choose = str(choose)
    return master_list, choose, history


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
    list.LinkedList.delete_element(master_list, key)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)


def menu4(master_list, history):
    print("One Step Back")
    print()
    list.LinkedList.save_state(master_list, history)
    list.LinkedList.delete_element(master_list, "123", history)
    list.LinkedList.save_state(master_list, history)
    momento.CareTaker.show_history(history)



    """
    momento.Caretaker.show_history(history)
   
    list.LinkedList.delete_element(master_list, "123", history)
    list.LinkedList.save_state(master_list, history)
    momento.Caretaker.show_history(history)
    list.LinkedList.delete_element(master_list, "645", history)
    list.LinkedList.save_state(master_list, history)
    momento.Caretaker.show_history(history)
    """
    print()


def menu():
    check = '1'
    while check == '1':
        master_list, choose, history = menu_start()
        if choose == '1':
            menu1(master_list)
        elif choose == '2':
            menu2(master_list)
        elif choose == '3':
            menu3(master_list)
        elif choose == '4':
            menu4(master_list, history)
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
