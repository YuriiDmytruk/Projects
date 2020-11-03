import inspect


class Library:
    def __init__(self, title=None, rent_price=None, start_rent_date=None, end_rent_date=None, user_name=None):
        self.title = title
        self.rent_price = rent_price
        self.start_rent_date = start_rent_date
        self.end_rent_date = end_rent_date
        self.user_name = user_name

    def create_new_elem(self, arr_add):
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

    def print_elem(self):
        check = 0
        while check < Library.number_of_fields(self):
            if inspect.isclass(Date):

            else:
                print(Library.get_value(self, check), end='; ')
            check += 1




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
        while check < Date.number_of_fields(self):
            Date.add_value(self, arr_add[check], check)
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

    def print_elem(self):
        check = 0
        word = ""
        x = 1
        while check < Date.number_of_fields(self):
            if x > 2:
                word += Date.get_value(self, check)
            else:
                word += Date.get_value(self, check)
                word += "-"
            check += 1
            x += 1
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