import random


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None
        self.prev_val = None


class LinkedList:
    def __init__(self):
        self.head_val = None

    def move_elements(self, x, key):
        num_elem = self.num_element(x)
        stop = 0
        if x > 0:
            key = num_elem - 1
        while key > stop:
            check = num_elem - 1
            last = self.return_end_val()
            prev = last.prev_val
            while check > 0:
                if self.return_date(last) < 0 and self.return_date(prev) < 0:
                    if x < 0:
                        self.swap_list(last, prev)
                        last = last.prev_val
                        if prev.prev_val is not None:
                            prev = last.prev_val
                        check -= 1
                    elif x > 0:
                        last = last.prev_val
                        if prev.prev_val is not None:
                            prev = prev.prev_val
                elif self.return_date(last) < 0 and self.return_date(prev) > 0:
                    if x < 0:
                        prev = prev.prev_val
                    elif x > 0:
                        last = last.prev_val
                        if prev.prev_val is not None:
                            prev = prev.prev_val
                elif self.return_date(last) > 0 and self.return_date(prev) < 0:
                    if x < 0:
                        last = last.prev_val
                        if prev.prev_val is not None:
                            prev = last.prev_val
                    elif x > 0:
                        if prev.prev_val is not None:
                            prev = prev.prev_val
                elif self.return_date(last) > 0 and self.return_date(prev) > 0:
                    if x < 0:
                        last = last.prev_val
                        if prev.prev_val is not None:
                            prev = prev.prev_val
                    elif x > 0:
                        self.swap_list(last, prev)
                        last = last.prev_val
                        if prev.prev_val is not None:
                            prev = last.prev_val
                        check -= 1
            if x > 0:
                key -= 1
                num_elem -= 1
            elif x < 0:
                stop += 1
        return self

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

    def create_random_list(self):
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
                self.add_to_end(x)
                check += 1
        print("Початковий масив")
        return self

    def num_element(self, x):
        num_elem = 0
        if x < 0:
            help_node = self.head_val
            while help_node is not None:
                if self.return_date(help_node) < 0:
                    num_elem += 1
                help_node = help_node.next_val
        else:
            help_node = self.head_val
            while help_node is not None:
                if self.return_date(help_node) > 0:
                    num_elem += 1
                help_node = help_node.next_val
        return num_elem

    def return_len(self):
        len = 0
        end_val = self.head_val
        while end_val.next_val:
            end_val = end_val.next_val
            len += 1
        return len


def rand(a, b):
    x = random.randint(a, b)
    return x