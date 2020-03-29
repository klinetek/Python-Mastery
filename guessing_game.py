import random

highest = 10
answer = random.randint(1,highest)

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("wow you got it first try! look at you...")
else:
    if guess < answer:
        print("guess a little higher thist time")
    else:
        print("guess just a bit lower")
    guess = int(input())
    if guess == answer:
        print("Now you got it!  Nice.")
    else:
        print("Sorry, you're all out of tries bud.  Time to die. ")
