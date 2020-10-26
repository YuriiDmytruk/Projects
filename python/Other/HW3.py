import math
class Variable:
    def __init__(self, value=0.0, name="name", checked=0.0):
        self.value = value
        self.name = name
        self.checked = checked

    def print(self):
        if self.checked == 0:
            print(self.name, end=" ")
        else:
            print(self.value, end=" ")

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_check(self):
        return self.checked

    def set_value(self, value):
        self.value = value
        self.checked = 1
        return self


def round_number(number):
    word_number = str(number)
    word_number_arr = list(word_number)
    full = ""
    check = 0
    while word_number_arr[check] != '.':
        full += word_number_arr[check]
        check += 1
    if check < len(word_number_arr):
        full += '.' + word_number_arr[check + 1]
        check += 1
    if check < len(word_number_arr) - 1:
        full += word_number_arr[check + 1]
    number = float(full)
    return number


def matrix_print(x):
    check = 0
    while check < len(x):
        stop = 0
        while stop < len(x):
            Variable.print(x[check][stop])
            stop += 1
        print()
        check += 1
    print()


def first(u, x, a):
    help = Variable.get_value(a[x][x])
    check = 0
    while check < x:
        help -= Variable.get_value(u[check][x]) ** 2
        check += 1
    if help > 0:
        help = math.sqrt(help)
        Variable.set_value(u[x][x], help)
    else:
        return u, 0
    if len(u) == 3:
        if x == 0:
            check = 1
            while check < 3:
                help = Variable.get_value(a[x][check]) / Variable.get_value(u[x][x])
                Variable.set_value(u[x][check], help)
                check += 1
        if x == 1:
            help = Variable.get_value(a[1][2]) - Variable.get_value(u[0][1]) * Variable.get_value(u[0][2]) /\
                   Variable.get_value(u[1][1])
            Variable.set_value(u[1][2], help)
    elif len(u) == 4:
        if x == 0:
            check = 1
            while check < len(u):
                help = Variable.get_value(a[x][check]) / Variable.get_value(u[x][x])
                Variable.set_value(u[x][check], help)
                check += 1
        if x == 1:
            help = (Variable.get_value(a[1][2]) - (Variable.get_value(u[0][1]) * Variable.get_value(u[0][2]))) /\
                   Variable.get_value(u[1][1])
            Variable.set_value(u[1][2], help)
            help = (Variable.get_value(a[1][3]) - (Variable.get_value(u[0][1]) * Variable.get_value(u[0][3]))) /\
                   Variable.get_value(u[1][1])
            Variable.set_value(u[1][3], help)
        if x == 2:
            help = (Variable.get_value(a[2][3]) - Variable.get_value(u[0][2]) * Variable.get_value(u[0][3]) -\
                    Variable.get_value(u[1][2]) * Variable.get_value(u[1][3])) / Variable.get_value(u[2][2])
            Variable.set_value(u[2][3], help)
    else:
        print("size error")
    return u, 1


def second(u, ut):
    if len(u) == 3:
        ut = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    else:
        ut = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    check = 0
    while check < len(u):
        stop = 0
        while stop < len(u):
            ut[stop][check] = u[check][stop]
            stop += 1
        check += 1
    return ut


a11, a12, a13, a21, a22, a23, a31, a32, a33 = Variable(1.63, "a11", 1), Variable(1.27, "a12", 1), Variable(-0.84, "a13", 1), \
                                              Variable(1.27, "a21", 1), Variable(0.65, "a22", 1), Variable(1.27, "a23", 1), \
                                              Variable(-0.84, "a31", 1), Variable(1.27, "a32", 1), Variable(-1.21, "a33", 1)
A = [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]


u11, u12, u13, u21, u22, u23, u31, u32, u33 = Variable(0, "u11", 0), Variable(0, "u12", 0), Variable(0, "u13", 0), \
                                              Variable(0, "u21", 1), Variable(0, "u22", 0), Variable(0, "u23", 0), \
                                              Variable(0, "u31", 1), Variable(0, "u32", 1), Variable(0, "u33", 0)
U = [[u11, u12, u13], [u21, u22, u23], [u31, u32, u33]]

print("Початкова матриця")
print("A = ")
matrix_print(A)

print("-------------------------------------")
check = 0
while check < len(A):
    U, error = first(U, check, A)
    if error == 0:
        print("sqrt(-) eror")
        break
    check += 1
print("Матриця U  після першого кроку:")
matrix_print(U)

Ut = []
print("Матриця Ut")
Ut = second(U, Ut)
matrix_print(Ut)

print("Розвязок для матриці:")
b11, b12, b13, b14, b21, b22, b23, b24, b31, b32, b33, b34, b41, b42, b43, b44 =\
    Variable(4, "b11", 1), Variable(2, "b12", 1),\
    Variable(2, "b13", 1), Variable(1.0, "b14", 1), \
    Variable(2, "b21", 1), Variable(5, "b22", 1), \
    Variable(1.0, "b23", 1), Variable(2, "b24", 1), \
    Variable(2, "b31", 1), Variable(1, "b32", 1),\
    Variable(5, "b33", 1), Variable(1, "b34", 1), \
    Variable(1, "b41", 1), Variable(2, "b42", 1), \
    Variable(1, "b43", 1), Variable(4.875, "b44", 1)
B = [[b11, b12, b13, b14], [b21, b22, b23, b24], [b31, b32, b33, b34], [b41, b42, b43, b44]]

l11, l12, l13, l14, l21, l22, l23, l24, l31, l32, l33, l34, l41, l42, l43, l44 = \
    Variable(0, "l11", 0), Variable(0, "l12", 0),\
    Variable(0, "l13", 0), Variable(0, "l14", 0), \
    Variable(0, "l21", 1), Variable(0, "l22", 0), \
    Variable(0, "l23", 0), Variable(0, "l24", 0), \
    Variable(0, "l31", 1), Variable(0, "l32", 1),\
    Variable(0, "l33", 0), Variable(0, "l34", 0), \
    Variable(0, "l41", 1), Variable(0, "l42", 1), \
    Variable(0, "l43", 1), Variable(0, "l44", 0)
L = [[l11, l12, l13, l14], [l21, l22, l23, l24], [l31, l32, l33, l34], [l41, l42, l43, l44]]
matrix_print(B)
print("-------------------------------------")
check = 0
while check < len(B):
    L, error = first(L, check, B)
    if error == 0:
        print("sqrt(-) eror")
        break
    check += 1
print("Матриця U  після першого кроку:")
matrix_print(L)
Lt = []
print("Матриця Ut")
Lt = second(L, Lt)
matrix_print(Lt)

