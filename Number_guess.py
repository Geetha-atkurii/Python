# Use a while loop to create a guessing game where the user has to guess a secret number.

secret_number = 28       # other way to guess [import random and secret_number = random.randint(1, 30)]  
guess = None

print("Try to guess the secret number between 1 and 30.")

while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    
    if guess < secret_number:
        print("The number you have guessed is too low! Try again.")
    elif guess > secret_number:
        print("The number you have guessed is too high! Try again.")
    else:
        print("Congratulations! You've guessed the secret number!")
    
        