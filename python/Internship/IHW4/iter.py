import List


class Iterator:
    def __iter__(self):
        return self

    def __init__(self, list):
        self.limit = List.LinkedList.return_end_val(list)
        self.counter = List.LinkedList.return_head(list)

    def __next__(self):
        if self.counter != self.limit:
            self.counter = List.LinkedList.return_next_val(list, self.counter)
            return List.LinkedList.return_date(list, self.counter)
        else:
            raise StopIteration
