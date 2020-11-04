import Class
import Validator
import os.path
import inspect


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
            x = Class.Date()
            x = Class.Date.create_new_elem(x, arr_main[check][2])
            arr_main[check][2] = x
            y = Class.Date()
            y = Class.Date.create_new_elem(y, arr_main[check][3])
            arr_main[check][3] = y
            check += 1
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
            stop = 0
            while stop < Class.Department.number_of_fields(print_val.data_val):
                if Class.Department.get_value(print_val.data_val, stop) is not None:
                    file.write(Class.Department.get_value(print_val.data_val, stop))
                else:
                    file.write("None")
                file.write(";")
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
        write_arr = ["ID =", "Title =", "DirectorName =", "PhoneNumber =", "MonthlyBudget =",
                     "YearlyBudget =", "WebsiteUrl ="]
        new_arr = []
        check = 0
        while check < len(write_arr):
            print(write_arr[check], end=' ')
            x = input()
            new_arr.append(x)
            check += 1
        x = Class.Department()
        Class.Department.create_new_elem(x, new_arr)
        self.add_to_end(x)
        return self

    def remove_last(self):
        temp = self.head_val
        prev = temp
        while temp.next_val is not None:
            prev = temp
            temp = temp.next_val
        prev.next_val = None





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


