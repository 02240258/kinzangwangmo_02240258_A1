# Function 1: Prime Number Sum Calculator
def prime_sum(start, end):    # Helper function to check whether number is prime
    def is_prime(n):
        if n <= 1:       # Numbers <= 1 are not prime
            return False
        for i in range(2, n):    # Check divisibility from 2 to n-1
            if n % i == 0:        # If divisible, n is not prime
                return False
        return True         # n is prime if no divisors found
    
    total = 0       # Initialize sum of prime numbers
    for num in range(start, end + 1):   # Loop from start to end
        if is_prime(num):    # Check if current number is prime
            total += num     # Add prime to total sum
    return total       # Return the sum of primes


# Function 2: Length Unit Converter
def length_converter(value, direction):
    if direction.lower() == 'm':  
        return round(value * 3.28084, 2)  # change meters to feet
    elif direction.lower() == 'f':
        return round(value / 3.28084, 2)  # change feet to meters
    else:
        return "Invalid direction"

# Function 3: Consonant Counter
def consonant_counter(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in text:    # Looping through each character in the input text
     if char in consonants:   # Checking if the character is a consonant
            count += 1
    return count          # Returning the total count of consonants

# Function 4: Min-Max Number Finder
def min_max_finder(numbers):
    if len(numbers) == 0:      
        return "No numbers entered"    # If the list of numbers is empty, return a message
    return f"Smallest: {min(numbers)}, Largest: {max(numbers)}"   # Return the smallest and largest number in the list

# Function 5: Palindrome Checker
def palindrome_checker(text):    
    cleaned_text = ''.join(text.split()).lower()  # Removing spaces and making it lowercase
    return cleaned_text == cleaned_text[::-1]

# Function 6: Word Counter (Sample words from file)
def word_counter(file_path):
    words_to_count = ["the", "was", "and"]
    word_count = {word: 0 for word in words_to_count}     # Creating a dictionary to store the count of each word

    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  # Read and convert to lowercase for case-insensitivity
            for word in words_to_count:     # Counting the occurrences of each word in the file
                word_count[word] = text.split().count(word)
    except FileNotFoundError:
        return "File not found"   # If the file doesn't exist, return an error message
    
    return word_count   # Returning the word counts as a dictionary

# Main program function
def main():
    while True:
        print("\nSelect any function from (1-6):")
        print("1. Calculate the sum of prime numbers of the given range")
        print("2. Convert length units into either meters or feets")
        print("3. Count consonants in given string")
        print("4. Find the minimum and the maximum numbers")
        print("5. Check whether the given word is a palindrome ")
        print("6. Count the words with Word Counter")
        print("0. Exit program")
        
        try:
            choice = int(input("Enter your choice: "))    # Asking the user for their choice of function
            
            if choice == 1:    # If choice is 1, calculate the sum of prime numbers in a range
                start = int(input("Enter the starting range: "))   
                end = int(input("Enter ending range: "))
                print(f"Result of the sum of prime numbers: {prime_sum(start, end)}")
                
            elif choice == 2:      # If choice is 2, convert a length value to meters or feet
                value = float(input("Enter any numeric value: "))    
                direction = input("Enter conversion direction (M for meters to feet, F for feet to meters): ")
                print(f"Converted value: {length_converter(value, direction)}")
                
            elif choice == 3:    # If choice is 3, count the number of consonants in a string
                text = input("Enter a string: ")  
                print(f"Number of consonants: {consonant_counter(text)}")
                
            elif choice == 4:   # If choice is 4, find the minimum and maximum values from a list of numbers
                n = int(input("How many numbers would you like to enter? "))
                numbers = []
                for i in range(n):
                    num = float(input(f"Enter number {i+1}: "))
                    numbers.append(num)
                print(min_max_finder(numbers))
                
            elif choice == 5:   # If choice is 5, check if the input string is a palindrome
                text = input("Enter a string: ")
                print(f"Is it a palindrome? {palindrome_checker(text)}")
                
            elif choice == 6:   # If choice is 6, count specific words in a file
                file_path = input("Enter the path to the text file: ")
                print(word_counter(file_path))
                
            elif choice == 0:    # If choice is 0, exit the program
                print("Exiting the program.")
                break
            else:       
                print("Invalid choice, please try again.")   # If the choice is invalid, ask the user to try again
            
            continue_choice = input("\nWould you like to try another function? (y/n): ").lower()   # Asking the user if they want to try another function
            if continue_choice != 'y':
                print("Exiting the program.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")   # If the user inputs a non-numeric value, display an error message

# Run the program
if __name__ == "__main__":    
    main()