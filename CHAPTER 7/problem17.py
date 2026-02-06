#print multiplication table using for loop

n = int(input("Enter a number:"))

for i in range(1, 11): #11 tak likhoge tab 10 tak print hoga
    print(f"{n} X {i} = {n * i}") #using f string It lets you put variables directly inside a string.

#f string syntax : f"some text {variable}"
#The f tells Python:
# “Evaluate what’s inside {}”

#with WHILE LOOP - 

i = 1
while(i<11):
    print(f"{n} X {i} = {n * i}")
    i += 1