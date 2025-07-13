# ----------------------------------------------------------
#                PASSWORD GENERATOR APP
# ----------------------------------------------------------
# Project developed for Open Source Development final project
# Purpose: Generate secure passwords based on user inputs
# ----------------------------------------------------------

import random


# ----------------------------------------------------------
#                        ASCII LOGO
# ----------------------------------------------------------

def print_logo():
    print("=" * 70)
    print("""
    ____                                     _    
    |  _ \ __ _ ___ _____      _____  _ __ __| |   
    | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |   
    |  __/ (_| \__ \__ ''\ V  V / (_) | | | (_| |   
    |_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|   
     / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
    | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
     \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   

      """)

    print("🔒 Welcome to Password Generator 🔒".center(70))
    print("=" * 70)
    print()


# ----------------------------------------------------------
#                   UTILITY FUNCTIONS
# ----------------------------------------------------------

def print_separator():
    """Prints a visual separator"""
    print("-" * 70)


def goodbye_message():
    """Prints a nice exit message"""
    print_separator()
    print("🎯 Thank you for using Password Generator! 🎯".center(70))
    print("🔐 Stay safe and keep your passwords secure! 🔐".center(70))
    print_separator()


def password_strength_check(length):
    """Simple password strength checker based on length"""
    if length < 8:
        return "Weak Password 🔴"
    elif 8 <= length < 12:
        return "Moderate Password 🟡"
    else:
        return "Strong Password 🟢"


# ----------------------------------------------------------
#                  INPUT SECTION
# ----------------------------------------------------------

def get_user_input():
    """Gets user input for number of letters, symbols, and numbers"""
    while True:
        try:
            nr_letters = int(input("How many letters would you like in your password? 🔤 "))
            nr_symbols = int(input("How many symbols would you like? 🔣 "))
            nr_numbers = int(input("How many numbers would you like? 🔢 "))
            return nr_letters, nr_symbols, nr_numbers
        except ValueError:
            print("❌ Please enter a valid number.")


# ----------------------------------------------------------
#              PASSWORD GENERATION FUNCTIONS
# ----------------------------------------------------------

# Character pools
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")


def generate_password_lists(nr_letters, nr_symbols, nr_numbers):
    """Generates lists of random letters, numbers, and symbols"""
    letter_list = []
    symbols_list = []
    numbers_list = []

    len_letters = len(letters)
    len_numbers = len(numbers)
    len_symbols = len(symbols)

    for _ in range(nr_letters):
        random_letter = random.randint(0, len_letters - 1)
        selected_letter = letters[random_letter]
        letter_list.append(selected_letter)

    for _ in range(nr_symbols):
        random_symbol = random.randint(0, len_symbols - 1)
        selected_symbol = symbols[random_symbol]
        symbols_list.append(selected_symbol)

    for _ in range(nr_numbers):
        random_number = random.randint(0, len_numbers - 1)
        selected_number = numbers[random_number]
        numbers_list.append(selected_number)

    return letter_list, numbers_list, symbols_list


def create_straight_password(letter_list, numbers_list, symbols_list):
    """Creates a straight (non-randomized) password"""
    final_list = letter_list + numbers_list + symbols_list
    straight_password = ""
    for char in final_list:
        straight_password += char
    return straight_password


def manual_randomizer(letter_list, numbers_list, symbols_list):
    """Randomizes the final password manually without shuffle"""
    final_list = letter_list + numbers_list + symbols_list
    final_password = ""
    copied_list = final_list.copy()
    check_list = ["available"] * len(copied_list)

    total_length = len(final_list)
    random_password_list = []

    for _ in range(total_length * total_length):
        rand_index = random.randint(0, total_length - 1)
        if check_list[rand_index] != "used":
            random_password_list.append(copied_list[rand_index])
            check_list[rand_index] = "used"

    for char in random_password_list:
        final_password += char

    return final_password


# ----------------------------------------------------------
#                      MAIN FUNCTION
# ----------------------------------------------------------

def main():
    # Print welcome logo
    print_logo()

    while True:
        # Get user input
        nr_letters, nr_symbols, nr_numbers = get_user_input()

        total_length = nr_letters + nr_symbols + nr_numbers

        # Generate password parts
        letters_part, numbers_part, symbols_part = generate_password_lists(nr_letters, nr_symbols, nr_numbers)

        # Straight password
        straight_password = create_straight_password(letters_part, numbers_part, symbols_part)

        # Randomized password
        random_password = manual_randomizer(letters_part, numbers_part, symbols_part)

        # Show passwords
        print_separator()
        print("\n🔑 Your generated password (non-randomized):")
        print(f"    {straight_password}")
        print(f"Password Strength: {password_strength_check(total_length)}")
        print_separator()

        print("\n🔑 Your randomized password (more secure):")
        print(f"    {random_password}")
        print(f"Password Strength: {password_strength_check(total_length)}")
        print_separator()

        # Ask user if they want to generate another password
        user_choice = input("\n🔁 Do you want to generate another password? (Y/N): ").strip().lower()
        if user_choice != 'y':
            break

    # Exit message
    goodbye_message()


# ----------------------------------------------------------
#                PROGRAM ENTRY POINT
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
