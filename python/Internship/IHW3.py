import random


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


class LinkedList:
    def __init__(self):
        self.head_val = None

    def list_print(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data_val, end=', ')
            print_val = print_val.next_val
        print()

    def add_to_begin(self, new_data):
        new_node = Node(new_data)
        new_node.next_val = self.head_val
        self.head_val = new_node

    def add_to_end(self, new_data):
        new_node = Node(new_data)
        if self.head_val is None:
            self.head_val = new_node
            return
        end_val = self.head_val
        while end_val.next_val:
            end_val = end_val.next_val
        end_val.next_val = new_node

    def add_to_middle(self, middle_node, new_data):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        new_node = Node(new_data)
        new_node.next_val = middle_node.next_val
        middle_node.next_val = new_node

    def return_date(self, node):
        return node.data_val

    def return_end_val(self):
        end_val = self.head_val
        while end_val.next_val:
            end_val = end_val.next_val
        return end_val

    def return_prev_val(self, node):
        prev_val = self.head_val
        while prev_val.next_val != node:
            prev_val = prev_val.next_val
        return prev_val

    def swap_list(self, node1, node2):
        new_node = Node()
        new_node.data_val = node1.data_val
        node1.data_val = node2.data_val
        node2.data_val = new_node.data_val


def return_prev_val_y(l_list, node, y):
    prev_node = l_list.return_prev_val(node)
    check = 0
    while check < y:
        prev_node = l_list.return_prev_val(prev_node)
        check += 1
    return prev_node


def rand(a, b):
    x = random.randint(a, b)
    return x


def info(l_list, x, y, val1, val2):
    l_list.list_print()
    print("Last: ", val1)
    print("Change: ", val2)
    print("Y: ", y)
    print("X: ", x)


def create_random_linked_list(l_list):
    """
    check = 0
    print("Введіть межі a і b")
    while check == 0:
        a = int(input("a = "))
        b = int(input("b = "))
        if a < b:
            check = 1
        else:
            print("b має бути більше за a!")
    check = 0
    while check == 0:
        n = int(input("N = "))
        if n > 0:
            check = 1
        else:
            print("N має бути > 0")
"""
    n = 5
    a = -9
    b = 9
    check = 0
    arr = [-5,-2,3,-1,2,4]
    #arr[check]
    while check <= n:
        x = rand(a, b)
        l_list.add_to_end(arr[check])
        check += 1
    print("Початковий масив")

    return l_list


def move_minus(l_list, key):
    # number minus elements
    num_minus_elem = 0
    help_node = l_list.head_val
    while help_node is not None:
        if l_list.return_date(help_node) < 0:
            num_minus_elem += 1
        help_node = help_node.next_val
    print(num_minus_elem)

    # move minus elements
    y = 1
    stop = 0
    while stop < key:
        x = num_minus_elem - 1
        help_node = l_list.return_end_val()
        change_node = l_list.return_prev_val(help_node)
        print("-------")
        info(l_list, x, y, l_list.return_date(help_node), l_list.return_date(change_node))
        while x > 0:
            print("++++++++")
            info(l_list, x, y, l_list.return_date(help_node), l_list.return_date(change_node))
            change_node = return_prev_val_y(l_list, help_node, y)
            if l_list.return_date(help_node) < 0 and l_list.return_date(change_node) < 0:
                print("======")
                info(l_list, x, y, l_list.return_date(help_node), l_list.return_date(change_node))
                l_list.swap_list(help_node, change_node)
                x -= 1
                y = 1
                help_node = l_list.return_prev_val(help_node)
                print("+")
            elif l_list.return_date(help_node) < 0 and l_list.return_date(change_node) > 0:
                print("======")
                info(l_list, x, y, l_list.return_date(help_node), l_list.return_date(change_node))
                y += 1

            elif l_list.return_date(help_node) > 0 and l_list.return_date(change_node) < 0:
                print("======")
                info(l_list, x, y, l_list.return_date(help_node), l_list.return_date(change_node))
                help_node = l_list.return_prev_val(help_node)
            elif l_list.return_date(help_node) > 0 and l_list.return_date(change_node) > 0:
                print("======")
                info(l_list, x, y, l_list.return_date(help_node), l_list.return_date(change_node))
                help_node = l_list.return_prev_val(help_node)
                y += 1
            l_list.list_print()
        stop += 1
    return l_list


linked_list = LinkedList()
create_random_linked_list(linked_list)
linked_list.list_print()


"""

while check == 0:
    k = int(input("K = "))
    if k > 0:
        check = 1
    else:
        print("N має бути > 0")
"""
k = 2

move_minus(linked_list, k)
linked_list.list_print()
