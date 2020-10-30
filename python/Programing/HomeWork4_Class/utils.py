def to_lover(word):
    word_arr = list(word)
    word = ""
    letter_word = "abcdefghilklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_arr = list(letter_word)
    letter = 0
    while letter < len(word_arr):
        check = 0
        while check < len(letter_arr):
            if word_arr[letter] == letter_arr[check]:
                if check > 25:
                    word_arr[letter] = letter_arr[check - 26]
                word += word_arr[letter]
            check += 1
        letter += 1
    return word