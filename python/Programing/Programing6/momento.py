import list


class ConcreteMemento:
    def __init__(self, memento=None):
        self.memento = memento

    def load(self):
        return self.memento

    def save(self, history):
        Caretaker.save_to_history(history, self)

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
        while check < len(self.mementos):
            list.LinkedList.list_print(ConcreteMemento.get(self.mementos[check]))
            print()
            check += 1
        return self
