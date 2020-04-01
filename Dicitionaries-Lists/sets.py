"""Sets, like dictionaries have immutable keys that are hashed"""
farm_animals = {"sheep", "cow", "hen"}

for animal in farm_animals:
    print(animal)
print("-" * 80)
wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)
for animal in wild_animals:
    print(animal)
print("-" * 80)
farm_animals.add("horse")
wild_animals.add("horse")
print("-" * 80)
empty_set = set()
even = set(range(0, 40, 2))
#remember this isn't in order.. it will still do it though.  but because it's a
#set it won't print it in order. you would have to sort it after if you wanted that.
print(even)
print("-" * 80)
squares_tuple = (4, 6, 9, 16, 25)
squares= set(squares_tuple)
print(squares)
print("-" * 80)
print(even.union(squares))
print(len(even.union(squares)))
print(squares.union(even))
print("-" * 80)
#you can also display the intersecting members only if you like with intersection
print(even.intersection(squares))
print(even & squares)  """either prints the same thing"""
"""subtracting set b from set a removes anything from set b in set a"""
