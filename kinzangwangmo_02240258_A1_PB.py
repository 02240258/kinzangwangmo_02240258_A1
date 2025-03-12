import random

def guess_number_game():
    print("\nWelcome to the Guess the Number game!")
    number_to_guess = random.randint(1, 100)  #  Selecting random number between 1 and 100
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def rock_paper_scissors_game():
    print("\nWelcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to stop): ").lower()

        if user_choice == 'exit':
            print("Thank you for playing! Goodbye.")
            break

        if user_choice not in choices:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")

def main():
    while True:
        print("\nSelect a function (1-3):")
        print("1. Guess Number game")
        print("2. Rock Paper Scissors game")
        print("3. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

# Run the main program
if __name__ == "__main__":
    main()