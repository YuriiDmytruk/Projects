class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None
        self.prev_val = None


class LinkedList:
    def __init__(self):
        self.head_val = None

    def return_head(self):
        return self.head_val

    def list_print(self):
        print_val = self.head_val.next_val
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
        x = self.head_val
        if x is None:
            return 0
        else:
            end_val = self.head_val
            while end_val.next_val:
                end_val = end_val.next_val
                len += 1
            return len


    def return_next_val(self, now):
        now = now.next_val
        return now
