import list

class Momento_main:
    def __init__(self, list=None):
        self.list = list

    def save(self, history):
        concrete = ConcreteMemento(self)
        CareTaker.set_originator(history, concrete)

    def get(self):
        return self.list


class ConcreteMemento:
    def __init__(self, momento):
        self.momento = momento

    def get(self):
        return self.momento

    def print_(self):
        list.LinkedList.list_print(Momento_main.get(self.momento))


class CareTaker:
    def __init__(self, originator=None):
        self.momentos = []
        self.originator = originator

    def save_to_history(self):
        self.momentos.append(self.originator)

    def set_originator(self, new):
        self.originator = new
        CareTaker.save_to_history(self)

    def show_history(self):
        list.LinkedList.list_print(Momento_main.get(ConcreteMemento.get(self.momentos[0])))
        print(Momento_main.get(ConcreteMemento.get(self.momentos[0])))
        print()
        list.LinkedList.list_print(Momento_main.get(ConcreteMemento.get(self.momentos[1])))
        print(Momento_main.get(ConcreteMemento.get(self.momentos[1])))
        print()

"""
class Momento:
    def __init__(self, list=None):
        self.list = list

    def get(self):
        return self


class ConcreteMemento:
    def __init__(self, memento=None):
        self.memento = memento

    def load(self):
        return self.memento

    def save(self, history):
        new = Momento(self)
        print(type(new))
        Caretaker.save_to_history(history, Momento.get(new))

    def get(self):
        return self.memento


class Caretaker:
    def __init__(self, originator=None):
        self.mementos = []
        self.originator = originator

    def save_to_history(self, new):
        self.mementos.append(new)

    def show_history(self):
        check = 0
        print("Full History")
        while check < len(self.mementos):
            list.LinkedList.list_print(ConcreteMemento.get(self.mementos[check]))
            print()
            check += 1
        print("--------------------")
        return self
"""