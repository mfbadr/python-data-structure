__author__ = 'mikeybadr'
class Node:
    def __init__(self, name):
        self.name = name
        self.previous = None
        self.next = None

class BinaryTree:
    head = None

    def insert_helper(self, current, newNode):
        if not current:
            self.head = newNode
        elif current.name > newNode.name:
            if current.previous:
                self.insert_helper(current.previous, newNode)
            else:
                current.previous = newNode
        elif current.name < newNode.name:
            if current.next:
                self.insert_helper(current.next, newNode)
            else:
                current.next = newNode

    def insert(self, obj):
    #TODO: check if inserting a duplicate
        self.insert_helper(self.head, Node(obj))

names = BinaryTree()
names.insert('mikey')
names.insert('alice')
names.insert('xander')
names.insert('bob')
names.insert('frank')
names.insert('joe')
names.insert('suzy')
names.insert('nancy')

pass

def binary_tree_printer(node):
    if node.previous:
        binary_tree_printer(node.previous)
    print(node.name)
    if node.next:
        binary_tree_printer(node.next)








binary_tree_printer(names.head)


pass


'''

how to insert a new entry into a binary tree

is there a current node? if no, make it current node (start with head)
    if yes, compare to current node
    if before, is there a previous?
        if no make it the previous
        if yes, iterate on previous
    if after, is there a next?
        if no, make it the next
        if no, iterate on next
'''
