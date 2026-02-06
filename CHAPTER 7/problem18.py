#if name starts with "M" greet them otherwise not

t = {"Madhav", "Madhubala", "veer", "sankalp", "maisha", "mayuresh", "mumma", "shardul"}

for name in t:
    if name.startswith(("M", "m")):
        print(f"Hello {name}")

'''
alt - 
for name in t:
    if name.lower().startswith("m"):
        print(f"Hello {name}")
'''