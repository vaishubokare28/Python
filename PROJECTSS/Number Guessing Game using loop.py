# Number Guessing Game in Python using loops and conditionals:
secret_number = 42 

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number: {secret_number}")
        break  
