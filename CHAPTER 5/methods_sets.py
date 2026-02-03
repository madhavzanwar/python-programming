# add() — adds one element
# update() — adds multiple elements
# remove() — removes element (error if missing)
# discard() — removes element (no error)
# pop() — removes random element
# clear() — empties set
# union() — combines sets
# intersection() — common values
# difference() — values in first not second
# issubset() — checks subset

#problems:
print({1,2,2,3})
a = {1,2,3,4}
b = {3,4,5,6}
c = {4,5,6,7}

print((a & b) | (b & c))


p = {1,2,3}
q = {2,3,4}
r = {3,4,5}

print((p | q) & (q | r))
t = r.pop() #remove random element
print(t)

