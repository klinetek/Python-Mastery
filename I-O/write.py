# cities = ["adelaide", "Alice springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)
#the = symbol should not have any spaces around it when assigning a filename

# cities = []
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))#<--removes the \n from the print
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
# with open("Imelda3.txt", 'w')as ifile:
#     print(imelda, file=ifile)
"""using eval can be damaging to your file so there are better methods just in
case you manage to damage something in your file but if you wanted to this would
be how you would get on with that"""
with open("Imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda= eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
