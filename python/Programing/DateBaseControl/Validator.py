class Validate:
    def __init__(self, name=None, email=None, int=None):
        self.name = name
        self.email = email
        self.int = int

    def main_valid(self):
        self.name = Validate.valid_name(self)
        self.email = Validate.valid_email(self)
        self.int = Validate.valid_int(self)
        return self.name, self.email, self.int

    def valid_name(self):
        if self.name is not None:
            symbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
            x = allowed_symbols(self.name, symbols)
            self.name = x
        else:
            return None
        return self.name

    def valid_email(self):
        if self.email is not None:
            symbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_@.1234567890"
            x = allowed_symbols(self.email, symbols)
            self.email = x
        else:
            return None
        return self.email

    def valid_int(self):
        if self.int is not None:
            symbols = "1234567890"
            x = allowed_symbols(self.int, symbols)
            self.int = x
        else:
            return None
        return self.int


def allowed_symbols(word, allow_symbols):
    word = str(word)
    word_arr = list(word)
    allowed_arr = list(allow_symbols)
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
