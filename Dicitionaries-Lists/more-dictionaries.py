fruit = {"orange": "a sweet, orange, citrus fruit",
        "apple": "good for making cider",
        "lemon": "a sour, yellow citrus fruit",
        "grape": "a small, sweet fruit growing in bunches",
        "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
        "sprouts": "mmmm, lovely",
        "spinach": "no thank you"}
print(veg)
print("-" * 80)
#update() appends the dict based on your input
veg.update(fruit)
print(veg)
print("-" * 80)

nice-and-nasty = fruit.copy()
