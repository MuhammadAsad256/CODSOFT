import random

# Function to generate password
def generate_password(characters):
    while True:
        # User input for password length
        pass_len = input("What length would you like your password to be (type 'exit' to quit): ")
        # Check if user wants to exit
        if pass_len.lower() == "exit":
            break
        else:
            pass_len = int(pass_len)
            # Generate password using random choice from given characters
            password = "".join(random.choice(characters) for _ in range(pass_len))
            # Display generated password
            print("................................................................................")
            print(f"Here is your generated password: {password}")
            print("................................................................................")

# Main loop to handle user choices
while True:
    # User choice for character set
    choice = input("Choose the type of characters for your password: \n1. Alphabets only\n2. Alphabets and Numbers\n3. Alphabets, Numbers, and Special Characters\n4. Exit\n")
    # Case 1: Alphabets only
    if choice == "1":
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        generate_password(characters)
    # Case 2: Alphabets and Numbers
    elif choice == "2":
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                      '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        generate_password(characters)
    # Case 3: Alphabets, Numbers, and Special Characters
    elif choice == "3":
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                      '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                      '`', '~', '!', '@', '#', '$', '%', '^', '&', '&', '*', '(', ')', '-', '_', '=', '+', '\\', '|', '[', ']', '{', '}', ';', ':', '/', '?', '>', '.', '<', ',']
        generate_password(characters)
    # Case 4: Exit
    elif choice == "4":
        break
    # Invalid choice
    else:
        print("................................................................................")
        print("Invalid choice. Please choose again.")
        print("................................................................................")
