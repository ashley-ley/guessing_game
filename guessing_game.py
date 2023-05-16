import random
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while number != guess:
    guess = int(input(f"Enter a number between {low} - {high}: "))
    guesses += 1 

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else: 
        print(f"{guess} is correct!") 

print(f"This round took you {guesses} guesses")