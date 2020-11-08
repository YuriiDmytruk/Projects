import list

def menu_start():
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
    list.LinkedList.delete_element(master_list, key)
    list.LinkedList.list_print(master_list)
    list.LinkedList.save_changes(master_list)


def menu4(master_list):
    print("One Step Back")
    caretaker = list.Caretaker()
    list.LinkedList.list_print(master_list)
    print()
    list.Caretaker.set_memento(caretaker, list.LinkedList.save_state(master_list))
    list.LinkedList.delete_element(master_list, "123")
    list.LinkedList.list_print(master_list)
    print()
    master_list = list.LinkedList.restore_state(master_list, list.Caretaker.get_memento(caretaker))
    print()
    list.LinkedList.list_print(master_list)


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



"""
originator = Class.Department()
caretaker = Class.Caretaker()

Class.Department.add_value(originator, '123', 0)
print('Originator state:', Class.Department.get_value(originator, 0))

Class.Caretaker.set_memento(caretaker, Class.Department.save_state(originator))
Class.Department.add_value(originator, '432', 0)

print('Originator change state:', Class.Department.get_value(originator, 0))
Class.Department.restore_state(originator, Class.Caretaker.get_memento(caretaker))


print('Originator restore state:', Class.Department.get_value(originator, 0))

"""