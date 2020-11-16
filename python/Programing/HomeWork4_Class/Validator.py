class Validate:
    def __init__(self, valid=None):
        self.valid = valid

    def check_invalid_symbols(self):
        allowed_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+()-."
        word_arr = list(self.valid)
        allowed_arr = list(allowed_symbols)
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
                return None
            letter += 1
        return self.valid
