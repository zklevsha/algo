"""
• Data can be inserted only at the end of a queue. (This is identical behavior
to the stack.)
• Data can be deleted only from the front of a queue. (This is the opposite
behavior of the stack.)
• Only the element at the front of a queue can be read. (This, too, is the
opposite of behavior of the stack.
"""


class Queue():
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data = self.data + [value]

    def read(self):
        try:
            return self.data[0]
        except IndexError:
            return None

    def get(self):
        try:
            value = self.data[0]
        except IndexError:
            return None
        self.data = self.data[1:]
        return value

    def list(self):
        return self.data


def test():
    queue = Queue()
    value = queue.get()
    assert value == None
    queue.add(1)
    queue.add(2)
    assert queue.list() == [1, 2]
    value = queue.read()
    assert value == 1
    value = queue.get()
    assert value == 1
    assert queue.list() == [2]
