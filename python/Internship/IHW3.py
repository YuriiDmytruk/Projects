import random


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None
        self.prev_val = None


class LinkedList:
    def __init__(self):
        self.head_val = None

    def list_print(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data_val, end=', ')
            print_val = print_val.next_val
        print()

    def add_to_end(self, new_data):
        new_node = Node(new_data)
        if self.head_val is None:
            self.head_val = new_node
            return
        end_val = self.head_val
        while end_val.next_val:
            end_val = end_val.next_val
        end_val.next_val = new_node
        new_node.prev_val = end_val

    def return_date(self, node):
        return node.data_val

    def return_end_val(self):
        end_val = self.head_val
        while end_val.next_val:
            end_val = end_val.next_val
        return end_val

    def swap_list(self, node1, node2):
        new_node = Node()
        new_node.data_val = node1.data_val
        node1.data_val = node2.data_val
        node2.data_val = new_node.data_val


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
    check = 0
    while check <= n:
        x = rand(a, b)
        if x != 0:
            l_list.add_to_end(x)
            check += 1
    print("Початковий масив")

    return l_list


def num_element_counter(l_list, x):
    num_elem = 0
    if x < 0:
        help_node = l_list.head_val
        while help_node is not None:
            if l_list.return_date(help_node) < 0:
                num_elem += 1
            help_node = help_node.next_val
    else:
        help_node = l_list.head_val
        while help_node is not None:
            if l_list.return_date(help_node) > 0:
                num_elem += 1
            help_node = help_node.next_val
    return num_elem


def move_minus(l_list, key):
    num_minus_elem = num_element_counter(l_list, -1)
    stop = 0
    while stop < key:
        x = num_minus_elem - 1
        last = l_list.return_end_val()
        prev = last.prev_val
        while x > 0:

            if l_list.return_date(last) < 0 and l_list.return_date(prev) < 0:
                l_list.swap_list(last, prev)
                last = last.prev_val
                if prev.prev_val is not None:
                    prev = last.prev_val
                x -= 1
            elif l_list.return_date(last) < 0 and l_list.return_date(prev) > 0:
                prev = prev.prev_val
            elif l_list.return_date(last) > 0 and l_list.return_date(prev) < 0:
                last = last.prev_val
                if prev.prev_val is not None:
                    prev = last.prev_val
            elif l_list.return_date(last) > 0 and l_list.return_date(prev) > 0:
                last = last.prev_val
                if prev.prev_val is not None:
                    prev = prev.prev_val
        stop += 1
    linked_list.list_print()
    return l_list


def move_plus(l_list):
    num_plus_elem = num_element_counter(l_list, 1)
    stop = num_plus_elem - 1
    while stop > 0:
        x = num_plus_elem - 1
        last = l_list.return_end_val()
        prev = last.prev_val

        while x > 0:
            if l_list.return_date(last) > 0 and l_list.return_date(prev) > 0:
                l_list.swap_list(last, prev)
                last = last.prev_val
                if prev.prev_val is not None:
                    prev = last.prev_val
                x -= 1
            elif l_list.return_date(last) > 0 and l_list.return_date(prev) < 0:
                if prev.prev_val is not None:
                    prev = prev.prev_val
            elif l_list.return_date(last) < 0 and l_list.return_date(prev) > 0:
                last = last.prev_val
                if prev.prev_val is not None:
                    prev = prev.prev_val
            elif l_list.return_date(last) < 0 and l_list.return_date(prev) < 0:
                last = last.prev_val
                if prev.prev_val is not None:
                    prev = prev.prev_val
        num_plus_elem -= 1
        stop -= 1
    linked_list.list_print()
    return l_list


linked_list = LinkedList()
create_random_linked_list(linked_list)
check = 0
while check == 0:
    k = int(input("K = "))
    if k > 0:
        check = 1
    else:
        print("N має бути > 0")
linked_list.list_print()
move_minus(linked_list, k)
move_plus(linked_list)

