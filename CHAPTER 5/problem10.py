#in python programming 1==1.0 is TRUE

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)
print(len(s))#the length displayed will be 2 instead of 3