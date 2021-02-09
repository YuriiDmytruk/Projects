import list


class Momento:
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


class CareTaker:
    def __init__(self, originator=None, iter=0):
        self.momentos = []
        self.originator = originator
        self.iter = iter

    def save_to_history(self):
        self.momentos.append(self.originator)

    def set_originator(self, new):
        self.originator = new
        CareTaker.set_iter(self)
        CareTaker.save_to_history(self)

    def show_history(self):
        print("Full History:")
        check = 0
        while check < len(self.momentos):
            print(check + 1, ":")
            list.LinkedList.list_print(Momento.get(ConcreteMemento.get(self.momentos[check])))
            print()
            check += 1
        print("-------------")

    def set_iter(self):
        if len(self.momentos) > 0:
            self.iter = len(self.momentos)
        else:
            self.iter = None

    def get_len(self):
        return len(self.momentos)

    def undo(self):
        if self.iter != 0:
            self.iter -= 1
            return Momento.get(ConcreteMemento.get(self.momentos[self.iter]))
        else:
            return None

    def redo(self):
        if len(self.momentos) > 0:
            if self.iter != len(self.momentos) - 1:
                self.iter += 1
                return Momento.get(ConcreteMemento.get(self.momentos[self.iter]))
            else:
                return None
        else:
            return None