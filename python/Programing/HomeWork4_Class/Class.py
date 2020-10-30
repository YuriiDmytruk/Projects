class Department:
    def __init__(self, id=None, title=None, director_name=None, phone_number=None, monthly_budget=None,
                 yearly_budget=None, website_url=None):
        self.id = id
        self.title = title
        self.director_name = director_name
        self.phone_number = phone_number
        self.monthly_budget = monthly_budget
        self.yearly_budget = yearly_budget
        self.website_url = website_url

    def print_elem(self):
        check = 0
        while check < Department.number_of_fields(self):
            print(Department.get_value(self, check), end='; ')
            check += 1

    def get_value(self, key):
        number = 0
        for attribute, value in self.__dict__.items():
            if number == key:
                return value
            else:
                number += 1

    def add_value(self, value, key):
        if value == "":
            value = "None"
        if key == 0:
            self.id = value
        elif key == 1:
            self.title = value
        elif key == 2:
            self.director_name = value
        elif key == 3:
            self.phone_number = value
        elif key == 4:
            self.monthly_budget = value
        elif key == 5:
            self.yearly_budget = value
        elif key == 6:
            self.website_url = value
        else:
            print("Invalid key")

    def create_new_elem(self, arr_add):
        validate(arr_add, 0, 0)
        check = 0
        while check < Department.number_of_fields(self):
            Department.add_value(self, arr_add[check], check)
            check += 1
        return self

    def number_of_fields(self):
        fields = 0
        for attribute, value in self.__dict__.items():
            fields += 1
        return fields


def validate(master, main_word, main_key):
    def check_invalid_symbols(word, key):
        if key == 0 or key == 4 or key == 5:
            word = leave_letter_number(word, 1)
        elif key == 1 or key == 2:
            word = leave_letter_number(word, 0)
        elif key == 3:
            word = leave_letter_number(word, 1)
            word = to_phone(word)
        elif key == 6:
            word = to_url(word)
        else:
            print("Invalid key")
        return word

    def full_validation(valid_arr):
        arr_ret = []
        check = 0
        while check < len(valid_arr):
            valid_arr[check] = check_invalid_symbols(valid_arr[check], check)
            check += 1
        return arr_ret

    def to_phone(word):
        word_arr = list(word)
        check = 0
        while check < len(word_arr):
            x = is_lns(word_arr[check], 2)
            if x == 1:
                word_arr.pop(check)
                check = -1
            check += 1
        if len(word_arr) < 13:
            while len(word_arr) != 12:
                word_arr.append('0')
        word = ""
        check = 0
        stop = 0
        phone_symbols = ['+', '(', ')', '-', '-']
        while check < len(word_arr):
            if check == 0:
                word += phone_symbols[stop]
                stop += 1
            elif check == 3:
                word += phone_symbols[stop]
                stop += 1
            elif check == 5:
                word += phone_symbols[stop]
                stop += 1
            elif check == 8:
                word += phone_symbols[stop]
                stop += 1
            elif check == 10:
                word += phone_symbols[stop]
                stop += 1
            if check < 12:
                word += word_arr[check]
            check += 1
        return word

    def to_url(word):
        word_arr = list(word)
        y = 0
        if word_arr[0] + word_arr[1] + word_arr[2] != "www":
            word = "www."
            word += arr_to_word(word_arr)
            y = 1
        if word_arr[len(word_arr) - 3] + word_arr[len(word_arr) - 2] +\
           word_arr[len(word_arr) - 1] != "com":
            if y == 1:
                word += ".com"
            else:
                word += arr_to_word(word_arr)
                word += ".com"
        return word

    def leave_letter_number(word, key):
        if key == 0:
            word = delete_lns(word, 1)
            word = delete_lns(word, 2)
            return word
        elif key == 1:
            word = delete_lns(word, 0)
            word = delete_lns(word, 2)
            return word
        else:
            print("Invalid key")

    def delete_lns(word, key):
        word_arr = list(word)
        check = 0
        while check < len(word_arr):
            if key == 2:
                x = is_lns(word_arr[check], 0)
                y = is_lns(word_arr[check], 1)
                z = is_lns(word_arr[check], 2)
                if x == 0 and y == 0 and z == 0:
                    word_arr.pop(check)
                    check = -1
                check += 1
            else:
                x = is_lns(word_arr[check], key)
                if x == 1:
                    word_arr.pop(check)
                    check = -1
                check += 1
        word = arr_to_word(word_arr)
        return word

    def is_lns(letter, key):
        letter_word = "abcdefghilklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number_word = "1234567890"
        sybmols_word = ""
        if key == 0:
            main_arr = list(letter_word)
        elif key == 1:
            main_arr = list(number_word)
        elif key == 2:
            main_arr = list(sybmols_word)
        else:
            print("Invalid key")
        check = 0
        while check < len(main_arr):
            if letter == main_arr[check]:
                return 1
            else:
                check += 1
        return 0

    def arr_to_word(arr):
        word = ""
        check = 0
        while check < len(arr):
            word += arr[check]
            check += 1
        return word

    if main_word == 0:
        full_validation(master)
        return master
    elif master == 0:
        main_word = leave_letter_number(main_word, main_key)
        return main_word
    else:
        print("Validation vent wrong")
