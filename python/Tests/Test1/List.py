import Class
import os.path


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
            Class.Library.print_element(print_val.data_val)
            print_val = print_val.next_val

    def read_from_file(self):
        file = open(file_name, "r")
        arr_main = []
        for line in file:
            arr_to_add = []
            word = ""
            for letter in line:
                if letter == ';':
                    arr_to_add.append(word)
                    word = ""
                else:
                    word += letter
            arr_main.append(arr_to_add)
        file.close()
        check = 0
        while check < len(arr_main):
            elem_add = Class.Library()
            Class.Library.create_new_elem(elem_add, arr_main[check])
            self.add_to_end(elem_add)
            check += 1
        return self

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

    def return_len(self):
        len = 0
        end_val = self.head_val
        while end_val.next_val:
            end_val = end_val.next_val
            len += 1
        return len

    def renew_file(self):
        open(file_name, "w").close()
        file = open(file_name, "w")
        print_val = self.head_val
        while print_val is not None:
            x = 0
            stop = 0
            while stop < Class.Library.number_of_fields(print_val.data_val):
                if Class.Library.get_value(print_val.data_val, stop) is not None:
                    if str(type(Class.Library.get_value(print_val.data_val, stop)).__name__) == "Date":
                        file.write(Class.Date.full_value(Class.Library.get_value(print_val.data_val, stop)))
                    else:
                        if Class.Library.get_value(print_val.data_val) is not None:
                            file.write(Class.Library.get_value(print_val.data_val, stop))
                        else:
                            file.write("None")
                else:
                    file.write("None")
                file.write(";")
                x += 1
                stop += 1
            print_val = print_val.next_val
            file.write("\n")
        file.close()

    def save_changes(self):
        print("Save changes to file?")
        print("Yes - 1; No - 0")
        save = int(input())
        if save == 1:
            LinkedList.renew_file(self)
        return self

    def add_new_element(self):
        """
        write_arr = ["Title =", "Rent price =", "Start rent date =", "End rent date =", "User name ="]
        new_arr = []
        check = 0
        while check < len(write_arr):
            print(write_arr[check], end=' ')
            x = input()
            new_arr.append(x)
            check += 1
        """
        new_arr = ["Title1", "12,56", "12-5-2001", "23-4-2007", "Chak"]
        x = Class.Library()
        Class.Library.create_new_elem(x, new_arr)
        self.add_to_end(x)
        return self

    def remove_last(self):
        temp = self.head_val
        prev = temp
        while temp.next_val is not None:
            prev = temp
            temp = temp.next_val
        prev.next_val = None

    def check_date(self):
        help_node = self.head_val
        while help_node is not None:
            check_node = help_node.next_val
            while check_node is not None:
                Class.Library.compare_date(help_node.data_val, check_node.data_val)
                check_node = check_node.next_val
            help_node = help_node.next_val


def text_check():
    name = ""
    print("Insert File name")
    x = 0
    while x == 0:
        name = input()
        if os.path.isfile(name):
            x = 1
        else:
            x = 0
            print("File not exist")
    return name


def text_start():
    global file_name
    # name = text_check()
    file_name = "Text.txt"


