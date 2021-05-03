import Validator


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

    def __str__(self):
        check = 0
        word = ""
        while check < Department.number_of_fields(self):
            word += Department.get_value(self, check)
            word += ", "
            check += 1
        return word

    def get_value(self, key):
        if self is None or key is None:
            return None
        else:
            number = 0
            for attribute, value in self.__dict__.items():
                if number == key:
                    #return value

                    if value is None:
                        return "None"
                    else:
                        return value

                else:
                    number += 1

    def set_value(self, value, key):
        if self is None or key is None:
            return None
        else:
            if value == "":
                value = "None"
            number = 0
            for attribute in self.__dict__.items():
                if number == Department.number_of_fields(self) - 1:
                    return None
                else:
                    if number == key:
                        name = str(attribute)
                        name = Department.get_name(self, name)
                        self.__dict__[name] = value
                        return self
                    else:
                        number += 1

    def create_new_elem(self, arr_add):
        if self is None or arr_add is None:
            return None
        else:
            while len(arr_add) != Department.number_of_fields(self):
                if len(arr_add) < Department.number_of_fields(self):
                    arr_add.append(None)
                else:
                    arr_add.pop(-1)
            check = 0
            while check < Department.number_of_fields(self):
                if arr_add[check] is None:
                    arr_add[check] = "None"
                Department.set_value(self, arr_add[check], check)
                check += 1
            x = Validator.Validate(self)
            y = Validator.Validate.main_validation(x)
            return y

    def number_of_fields(self):
        if self is None:
            return None
        else:
            fields = 0
            for attribute, value in self.__dict__.items():
                fields += 1
            return fields

    def get_name(self, name):
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

    def set_value_by_name(self, value, key):
        if key is None or self is None:
            return None
        else:
            if value == "":
                value = "None"
            number = 0
            for attribute in self.__dict__.items():
                name = str(attribute)
                name = Department.get_name(self, name)
                if name == key:
                    self.__dict__[key] = value
                    return self
                else:
                    number += 1
        return None

    def get_value_by_name(self, key):
        if key is None or self is None:
            return None
        else:
            for attribute, value in self.__dict__.items():
                if attribute == key:
                    if value is None:
                        return "None"
                    else:
                        return value
        return None



