parrot_list = ["non pinin","no more","a stiff","bereft of life"]

parrot_list.append("ANOTHERFUCKINGPARROT")

for state in parrot_list:
    print("This parrot is " + state)
print("="*79)
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
numbers.sort() #this does not make a new object it modfies the numbers obj
print(numbers)
print("|"*80)

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

print(menu)
