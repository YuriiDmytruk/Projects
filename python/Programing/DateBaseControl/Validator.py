class Validate:
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def main_valid(self):
        if self.name is not None and self.email is None:
            self.name = Validate.valid_name(self)
        elif self.name is None and self.email is not None:
            self.email = Validate.valid_email(self)
        else:
            self.name = Validate.valid_name(self)
            self.email = Validate.valid_email(self)
        return self.name, self.email

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
