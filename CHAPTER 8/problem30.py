#Write a python function to remove a given word from a list ad strip it at the same
#time.

def remove_word(lst, word):
    new_list = []

    for item in lst:
        if item.strip() != word:
            new_list.append(item.strip())

    return new_list


words = ["apple", " banana ", "mango", "banana"]

print(remove_word(words, "banana"))

'''
Loop list
Remove spaces
If word matches → skip
Else → keep

'''