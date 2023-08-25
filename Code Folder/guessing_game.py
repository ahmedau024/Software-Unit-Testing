# Import the 'random' module for generating random numbers
import random

# Function to generate a random 4-digit number as a string
def generate_random_number():
    return str(random.randint(1000, 9999))

# Function to provide hints based on the secret number and the player's guess
def give_hints(secret_number, guess):
    # Initialize an empty list to store hints
    hints = []
    
    # Iterate through each digit's position
    for i in range(len(secret_number)):
        # Compare the digit at the current position in secret_number and guess
        if secret_number[i] == guess[i]:
            hints.append('O')  # Add 'O' if the digit and position match
        elif guess[i] in secret_number:
            hints.append('x')  # Add 'x' if the digit is correct but in the wrong position
        else:
            hints.append('_')  # Add '_' if the digit is not present in the secret number
    return hints

# Function to play the guessing game
def play_game():
    # Generate a random secret number for the current game
    print("Welcome to the Guess Number Game!")
    secret_number = generate_random_number()
    
    # Initialize the number of attempts made by the player
    attempts = 0
    
    # Start a loop for each game session
    while True:
        # Get the player's guess as input
        guess = input("Guess the four-digit number: or write quit for quitting the game: ")
        
        # Check if the player wants to quit the game
        if guess == 'quit':
            # Display the secret number and the number of attempts made
            print(f"The secret number was {secret_number}.")
            if attempts == 0:
                print("You took 0 attempts.")
            else:
                print(f"You took {attempts} attempts.")
            break
        
        # Validate the input for a 4-digit number
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a four-digit number.")
            continue
        
        # Increment the attempts counter
        attempts += 1
        
        # Get hints based on the player's guess and the secret number
        hints = give_hints(secret_number, guess)
        
        # Check if the player's guess matches the secret number
        if guess == secret_number:
            # Display a congratulatory message with the secret number and attempts made
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        else:
            # Display the hints provided for the player's guess
            print("Hints:", ' '.join(hints))

# Function to manage the entire game
def main():
    # Start an infinite loop for playing multiple game sessions
    while True:
        # Call the play_game function to play a single game
        play_game()
        
        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        
        # Check if the player wants to end the game
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

# Start the main function if the script is run as the main program
if __name__ == "__main__":
    main()
