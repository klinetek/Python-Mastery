low = 1
high = 1000
guess = 1
actual_guesses = 1
print("I am going to guess your number. Think of a number between {} and {}".format(low, high))
input("When youre ready, press the enter Key and Ill start.")

while True:
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. Should i guess higher or lower?"
                     " Enter an H, L, or C if my guess was correct ". format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(actual_guesses))
        break
    else:
        print("Please enter an H, L, or C ")
    actual_guesses += 1
