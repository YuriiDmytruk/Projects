class Variable:
    def __init__(self, value=0, name="name", checked=0):
        self.value = value
        self.name = name
        self.checked = checked

    def print(self):
        if self.checked == 0:
            print(self.name, end=" ")
        else:
            self.value = int(self.value)
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


def matrix_print(x):
    check = 0
    while check < 3:
        stop = 0
        while stop < 3:
            Variable.print(x[check][stop])
            stop += 1
        print()
        check += 1
    print()


def multiplication(l, u, x, y, a):
    printm = Variable.print
    check = 0
    devide = 1
    c, h = 0, 0
    ans = Variable.get_value(a[x][y])
    while check < 3:
        if Variable.get_check(l[x][check]) == 0 or Variable.get_check(u[check][y]) == 0:
            if Variable.get_check(l[x][check]) == 0:
                devide = Variable.get_value(u[check][y])
            else:
                devide = Variable.get_value(l[x][check])
        else:
            if c == 0:
                c = Variable.get_value(u[check][y]) * Variable.get_value(l[x][check])
            else:
                h = Variable.get_value(u[check][y]) * Variable.get_value(l[x][check])
        check += 1
    check = 0
    while check < 3:
        if Variable.get_check(l[x][check]) == 0 or Variable.get_check(u[check][y]) == 0:
            if Variable.get_check(l[x][check]) == 0:
                if devide == 0:
                    devide = 1
                if x == 2 and y == 0:
                    devide = 3
                l[x][y] = Variable.set_value(l[x][check], (ans - c - h)/devide)
                break
            else:
                if devide == 0:
                    devide = 1
                u[x][y] = Variable.set_value(u[check][y], (ans - c - h)/devide)
                break
        check += 1
    return l, u


a11, a12, a13, a21, a22, a23, a31, a32, a33 = Variable(3, "a11", 1), Variable(-3, "a12", 1), Variable(-1, "a13", 1), \
                                              Variable(9, "a21", 1), Variable(-8, "a22", 1), Variable(-2, "23", 1), \
                                              Variable(-3, "a31", 1), Variable(2, "a32", 1), Variable(3, "a33", 1)
A = [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]

l11, l12, l13, l21, l22, l23, l31, l32, l33 = Variable(1, "l11", 1), Variable(0, "a12", 1), Variable(0, "a13", 1), \
                                              Variable(0, "l21", 0), Variable(1, "a22", 1), Variable(0, "23", 1), \
                                              Variable(0, "l31", 0), Variable(0, "l32", 0), Variable(1, "l33", 1)
L = [[l11, l12, l13], [l21, l22, l23], [l31, l32, l33]]

u11, u12, u13, u21, u22, u23, u31, u32, u33 = Variable(0, "u11", 0), Variable(0, "u12", 0), Variable(0, "u13", 0), \
                                              Variable(0, "u21", 1), Variable(0, "u22", 0), Variable(0, "u23", 0), \
                                              Variable(0, "u31", 1), Variable(0, "u32", 1), Variable(0, "u33", 0)
U = [[u11, u12, u13], [u21, u22, u23], [u31, u32, u33]]
print("Початкові матриці")
print("L = ")
matrix_print(L)
print("U = ")
matrix_print(U)
print("A = ")
matrix_print(A)

lenght = len(A)
check = 0
while check < lenght:
    stop = 0
    while stop < lenght:
        L, U = multiplication(L, U, check, stop, A)
        stop += 1

    check += 1

print("-------------------------------------")
print("Кінцеві матриці")
print("U")
matrix_print(U)
print("L")
matrix_print(L)
