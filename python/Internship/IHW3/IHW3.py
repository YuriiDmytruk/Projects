import Class


def info(l_list, x, y, val1, val2):
    l_list.list_print()
    print("Last: ", val1)
    print("Change: ", val2)
    print("Y: ", y)
    print("X: ", x)


linked_list = Class.LinkedList()
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

