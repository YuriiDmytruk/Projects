def print_matrix(mat, x):
    check = 0
    while check < x:
        print(mat[check])
        check += 1


def main(mat, x):
    check = 0
    counter = 1
    while check < x:
        array = []
        if check == (x - 1) / 2:
            stop = 0
            while stop < x:
                if stop == (x - 1) / 2:
                    array.append((x // 2) + 1)
                else:
                    array.append(0)
                stop += 1

        elif check < (x - 1) / 2:
            stop = 0
            minus  = -1
            while stop < x:
                if stop == check or stop == x - check - 1:
                    array.append(check + 1)
                else:
                    array.append(0)
                stop += 1

        elif check > (x - 1) / 2:
            stop = 0
            while stop < x:
                if stop == check or stop == x - check - 1:
                    array.append((x // 2) + 1 - counter)

                else:
                    array.append(0)
                stop += 1
            counter += 1
        mat.append(array)
        check += 1
    return mat


matrix = []
check = 0
while check == 0:
    N = int(input("N = "))
    if N > 0 and N % 2 == 1:
        check = 1
    else:
        print("N має бути більше 0 і непарне")
        check = 0
main(matrix, N)
print_matrix(matrix, N)
