#lets you assign a value inside an expression

# n = len([1,2,3,4,5])

# if n > 3:
#     print(n)

#better approach - 

if (n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n})")

#assign AND use value at same time
#It avoids calculating the same thing twice.