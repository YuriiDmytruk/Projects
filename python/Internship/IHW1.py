def options(n):
    N = n
    options_number = 0
    num_of_field = 0

    z = n - 1
    stop = 0
    num_of_field = 0
    while stop < z:
        num_of_field += n + stop
        stop += 1
    num_of_field *= 2
    num_of_field += n + stop

    num_of_extreme_fields = (n - 2) * 6 + 6
    num_of_normal_fields = num_of_field - num_of_extreme_fields
    options_number += num_of_normal_fields * 3

    num_of_triple_fields = (n - 2) * 2
    options_number += num_of_triple_fields * 3

    num_of_double_fields = (n - 1) * 2
    options_number += num_of_double_fields * 2

    num_of_one_fields = (n - 1) * 2
    options_number += num_of_one_fields
    return options_number + 3


N = int(input("N = "))
x = options(N)

print(x)

