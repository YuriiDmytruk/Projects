import Class


class Validate:
    def __init__(self, valid=None, date=None):
        self.valid = valid
        self.date = date

    def main_validation(self):
        for attribute in self.valid.__dict__.items():
            name = str(attribute)
            name = Class.Department.get_name(self.valid, name)
            arr = ret_arr(name)
            Validate.controler(self, arr, name)
        return self.valid

    def controler(self, arr, name):
        self.date = Class.Department.get_value_by_name(self.valid, name)
        arr_check = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+()-."
        self.date = allowed_symbols(self.date, arr_check)
        if self.date is not None:
            self.date = allowed_symbols(self.date, arr)
        Class.Department.set_value_by_name(self.valid, self.date, name)


def ret_arr(name):
        if name == "id":
            result = "0123456789"
        elif name == "title" or name == "director_name":
            result = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif name == "phone_number":
            result = "0123456789()+-"
        elif name == "monthly_budget" or name == "yearly_budget":
            result = "0123456789."
        elif name == "website_url":
            result = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."
        else:
            result = ""
        return result


def first_step(func):
    def outer(word, arr):
        result = func(word, arr)
        return result
    return outer


@first_step
def allowed_symbols(word, arr):
    word = str(word)
    word_arr = list(word)
    allowed_arr = list(arr)
    letter = 0
    while letter < len(word_arr):
        x = 0
        allow = 0
        while allow < len(allowed_arr):
            if allowed_arr[allow] == word_arr[letter]:
                x = 1
                break
            allow += 1
        if x != 1:
            word = None
        letter += 1
    return word
