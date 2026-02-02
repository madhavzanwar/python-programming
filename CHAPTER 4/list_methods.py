friends = ["shardul", "veer", 7, True, "sanakalp",69.00]
print(friends)

friends.append("Rahul")

#append = add at end
print(friends)

l1 = [1, 8, 7, 2, 21, 15]

#sort = Sorts the list in ascending order.
l1.sort() #dont forget ()
print(l1)

#reverse = Reverses the order of list.
l1.reverse()
print(l1)

#insert(index, value) = Adds element at specific index.
l1.insert(3, 8)
print(l1)

#pop = Removes AND returns value.
x = l1.pop(2)
print(l1)
print(x)

#remove = Removes that value.
l1.remove(21)
print(l1)
#pop() without index removes LAST element.


# 🎯 Quick Difference
# pop()

# ➡️ Uses index
# ➡️ Returns value

# remove()

# ➡️ Uses value
# ➡️ Returns nothing