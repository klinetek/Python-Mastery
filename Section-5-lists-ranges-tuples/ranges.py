my_list = (range(10))
print(my_list)


my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0,10)
print(small_decimals)

print(small_decimals.index(3))

decimals = range(0,100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('='*40)

for i in range(3,40,3):
    print(i)

r = range(0,100)
for i in r[::2]:
    print(i)
