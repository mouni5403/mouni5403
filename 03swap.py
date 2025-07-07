# swap two variables in python
# example:1
x = 100
y = 200
temp = x
x = y
y = temp
print(x)
print(y)

#using comma assignment
#example:2
x = 100
y = 200
x,y = y,x
print(x)
print(y)

#using comma assign multiple values & multiple variables
#example:3
x, y, z = 100, "mouni", 10.5
print(x, y, z)
x, y = x-5, y
print(x)
print(y)


 