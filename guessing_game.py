import random

highest = 30
answer = random.randint(1,highest)
number_of_geusses = 5

print("Please guess a number between 1 and {}:".format(highest))
guess = int(input())
if guess == answer:
    print("wow you got it first try! look at you...")
else:
    if guess < answer:
        print("No, Higher this time...")
    else:
        print("No, Lower this time...")

    while number_of_geusses != 0:
        guess = int(input())
        if guess == answer:
            print("Now you got it!  Nice.")
            break
        else:
            number_of_geusses -= 1
            print("Nope, you have {} tries remaining".format(number_of_geusses))
            if guess < answer:
                print("No, Higher this time...")
            else:
                print("No, Lower this time...")
