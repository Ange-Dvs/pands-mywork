# lab4.2.2_guess1.py
# This program asks a user to guess a number. 
# The user should continue to be prompted until the right answer is given.
# Author: Angela Davis 

# Define number to guess
# Gather users input 
# while num_To_Guess != user_Guess prompt user to guess again 

print("Lets play a guessing game!Try to guess the correct number.\n*Hint: The number is between 1 and 100")

num_to_guess = 35
user_Guess = int(input("Please guess the number:"))

while user_Guess != num_to_guess: #checks if the number guessed by the user is not equal to the correct answer
    user_Guess = int(input("Wrong\nPlease guess again:"))

print(f"Well done! Yes the number to was", num_to_guess)



                 
