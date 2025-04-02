import collections
l=[11,22,33,44]
deque=collections.deque(l)
#adding
deque.append(55)
print(deque) #deque([11, 22, 33, 44, 55])
deque.appendleft(100)
print(deque) #deque([100, 11, 22, 33, 44, 55])

#poping 
deque.pop()
print(deque) #deque([100, 11, 22, 33, 44])
deque.popleft()
print(deque)#deque([11, 22, 33, 44])

