class Itor:
    def __init__(self, limit) -> None:
        self.limit = limit
        self.prev = 0
        self.curr = 1
        self.n = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.limit:
            result = self.prev + self.curr
            self.prev = self.curr
            self.curr = result
            self.n += 1
            return result
        else:
            raise StopIteration
            exit

ob = Itor(10)
for i in ob:
    try:
        print(ob.__next__())
    except StopIteration:
        break
    


