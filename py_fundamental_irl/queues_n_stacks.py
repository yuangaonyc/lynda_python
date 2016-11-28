# Queues and Stacks
import queue
# Queues
q = queue.Queue(2)
print(q.empty())
q.put('bag1')
print(q.empty())
print(q.full())
q.put('bag2')
print(q.empty())
print(q.full())
# q.put_nowait('bag3') # gives an error cuz queue is full
# q.put('bag3') # will keep the program waiting until an available spot
print(q.get())
print(q.get())
# q.get_nowait() # gives an error cuz queue is empty
# q.get() # will keep the program waiting until an available next item
print(" ")

# Stacks
stack = list()
stack.append('bill1')
stack.append('bill2')
print(stack.pop())
stack.append('bill3')
stack.append('bill4')
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.pop()) # gives an error cuz list is empty

