class Queue:
    def __init__(self):
        self.items = []
        self.boards = []

    def show(self):
        print(self.items)

    def put(self, item):
        self.boards.insert(0, item.board)
        self.items.insert(0, item)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def instances(self, item):
        return self.boards.count(item.board)

    def push(self):
        a = []
        for x in self.items:
            a.append(x.priority)
        min_index = a.index(min(a))
        return self.items.pop(min_index)

    def __getitem__(self, item):
        return self.items[item]
