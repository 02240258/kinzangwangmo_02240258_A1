import random   # Importing the random module to generate random numbers


def guess_number_game():
    print("\nWelcome to the Guess the Number game!")     # Welcome message
    number_to_guess = random.randint(1, 100)  #  Selecting random number between 1 and 100
    attempts = 0       # Initialize attempts counter

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))    # Prompt user for input
            attempts += 1        # Increment attempts count
            if user_guess < number_to_guess:
                print("Too low! Try again.")    # If the guess is too low
            elif user_guess > number_to_guess:
                print("Too high! Try again.")     # If the guess is too high
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                break   # Exit the loop
        except ValueError:     # If the user enters something that’s not a number
            print("Please enter a valid number.")    # Error message for invalid input


def rock_paper_scissors_game():
    print("\nWelcome to Rock, Paper, Scissors!")     # Welcome message
    choices = ['rock', 'paper', 'scissors']        # List of possible choices
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to stop): ").lower()   # Prompt user for input and convert to lowercase


        if user_choice == 'exit':      # Check if user wants to exit the game
            print("Thank you for playing! Goodbye.")    # Goodbye message
            break   # Exit the loop


        if user_choice not in choices:   # Check if the input is valid
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")       # Error message for invalid input
            continue   # Prompt user again

        computer_choice = random.choice(choices)      # Randomly choose for the computer
        print(f"Computer chose: {computer_choice}")     # Show the computer's choice


        if user_choice == computer_choice:     # If both choices are the same
            print("It's a tie!")     # Tie message
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):   # If user wins
            print("You win!")  
        else:   # If the computer wins
            print("You lose!")

def main():
    while True:
        print("\nSelect a function (1-3):")   # Show menu options  
        print("1. Guess Number game")       # Option 1
        print("2. Rock Paper Scissors game")   # Option 2
        print("3. Exit program")         # Option 3

        choice = input("Enter your choice: ")     # Prompt user to choose an option


        if choice == '1':      # If user chooses the Guess Number game
            guess_number_game()
        elif choice == '2':       # If user chooses the Rock Paper Scissors game
            rock_paper_scissors_game()
        elif choice == '3':     # If user chooses to exit the program
            print("Exiting the program. Goodbye!")   # Exit message
            break    # Exit the loop and end the program
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")   # Error message for invalid input


# Run the main program
if __name__ == "__main__":
    main()
