import Class
import utils
import Validator
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
            Class.Department.print_elem(print_val.data_val)
            print()
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
            elem_add = Class.Department()
            Class.Department.create_new_elem(elem_add, arr_main[check])
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

    def delete_element(self, key):
        help_node = self.head_val
        x = 0
        while help_node is not None:
            if key == Class.Department.get_value(help_node.data_val, 0):
                if x == 0:
                    print("This element was deleted:")
                x = 1
                Class.Department.print_elem(help_node.data_val)
                print()
                if help_node.next_val is not None:
                    help_node.data_val = help_node.next_val.data_val
                    help_node.next_val = help_node.next_val.next_val
                else:
                    LinkedList.remove_last(self)
            help_node = help_node.next_val
        if x == 0:
            print("No elements with this Id")
        print()

    def change_element(self, i_d, key, value):
        x = 1
        help_node = self.head_val
        while help_node is not None:
            if i_d == Class.Department.get_value(help_node.data_val, 0):
                x = 0
                element = Validator.Validate(value)
                value = Validator.Validate.check_invalid_symbols(element)
                Class.Department.add_value(help_node.data_val, value, key)
                print("Changed element:")
                Class.Department.print_elem(help_node.data_val)
                print()
                print()
                break
            help_node = help_node.next_val
        if x == 1:
            print("Element with ID ", i_d, "wasn't found")
        return self

    def search_element(self, find):
        find_arr = []
        main = self.head_val
        find_len = len(find)
        while main is not None:
            atributes = 0
            while atributes < Class.Department.number_of_fields(main.data_val):
                word = Class.Department.get_value(main.data_val, atributes)
                if word is not None:
                    word_len = len(word)
                    if word_len == find_len:
                        if word == find:
                            find_arr.append(main.data_val)
                    elif find_len < word_len:
                        check = 0
                        while check + find_len - 1 < word_len:
                            word_arr = list(word)
                            lil_word_arr = []
                            stop = check
                            x = 0
                            while x < find_len:
                                lil_word_arr.append(word_arr[stop])
                                x += 1
                                stop += 1
                            stop = 0
                            lil_word = ""
                            while stop < len(lil_word_arr):
                                lil_word += lil_word_arr[stop]
                                stop += 1
                            if lil_word == find:
                                find_arr.append(main.data_val)
                            check += 1
                atributes += 1
            main = main.next_val
        if len(find_arr) > 0:
            check = 0
            while check < len(find_arr):
                stop = 0
                while stop < len(find_arr) - check:
                    print(stop, check)
                    if Class.Department.get_value(find_arr[check], 0) == Class.Department.get_value(find_arr[stop], 0)\
                            and stop != check:
                        find_arr.pop(stop)
                        check = 0
                        stop = 0
                    else:
                        stop += 1
                check += 1
            check = 0
            while check < len(find_arr):
                Class.Department.print_elem(find_arr[check])
                print()
                check += 1
        else:
            print("Nothing was found")

    def list_move_end(self, key):
        help_node = self.head_val
        check = 0
        while check != key:
            help_node = help_node.next_val
            check += 1
        while help_node.next_val is not None:
            help_node.data_val, help_node.next_val.data_val = help_node.next_val.data_val, help_node.data_val
            help_node = help_node.next_val
        return self

    def sort_by_elements(self, key):
        if key >= 0 and key <= 6:
            help_node = self.head_val
            while help_node is not None:
                chenge_node = self.head_val
                while chenge_node.next_val is not None:
                    x = utils.to_lover(Class.Department.get_value(chenge_node.data_val, key))
                    y = utils.to_lover(Class.Department.get_value(chenge_node.next_val.data_val, key))
                    if x > y:
                        node = chenge_node.data_val
                        chenge_node.data_val = chenge_node.next_val.data_val
                        chenge_node.next_val.data_val = node
                    chenge_node = chenge_node.next_val
                help_node = help_node.next_val
            help_node = self.head_val
            check = 0
            while help_node is not None:
                if Class.Department.get_value(help_node.data_val, key) == "None":
                    LinkedList.list_move_end(self, check)
                check += 1
                help_node = help_node.next_val
        else:
            print("Invalid key")
        return self


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
    #name = text_check()
    file_name = "Text.txt"
