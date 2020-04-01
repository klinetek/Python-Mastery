cities = ["adelaide", "Alice springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)
#the = symbol should not have any spaces around it when assigning a filename
