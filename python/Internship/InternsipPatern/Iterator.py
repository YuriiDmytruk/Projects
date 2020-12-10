class Iterator:
    def __iter__(self):
        return self

    def __init__(self, start=0, num=0):
        self.limit = start + num
        self.counter = start

    def get_arr(self):
        arr = []
        while self.counter != self.limit:
            arr.append(self.counter)
            self.counter += 1
        return arr



