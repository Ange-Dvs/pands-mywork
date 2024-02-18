# lab4.2.2_guess1.py
# This program asks a user to guess a number. 
# The user should continue to be prompted until the right answer is given.
# It should tell the user if they are guessing too high or too low if the answer is not correct
# Author: Angela Davis 

print("Lets play a guessing game!Try to guess the correct number.\n*Hint: The number is between 1 and 100")

num_to_guess = 35
user_Guess = int(input("Please guess the number:"))

while user_Guess != num_to_guess: #checks if the number guessed by the user is not equal to the correct answer
    if user_Guess < num_to_guess: #if it's not equal and it's lower than the number to guess this flow is triggered
        user_Guess = int(input("Too low\nPlease guess again:"))
    else: #if it's not equal and not lower to the guess it most be higer, in this case this flow is triggered
        user_Guess = int(input("Too high\nPlease guess again:"))

print(f"Well done! Yes the number to was", num_to_guess)




                 
