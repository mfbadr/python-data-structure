__author__ = 'mikeybadr'

from que import *
from stack import *
from recursion import *



food1 = Queue1()
food1.enqueue('pizza')
food1.enqueue('hot dogs')
food1.enqueue('sushi')

food1.dequeue()

pass


food = Stack()
food.push('burgers')
food.push('fries')
food.push('cake')
food.pop() #remove cake

pass

print(fact(5))

print('fib(5) evals to ',fib(5), '(should be 5)')
print('fib(8) evals to ',fib(8), '(should be 21)')
print('fib(7) evals to ',fib(7), '(should be 13)')
print('fib(25) evals to ',fib(25), '(should be 75025)')

for x in range(20):
    print('fib({0}) = {1}'.format(x, fib(x)))