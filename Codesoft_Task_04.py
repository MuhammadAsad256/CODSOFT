# Initialize an empty dictionary to store contacts
contact = {}

# Function to display all contacts
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key, contact[key]))

# Main loop for the contact management system
while True:
    # Display menu options
    print("1. Add new Contact")
    print("2. Search Contact")
    print("3. Display Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

    # Take user input for choice
    choice = int(input("Enter your choice..."))

    # Option 1: Add new contact
    if choice == 1:
        name = input("Enter the Contact Name...")
        phone = input("Enter the Mobile Number...")
        contact[name] = phone

    # Option 2: Search contact
    elif choice == 2:
        search_name = input("Enter the Contact Name...")
        if search_name in contact:
            print(search_name, ": Contact Number is ", contact[search_name])
        else:
            print("Name is not found in contact book")

    # Option 3: Display all contacts
    elif choice == 3:
        if not contact:
            print("Empty Contact Book")
        else:
            display_contact()

    # Option 4: Edit contact
    elif choice == 4:
        edit_contact = input("Enter the Contact to be edit...")
        if edit_contact in contact:
            phone = input("Enter mobile Number...")
            contact[edit_contact] = phone
            print("Contact Update")
            display_contact()
        else:
            print("Name is not Found in contact book")

    # Option 5: Delete contact
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted...")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n...")
            if confirm.lower() == 'y':
                contact.pop(del_contact)
                print("Contact Deleted")
                display_contact()
        else:
            print("Name is not Found in contact book")

    # Option 6: Exit the program
    elif choice == 6:
        break

    # Invalid choice handling
    else:
        print(".....................................................")
        print("              Invalid Choice")
        print(".....................................................")
