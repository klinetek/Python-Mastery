fruit = {"orange": "a sweet, orange, citrus fruit",
        "apple": "good for making cider",
        "lemon": "a sour, yellow citrus fruit",
        "grape": "a small, sweet fruit growing in bunches",
        "lime": "a sour, green citrus fruit"}
"""#adding another key of the same name will update the original key to what you
#wrote it is in the latest update, remember Python goes line by line so the final
#entry is the one it will keep
print("*" *79)
print(fruit["lemon"])
#keys must be imutable
#you can add a key by declairing the dictionary and referencing a key that doesnt
#exist yet and it will add it a that point in the program.
fruit["pear"] = "an odd shaped apple"
print (fruit)
#del deletes whatever you choose including the whole varaible if you're not specific
del fruit["lemon"]
print(fruit)
#if you want to empty a dictionary you would use .clear and that empties it
fruit.clear()
print(fruit)
fruit["lime"] = "great with Tequila"
print("*"*79)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)"""
print("*"*79)
#as you'd imagine you can it over the diction in typical fashion.
"""for i in range(3):
    for f in fruit:
        print(f + " is " + fruit[f])
    print('-' * 80)"""
#remember, using sorted creates a new object and is no longer the original.
#alt you could use a .sort() func, this modifies the original obj.
print(fruit)
for f in sorted(fruit.keys()):
    print(f + " = " + fruit[f])
#you can also dump the dictionary into a tuple!
fruit_tuple = tuple(fruit.items())
print(fruit_tuple)
#of course you can it over this in natural fashion
for f in fruit_tuple:
    item, description = f
    print(item + " is "+ description)
#you could invert this and put a dictionary in a tuple as well using a dict() func
print(dict(fruit_tuple))
