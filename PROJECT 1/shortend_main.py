import random

# 1 = Snake, -1 = Water, 0 = Gun
comp = random.choice([-1, 0, 1])

choice = input("Enter your choice (s/w/g): ")

map_in = {"s": 1, "w": -1, "g": 0}
map_out = {1: "Snake", -1: "Water", 0: "Gun"}

user = map_in[choice]

print(f"You chose {map_out[user]}")
print(f"Computer chose {map_out[comp]}")

if comp == user:
    print("It's a draw")

else:
    if (comp - user) == -1 or (comp - user) == 2:
        print("You lose!")
    else:
        print("You win!")
