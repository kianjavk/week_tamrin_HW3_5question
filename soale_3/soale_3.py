import os

CONTACTS_FILE = 'contacts.txt'


def load_contacts():

    """Load contacts from the file."""

    contacts = []

    if os.path.exists(CONTACTS_FILE):

        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                contacts.append(line.strip())

        return contacts


def save_contacts(contacts):

    """Save contacts to the file."""

    with open(CONTACTS_FILE, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')


def add_contact(name, phone, email):
    """Add a new contact."""

    contacts = load_contacts()
    new_contact = f"{name},{phone},{email}"


    for contact in contacts:
        contact_name, contact_phone, _ = contact.split(',')

        if contact_name == name and contact_phone == phone:
            print("Error: Duplicate contact found.")
            return

    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts():
    """View all contacts."""

    contacts = load_contacts()
    if not contacts:
        print("No contacts available.")
        return

    contacts.sort()
    print("\nContacts List:")

    for index, contact in enumerate(contacts, start=1):
        name, phone, email = contact.split(',')
        print(f"{index}. {name}, {phone}, {email}")
    print()

def search_contact(name):
    """Search for a contact by name."""

    contacts = load_contacts()
    for contact in contacts:
        if contact.startswith(name + ','):
            name, phone, email = contact.split(',')
            print(f"Found: {name}, Phone: {phone}, Email: {email}")
            return

    print("Contact not found.")


def delete_contact(name):
    """Delete a contact by name."""

    contacts = load_contacts()
    updated_contacts = [c for c in contacts if not c.startswith(name + ',')]

    if len(updated_contacts) == len(contacts):
        print("Contact not found.")
        return

    save_contacts(updated_contacts)
    print("Contact deleted successfully!")


def main():
    """Main function to run the CLI."""

    while True:
        print("\nContact Management System:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            email = input("Enter Email: ").strip()

            if name and phone and email:
                add_contact(name, phone, email)
            else:
                print("Error: All fields are required.")

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name = input("Enter the name to search: ").strip()
            search_contact(name)

        elif choice == '4':
            name = input("Enter the name to delete: ").strip()
            delete_contact(name)

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":

    main()