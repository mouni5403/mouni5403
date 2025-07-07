# A tuple is a collection of items that are ordered and unchangeble.
# tuples are defined by enclosing the items in parantheses().
#example:1
t = (10, 20, "mouni")
print(t)
t = ()
print(type(t))
print(t)
t = 10
print(type(t))
t = 10,
print(type(t))

# To create a tuple without smalle parantheses()
#example:2
t = 10, 20, 30, 40, 10
print(t[2])
print(t[-1])
print(t[1:3])
print(len(t))
print(t.count(10))
print(t.index(20))


# Handling mixed data types
#example:3
nested_tuple = (10,'mouni',(1, 2, 3))
print(nested_tuple[2])
print(nested_tuple[2][1])