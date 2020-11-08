import Class


def print_arr(array):
    check = 0
    while check < len(array):
        Class.Department.print_elem(array[check])
        print()
        check += 1


def read_from_file():
    file = open("Text.txt", "r")
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
    master = []
    while check < len(arr_main):
        elem_add = Class.Department()
        Class.Department.create_new_elem(elem_add, arr_main[check])
        master.append(elem_add)
        check += 1
    return master


def renew_file(master):
    open("Text.txt", "w").close()
    file = open("Text.txt", "w")
    check = 0
    while check < len(master):
        stop = 0
        while stop < 7:
            file.write(Class.Department.get_value(master[check], stop))
            file.write(";")
            stop += 1
        check += 1
        file.write("\n")
    file.close()


def save_changes(master):
    print("Save changes to file?")
    print("Yes - 1; No - 0")
    save = int(input())
    if save == 1:
        renew_file(master)
    master = read_from_file()
    return master


def add_new_element(master):
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
    master.append(x)
    return master


def delete_elem_id(master, key):
    check = 0
    x = 0
    while check < len(master):
        if key == Class.Department.get_value(master[check], 0):
            x = 1
            print("This element was deleted:")
            Class.Department.print_elem(master[check])
            print()
            print()
            master.pop(check)
        check += 1
    if x == 0:
        print("No elements with this Id")
    return master


def change_element(master, i_d, key, value):
    check = 0
    x = 1
    while check < len(master):
        if i_d == Class.Department.get_value(master[check], 0):
            x = 0
            Class.Department.add_value(master[check], value, key)
        check += 1
    if x == 1:
        print("Element with ID ", i_d, "wasn't found")
    return master


def search_element(master, find):
    find_arr = list(find)
    search_arr = []
    arr_elem = 0
    while arr_elem < len(master):
        class_elem = 0
        while class_elem < 7:
            checked_word = list(Class.Department.get_value(master[arr_elem], class_elem))
            letter_word = 0
            if len(checked_word) == len(find_arr):
                if checked_word == find_arr:
                    search_arr.append(master[arr_elem])
            if len(checked_word) > len(find_arr):
                while letter_word < len(checked_word) - len(find_arr):
                    x = 1
                    letter_find = 0
                    while letter_find < len(find_arr) and x == 1:
                        if checked_word[letter_word + letter_find] == find_arr[letter_find]:
                            x = 1
                        else:
                            x = 0
                        letter_find += 1
                    if x == 1:
                        search_arr.append(master[arr_elem])
                    letter_word += 1
            class_elem += 1
        arr_elem += 1
    if len(search_arr) == 0:
        print("Nothing was found")
    return search_arr


def swap(master, x, y):
    if x != len(master) - 1:
        master[x], master[y] = master[y], master[x]
    return master


def arr_move_end(master, key):
    while key < len(master):
        swap(master, key, key + 1)
        key += 1
    return master


def sort_by_elements(master, key):
    if key >= 0 and key <= 6:
        n = 1
        while n < len(master):
            for i in range(len(master) - n):
                if key == 1 or key == 2 or key == 6:
                    x = to_lover(Class.Department.get_value(master[i], key))
                    y = to_lover(Class.Department.get_value(master[i + 1], key))
                else:
                    x = Class.Department.get_value(master[i], key)
                    y = Class.Department.get_value(master[i + 1], key)
                if x > y:
                    master[i], master[i + 1] = master[i + 1], master[i]
            n += 1
        check = 0
        while check < len(master):
            if Class.Department.get_value(master[check], key) == "None":
                arr_move_end(master, check)
            check += 1
    else:
        print("Invalid key")
    return master


def to_lover(word):
    word_arr = list(word)
    word = ""
    letter_word = "abcdefghilklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_arr = list(letter_word)
    letter = 0
    while letter < len(word_arr):
        check = 0
        while check < len(letter_arr):
            if word_arr[letter] == letter_arr[check]:
                if check > 25:
                    word_arr[letter] = letter_arr[check - 26]
                word += word_arr[letter]
            check += 1
        letter += 1
    return word


def menu():
    check = '1'
    while check == '1':
        master_arr = read_from_file()
        renew_file(master_arr)
        print("If you want to ... click:")
        print("Print file - 1")
        print("Add element - 2")
        print("Delete element by id - 3")
        print("Change element - 4")
        print("Search - 5")
        print("Sort - 6")
        choose = input()
        choose = Class.validate(0, choose, 1)
        if choose == '1':
            print("Your file:")
            master_arr = read_from_file()
            print_arr(master_arr)
        elif choose == '2':
            print("Create new element:")
            add_new_element(master_arr)
            print_arr(master_arr)
            save_changes(master_arr)
        elif choose == '3':
            print("Delete element")
            print("Input Id to delete:", end=' ')
            key = input()
            key = Class.validate(0, key, 1)
            delete_elem_id(master_arr, key)
            print_arr(master_arr)
            save_changes(master_arr)
        elif choose == '4':
            print("Element to change:")
            print("ID - 0; Title - 1; DirectorName - 2; PhoneNumber - 3; MonthlyBudget - 4;"
                  " YearlyBudget - 5; WebsiteUrl - 6")
            key = input()
            key = Class.validate(0, key, 1)
            key = int(key)
            print("Input Id to find:", end=' ')
            i_d = input()
            i_d = Class.validate(0, i_d, 1)
            i_d = str(i_d)
            print("Input value:", end=' ')
            value = input()
            change_element(master_arr, i_d, key, value)
            print_arr(master_arr)
            save_changes(master_arr)
        elif choose == '5':
            print("Search")
            print("Input phrase to search:", end=' ')
            find = input()
            arr = search_element(master_arr, find)
            print_arr(arr)
        elif choose == '6':
            print("Sort by:")
            print("ID - 0; Title - 1; DirectorName - 2; PhoneNumber - 3; MonthlyBudget - 4;"
                  " YearlyBudget - 5; WebsiteUrl - 6")
            key = input()
            key = Class.validate(0, key, 1)
            key = int(key)
            sort_by_elements(master_arr, key)
            print_arr(master_arr)
            save_changes(master_arr)
        else:
            print("Invalid option")
        stop = 1
        while stop == 1:
            print("Continue? Yes - 1 No - 0")
            check = input()
            Class.validate(0, check, 1)
            if check == '1' or check == '0':
                stop = 0
            else:
                print("Invalid option")
                stop = 1
    if check == '0':
        print("Bye")


menu()
