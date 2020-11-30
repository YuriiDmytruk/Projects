class Validator:
    def __init__(self,new=None):
        self.new = new

    def check_number(self):
        word = str(self.new)
        word_arr = list(word)
        allowed_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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
                self.new = None
                break
            letter += 1
        return self.new