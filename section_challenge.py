#the goal of this ecxorsize is to allow the user to choose an input from 1-9 in
#the console and have the program loop until the user choses 0 as an option.
#show the value chosen with replacement fields when they choose a viable option

choice = "~"
while choice != "0":
    if choice in "12345":
        print("You chose option {}".format(choice))
    else:
        print("what would you like to do? ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tLearn Unity3D")
        print("4:\tLearn Music")
        print("5:\tLearn Astrophysics")
        print("0:\tExit")

    choice = input()
