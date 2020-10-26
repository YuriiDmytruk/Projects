def multiplication_array_on_number(array1, array2, x):
    check = 0
    while check < len(array1):
        array1[check] += array2[check] * x
        check += 1
    return array1


def print_all(array1, array2, array3, array4):
    print(array1)
    print(array2)
    print(array3)
    print(array4)


def main(array1, array2, array3, array4):
    print("Початкова матриця")
    print_all(array1, array2, array3, array4)
    multiplication_array_on_number(array2, array1, -2)
    multiplication_array_on_number(array3, array1, -2)
    multiplication_array_on_number(array4, array1, -3)
    print("Матриця після першого додавання")
    print_all(array1, array2, array3, array4)

    multiplication_array_on_number(array3, array2, 4)
    multiplication_array_on_number(array4, array2, -1)
    print("Матриця після другого додавання")
    print_all(array1, array2, array3, array4)

    z = array4[4] / array4[2]
    t = array3[4] - (array3[2] * z)
    y = (array2[4] * (-1)) - t
    x = array1[4] - (array1[1] * y) - (2 * array1[2]) - t
    print()
    print("z = ", array4[4], "/", array4[2])
    print("t =", array3[4], " - ", "(", array3[2], " *  z)")
    print("y = (", array2[4], " * (-1)) - t")
    print("x = ", array1[4], " - (", array1[1], " * y) - (2 * ", array1[2], ") - t")
    print()
    print("x =", x, "; y =", y, "; z =", z, "; t =", t)


arr1 = [1, 3, 2, 1, 11]
arr2 = [2, 5, 4, 1, 20]
arr3 = [2, 10, 9, 7, 40]
arr4 = [3, 8, 9, 2, 37]

main(arr1, arr2, arr3, arr4)


