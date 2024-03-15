import random

# the set of characters like alphabets, numbers, and special characters:
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
              '`', '~', '!', '@', '#', '$', '%', '^', '&', '&', '*', '(', ')', '-', '_', '=', '+', '\\', '|', '[', ']', '{', '}', ';', ':', '/', '?', '>', '.', '<', ',']

while True:
#   User input
    pass_len = input("What Length would you like your password to be (type 'exit' to quit): ")
#   Check condition
    if pass_len == "exit":
        break
    else:
        pass_len = int(pass_len)
        password = ""
        for i in range(pass_len):
            password += random.choice(characters)
        print("................................................................................")
        print(f"Here is your Generated Password : {password}")
        print("................................................................................")
