#List in python are one of the most versatile and commanly used data structure.
#They allow ypu to store collections of items in an orderd and mutable format.
# This makes lists ideal for various applications, from simple scripts to complex data manipulation tasks.
#example:1
l = [10, 20, 30, 40, 50]
print(l)
print(l[3])
print(l[-1])
print(l[-2])

#insert and search function
#example:2
l = [10, 20, 30, 40, 50]
l. append(30)
print(l)
l.insert(1, 15)
print(l)
print(15 in l)
print(l.count(30))
print(l.index(30))
print(l.index(30, 4, 7))

#removal of items
#example:3
l =[10, 20, 30, 40, 50, 60, 70, 80]
l.remove(20)
print(l)
print(l.pop())
print(l)
print(l.pop(2))
print(l)
del l[1]
print(l)
del l[0:2]
print(l)


#some general purpose
#functions
#example:4
l = [10, 40, 20, 50]
print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)