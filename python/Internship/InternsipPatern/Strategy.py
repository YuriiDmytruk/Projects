from __future__ import annotations
from abc import ABC, abstractmethod
import List
import Validator
import os.path

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def full_list(self, my_list):
        return self._strategy.do_algorithm(my_list)


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, my_list):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, my_list):
        my_list = ConcreteStrategyA.set_list(self, my_list)
        return my_list

    def set_list(self, my_list):
        print("Input Number of fields:", end=" ")
        number = None
        while number is None:
            number = input()
            z = Validator.Validator(number)
            z = Validator.Validator.check_number(z)
            if z is not None:
                number = int(number)
            else:
                print("Value should be integer")
        check = 0
        while check < number:
            print("Input id:", end=" ")
            i_d = input()
            print("Input value:", end=" ")
            value = input()
            print()
            x = Validator.Validator(i_d)
            Validator.Validator.check_number(x)
            if x is not None:
                i_d = int(i_d)
                List.LinkedList.insert(my_list, i_d, value)
            else:
                print("Value should be integer")
            check += 1
        return my_list


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, my_list):
        my_list = ConcreteStrategyB.set_list(self, my_list)
        return my_list

    def set_list(self, my_list):
        arr = ConcreteStrategyB.read_from_file(self)
        check = 0
        while check < len(arr):
            my_list = List.LinkedList.insert(my_list, int(arr[check][0]), arr[check][1])
            check += 1
        return my_list

    def read_from_file(self):
        arr_main = []
        arr_add = [0, 0]
        file = open(file_name, "r")
        for line in file:
            word = ""
            for letter in line:
                if letter == ';':
                    arr_add[1] = word
                    arr_main.append(arr_add)
                    arr_add = [0, 0]
                    word = ""
                elif letter == ".":
                    arr_add[0] = word
                    word = ""
                else:
                    word += letter
        file.close()
        return arr_main


def text_check():
    name = ""
    print("Insert File name")
    x = 0
    while x == 0:
        name = input()
        if os.path.isfile(name):
            x = 1
        else:
            x = 0
            print("File not exist")
    return name


def text_start():
    global file_name
    #name = text_check()
    file_name = "Text.txt"
