from collections import deque

lst = ['b','h','u','p','e','n','d','r','a']
dq = deque(lst)
print(dq)

dq.append('13')
print(dq)

dq.appendleft('Mr')
print(dq)

dq.popleft()
print(dq)

