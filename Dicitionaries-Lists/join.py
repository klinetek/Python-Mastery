my_list = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

"""Note that this acts as a for loop in Python3 whereas in P2 you had to have a
for loop to iterate over each point; not in Python3.  line 7 produces the same
result as a for loop with a simple .join() command."""

new_string = " mississippi, ".join(numbers)
print(new_string)

print("$" * 80)

locations ={0: "you are sitting in front of a computer learning python",
            1: "you are standing at the end of a road before a small brick building",
            2: "you are at the top of a hill",
            3: "You are inside a building, a well house",
            4: "You are in a valley beside a stream",
            5: " you are in a forest, dark and endless"}

exits =[{"Q": 0},
        {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
        {"N": 5, "Q": 0},
        {"W": 1, "Q": 0},
        {"N": 1, "W": 2, "Q": 0},
        {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    available_exits = ""
    for direction in exits[loc].keys():
        available_exits += direction + ", "
    print(locations[loc])

    if loc == 0:
        break
    direction = input("Available exits are " + available_exits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc] [direction]
    else:
        print("You cannot go that way.")
