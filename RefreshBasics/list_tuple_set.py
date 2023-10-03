l = [1, 2, 3]
# tuples cannot be modified after they are created
t = (1, 2, 3)
s = {1, 2, 3, 4}

print(l[0])
print(t[1])

l[0] = 2
print(l[0])
l.append(4)
l.remove(2)
print(l)
print(l[-1:])
