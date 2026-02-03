# Can you write a version that prints:
# input : 23,25,25,10
# Largest is 25 and smallest is 10 and how many times did that appreared

a = 23
b = 25
c = 25
d = 10

nums = [a,b,c,d]

largest = max(nums)
smallest = min(nums) 
count = nums.count(largest)
count1 = nums.count(smallest) 

print("Largest is", largest, "and it appears", count, "times")
print("Smallest is",smallest,"and it apprears",count1,"times") 
