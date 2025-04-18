contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!\n")
    
def view_contacts():
        if not contacts:
           print("No contacts found.\n")
        else:
            for i, contact in enumerate(contacts, 1):
               print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
        print()

def search_contact():
    query = input("Enter name or phone to search: ")
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
            found = True
    if not found:
        print("No matching contact found.\n")

def update_contact():
    phone = input("Enter phone number of the contact to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contact['name'] = input("Enter new name: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

    def delete_contact():
      phone = input("Enter phone number of the contact to delete: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

    def menu():
        while True:
          print("===== Contact Book =====")
          print("1. Add Contact")
          print("2. View Contacts")
          print("3. Search Contact")
          print("4. Update Contact")
          print("5. Delete Contact")
          print("6. Exit")

          choice = input("Enter your choice (1-6): ")
          print()
          if choice == '1':
            add_contact()
          elif choice == '2':
            view_contacts()
          elif choice == '3':
            search_contact()
          elif choice == '4':
            update_contact()
          elif choice == '5':
            delete_contact()
          elif choice == '6':
            print("Goodbye!")
            break
          else:
            print("Invalid choice. Please try again.\n")
        menu()
