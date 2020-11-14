def to_lover(word):
    if word is not None:
        word_arr = list(word)
        word = ""
        letter_word = "abcdefghilklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter_arr = list(letter_word)
        letter = 0
        while letter < len(word_arr):
            x = 0
            check = 0
            while check < len(letter_arr):
                if word_arr[letter] == letter_arr[check]:
                    x = 1
                    if check > 25:
                        word_arr[letter] = letter_arr[check - 26]
                    word += word_arr[letter]
                check += 1
            if x == 0:
                word += word_arr[letter]
            letter += 1
            return word
    else:
        word = "None"
        return word