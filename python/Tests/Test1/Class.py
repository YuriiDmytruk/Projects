import Validator


class Library:
    def __init__(self, title=None, rent_price=None, start_rent_date=None, end_rent_date=None, user_name=None):
        self.title = title
        self.rent_price = rent_price
        self.start_rent_date = start_rent_date
        self.end_rent_date = end_rent_date
        self.user_name = user_name

    def create_new_elem(self, arr_add):
        x = Date()
        x = Date.create_new_elem(x, arr_add[2])
        arr_add[2] = x
        y = Date()
        y = Date.create_new_elem(y, arr_add[3])
        arr_add[3] = y
        validate_list_add(arr_add)
        is_date_correct(arr_add)
        check = 0
        while check < Library.number_of_fields(self):
            Library.add_value(self, arr_add[check], check)
            check += 1

        return self

    def add_value(self, value, key):
        if value == "":
            value = "None"
        number = 0
        for attribute in self.__dict__.items():
            if number == key:
                name = str(attribute)
                name = get_name(name)
                self.__dict__[name] = value
                break
            else:
                number += 1

    def number_of_fields(self):
        fields = 0
        for attribute, value in self.__dict__.items():
            fields += 1
        return fields

    def get_value(self, key):
        number = 0
        for attribute, value in self.__dict__.items():
            if number == key:
                return value
            else:
                number += 1

    def print_element(self):
        x = 0
        for attribute, value in self.__dict__.items():
            name = str(attribute)
            if name == "start_rent_date" or name == "end_rent_date":
                Date.print_element(value)
                print("; ", end='')
            else:
                print(value, end='; ')
            x += 1
        print()

    def compare_date(self, check):
        check_date_arr = []
        help_date_arr = []
        for attribute, value in self.__dict__.items():
            name = str(attribute)
            if name == "start_rent_date" or name == "end_rent_date":
                help_date_arr.append(value)
        for attribute, value in check.__dict__.items():
            name = str(attribute)
            if name == "start_rent_date" or name == "end_rent_date":
                check_date_arr.append(value)
        compare_date(help_date_arr, check_date_arr)

class Date:
    def __init__(self, day=None, month=None, year=None):
        self.day = day
        self.month = month
        self.year = year

    def create_new_elem(self, name):
        arr_add = []
        check = 0
        element = ""
        while check < len(name):
            if name[check] == "-":
                arr_add.append(element)
                element = ""
            else:
                element += name[check]
            check += 1
        arr_add.append(element)
        check = 0
        validate_list_add(arr_add)
        while check < Date.number_of_fields(self):
            Date.add_value(self, arr_add[check], check)
            check += 1
        x = Date.validate(self)
        return x

    def add_value(self, value, key):
        if value == "":
            value = "None"
        number = 0
        for attribute in self.__dict__.items():
            if number == key:
                name = str(attribute)
                name = get_name(name)
                self.__dict__[name] = value
            else:
                number += 1

    def number_of_fields(self):
        fields = 0
        for attribute, value in self.__dict__.items():
            fields += 1
        return fields

    def get_value(self, key):
        number = 0
        for attribute, value in self.__dict__.items():
            if number == key:
                return value
            else:
                number += 1

    def print_element(self):
        x = 0
        for attribute, value in self.__dict__.items():
            print(value, end='')
            if x != 2:
                print('-', end="")
            x += 1

    def validate(self):
        x = Validator.Validate(Date.get_value(self, 0))
        a = Validator.Validate.day_validation(x, Date.get_value(self, 1), Date.get_value(self, 1))
        x = Validator.Validate(Date.get_value(self, 1))
        b = Validator.Validate.month_validation(x)
        x = Validator.Validate(Date.get_value(self, 2))
        c = Validator.Validate.year_validation(x)
        if a is None or b is None or c is None:
            Date.full_none(self)
            return self
        else:
            return self

    def full_none(self):
        self.day = None
        self.month = None
        self.year = None
        return self

    def full_value(self):
        if self.day is None or self.month is None or self.year is None:
            Date.full_none(self)
        word = self.day
        word += "-"
        word += self.month
        word += "-"
        word += self.year
        return word


def get_name(name):
    ret_name = ""
    check = 0
    x = 0
    while check < len(name):
        if name[check] == "'":
            x += 1
            check += 1
        if x == 1:
            ret_name += name[check]
            check += 1
        elif x == 2:
            break
        else:
            check += 1
    return ret_name


def validate_list_add(arr_add):
    check = 0
    while check < len(arr_add):
        element = Validator.Validate(arr_add[check])
        add_value = Validator.Validate.check_invalid_symbols(element)
        arr_add[check] = add_value
        check += 1
    return arr_add


def is_date_correct(arr):
    x = arr[2]
    y = arr[3]
    if int(Date.get_value(x, 2)) > int(Date.get_value(y, 2)):
        special(x, y, arr)
        return arr
    else:
        if int(Date.get_value(x, 1)) > int(Date.get_value(y, 1)) and Date.get_value(x, 2) == Date.get_value(y, 2):
            special(x, y, arr)
            return arr
        else:
            if int(Date.get_value(x, 0)) > int(Date.get_value(y, 0)) and Date.get_value(x, 2) == Date.get_value(y, 2)\
                    and Date.get_value(x, 1) == Date.get_value(y, 1):
                special(x, y, arr)
                return arr
            else:
                return arr


def special(x, y, arr):
    Date.full_none(x)
    Date.full_none(y)
    arr[2] = x
    arr[3] = y
    return arr