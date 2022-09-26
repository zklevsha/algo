class Stack():
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data = self.data + [value]

    def pop(self):
        if len(self.data) == 0:
            return None
        value = self.data[-1]
        self.data = self.data[:-1]
        return value

    def list(self):
        return self.data


def test():
    stack = Stack()
    assert stack.pop() == None
    stack.push(1)
    assert stack.list() == [1]
    stack.pop()
    assert stack.list() == []
