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
            if print_val.data_val is not None:
                print(print_val.data_val, end=", ")
            else:
                print("None", end=", ")
            print_val = print_val.next_val
        print()

    def add_to_end(self, new_data):
        if self is None:
            return None
        else:
            if new_data == "" or new_data is None:
                new_data = "None"
            new_node = Node(new_data)
            if self.head_val is None:
                self.head_val = new_node
                return self
            end_val = self.head_val
            while end_val.next_val:
                end_val = end_val.next_val
            end_val.next_val = new_node
            new_node.prev_val = end_val
            return self

    def insert(self, i_d, value):
        if i_d is None or value is None:
            print("None error")
        else:
            if i_d > LinkedList.return_len(self):
                LinkedList.create_none(self, i_d)

            LinkedList.set_by_id(self, i_d, value)
            return self

    def create_none(self, i_d):
        while i_d > LinkedList.return_len(self):
            LinkedList.add_to_end(self, None)
        return self

    def set_by_id(self, i_d, value):
        if i_d == 0:
            LinkedList.add_to_end(self, value)
            return self
        else:
            help_node = self.head_val
            check = 0
            while check != i_d:
                help_node = help_node.next_val
                check += 1
            help_node.data_val = value
            return self

    def return_len(self):
        if self is None:
            return None
        else:
            len = 0
            end_val = self.head_val
            if end_val is None:
                return 0
            else:
                while end_val.next_val:
                    end_val = end_val.next_val
                    len += 1
                return len

    def delete_element(self, i_d):
        if i_d > LinkedList.return_len(self):
            print("This id not exist")
        else:
            help_node = self.head_val
            check = 0
            while help_node is not None:
                if i_d == check:
                    if help_node.next_val is not None:
                        help_node.data_val = help_node.next_val.data_val
                        help_node.next_val = help_node.next_val.next_val
                    else:
                        LinkedList.remove_last(self)
                help_node = help_node.next_val
                check += 1
            return self

    def delete_in_range(self, start, stop):
        if start > LinkedList.return_len(self) or stop < 0:
            print("Wrong parameters")
        else:
            start += 1
            while start != stop:
                LinkedList.delete_element(self, start)
                stop -= 1
        return self

    def remove_last(self):
        if self is None:
            return None
        else:
            temp = self.head_val
            prev = temp
            while temp.next_val is not None:
                prev = temp
                temp = temp.next_val
            prev.next_val = None
            return self

    def sort(self):
        help_node = self.head_val
        while help_node is not None:
            chenge_node = self.head_val
            while chenge_node.next_val is not None:
                x = chenge_node.data_val
                y = chenge_node.next_val.data_val
                if x > y:
                    node = chenge_node.data_val
                    chenge_node.data_val = chenge_node.next_val.data_val
                    chenge_node.next_val.data_val = node
                chenge_node = chenge_node.next_val
            help_node = help_node.next_val
        help_node = self.head_val
        check = 0
        while help_node is not None:
            if help_node.data_val == "None":
                LinkedList.list_move_end(self, check)
            check += 1
            help_node = help_node.next_val
        return self

    def list_move_end(self, key):
        if self is None or key is None:
            return None
        else:
            help_node = self.head_val
            check = 0
            while check != key:
                help_node = help_node.next_val
                check += 1
            while help_node.next_val is not None:
                help_node.data_val, help_node.next_val.data_val = help_node.next_val.data_val, help_node.data_val
                help_node = help_node.next_val
            return self

    def copy_list(self):
        if self is None:
            return None
        else:
            new = LinkedList()
            node = self.head_val
            while node is not None:
                LinkedList.add_to_end(new, node.data_val)
                node = node.next_val
            return new
