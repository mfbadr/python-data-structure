__author__ = 'mikeybadr'


class Queue1:
    data = []

    def enqueue(self, name):
        self.data.append(name)

    def dequeue(self):
        return self.data.pop(0)


pass
