import random
number = random.randint(1, 20)
attemps = 0
print("Guess the number between 1 and 20")
while True:
    guess = int(input("Enter your guess: "))
    attemps += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! the number was {number}")
        print(f"you guessed it in {attemps} attemps!")