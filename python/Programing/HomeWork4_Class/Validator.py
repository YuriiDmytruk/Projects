class Validate:
    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key

    def main_validation(self):
        arr = ret_arr(self.key)
        self.value = Validate.controler(self, arr)
        return self.value

    def controler(self, arr):
        arr_check = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+()-."
        self.value = allowed_symbols(self.value, arr_check)
        if self.value is not None:
            self.value = allowed_symbols(self.value, arr)
        return self.value


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
