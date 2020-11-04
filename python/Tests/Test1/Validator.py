class Validate:
    def __init__(self, valid=None):
        self.valid = valid

    def check_invalid_symbols(self):
        if str(type(self.valid)) == "<class 'str'>":
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

    def day_validation(self, month, year):
        if self.valid is not None and month is not None and year is not None:
            day = self.valid
            day = int(day)
            month = int(month)
            year = int(year)
            if month % 2 == 1:
                if 0 < day < 31:
                    return self.valid
                else:
                    return None
            elif month % 2 == 0:
                if 0 < day < 32:
                    return self.valid
                else:
                    return None
            elif month == 2:
                if year % 4 == 0:
                    if 0 < day < 30:
                        return self.valid
                    else:
                        return None
                else:
                    if 0 < day < 29:
                        return self.valid
                    else:
                        return None
            else:
                return None

    def month_validation(self):
        if self.valid is not None:
            month = self.valid
            month = int(month)
            if 0 < month < 13:
                return self.valid
            else:
                return None

    def year_validation(self):
        if self.valid is not None:
            year = self.valid
            year = int(year)
            if 0 < year < 2021:
                return self.valid
            else:
                return None
