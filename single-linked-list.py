__author__ = 'mikeybadr'

class Node:
    next = None
    data = None

class SingleLinkedList:
    head = None

    def insert(self, obj):
        node = Node()
        node.data = obj

        def add(current, newNode):
            if not current.next:
                current.next = newNode
            else:
                add(current.next, newNode)

        if self.head == None:
            self.head = node
        else:
            add(self.head, node)


people = SingleLinkedList()
people.insert('bob')
people.insert('sara')
people.insert('alice')
people.insert('joe')

def print_linked_list(node):
    if node.next:
        print(node.data, 'then', node.next.data)
        print_linked_list(node.next)
    else:
        print(node.data)

print_linked_list(people.head)


print('Now lets print backwards!')


def print_linked_backwards(node):
    if not node.next:
        print(node.data)
    else:
        print_linked_backwards(node.next)
        print(node.data)

print_linked_backwards(people.head)




pass


