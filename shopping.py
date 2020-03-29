shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

#for item in shopping_list:
#    if item != "spam":
#    print("Buy" + item)

for item in shopping_list:
    if item == "albus":
        continue
    print ("Buy " + item)

item_to_find = "albus"
found_at = None
for i in range (len(shopping_list)):
    if shopping_list[i] == item_to_find:
        found_at = i
        break
print("Item Found at position {}".format(found_at))
