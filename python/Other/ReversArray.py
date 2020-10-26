word = "Я люблю програмувати"
print(word)


word_arr = list(word)
print(word_arr)


check = len(word_arr) - 1
reverse_word_arr = []
while check > -1:
    reverse_word_arr.append(word_arr[check])
    check -= 1

print(reverse_word_arr)

check = 0
revers_word = ""
while check < len(reverse_word_arr):
    revers_word += reverse_word_arr[check]
    check += 1

print(revers_word)
