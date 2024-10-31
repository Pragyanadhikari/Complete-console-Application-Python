# Contact Management System
# • Description: Build a console application to manage contacts. Implement classes for Contact, PhoneBook, and User. Include features to add, edit, delete, and search for contacts.
# • OOP Concepts: Composition (phone books contain contacts), Encapsulation (managing contact details), and Inheritance (different types of contacts).

class Contact:
    def __init__(self, contact, name='', email='', nickname=''):
        self.name = name
        self.contact_number = contact
        self.email = email
        self.nickname = nickname
    
    def update_contact(self, name=None, contact=None, email=None, nickname=None):
        if name:
            self.name = name
        if contact:
            self.contact_number = contact
        if email:
            self.email = email
        if nickname:
            self.nickname = nickname
        print("Contact updated.")
    
    def __str__(self):
        return f'Name: {self.name}\nContact Number: {self.contact_number}\nEmail: {self.email}\nNickname: {self.nickname}'

class PhoneBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        if any(c.contact_number == contact.contact_number for c in self.contacts):
            print("Contact already exists.")
        else:
            self.contacts.append(contact)
            
    
    def remove_contact(self, contact_number):
        for contact in self.contacts:
            if contact.contact_number == contact_number:
                self.contacts.remove(contact)
                print(f"Contact {contact.name} with number {contact_number} removed.")
                return
        print(f"Contact with number {contact_number} not found.")
    
    def edit_contact(self, contact_number, name=None, email=None, nickname=None):
        for contact in self.contacts:
            if contact.contact_number == contact_number:
                contact.update_contact(name=name, contact=contact_number, email=email, nickname=nickname)
                return
        print(f"Contact with number {contact_number} not found.")
    
    def search_contact(self, name=None, contact_number=None):
        results = []
        for contact in self.contacts:
            if name and contact.name.lower() == name.lower():
                results.append(contact)
            elif contact_number and contact.contact_number == contact_number:
                results.append(contact)
        
        if results:
            print("Search Results:")
            for contact in results:
                print(contact)
        else:
            print("No matching contacts found.")
    
    def show_contacts(self):
        if not self.contacts:
            print("No contacts in the Phone book.")
        else:
            print("Contacts in Phone book:")
            for contact in self.contacts:
                print(contact)
            print()

class User:
    user_id_counter = 1
    
    def __init__(self, username):
        self.username = username
        self.user_id = User.user_id_counter
        User.user_id_counter += 1
        self.phone_book = PhoneBook()
    
    def add_contact_to_phoneBook(self, contact):
        self.phone_book.add_contact(contact)
    
    def remove_contact_from_phoneBook(self, contact_number):
        self.phone_book.remove_contact(contact_number)
    
    def edit_contact_in_phoneBook(self, contact_number, name=None, email=None, nickname=None):
        self.phone_book.edit_contact(contact_number, name=name, email=email, nickname=nickname)
    
    def search_contact_in_phoneBook(self, name=None, contact_number=None):
        self.phone_book.search_contact(name=name, contact_number=contact_number)
    
    def show_all_contacts(self):
        self.phone_book.show_contacts()
    
    def __str__(self):
        return f'User: {self.username}, ID: {self.user_id}'

# Example usage
user1 = User("Pragyan")
contact1 = Contact("984123456", name="Hira", email="hira@gmail.com", nickname="HiraJira")
contact2 = Contact("987987654", name="Nita", email="Nita@gmail.com")

user1.add_contact_to_phoneBook(contact1)
user1.add_contact_to_phoneBook(contact2)
user1.show_all_contacts()

user1.edit_contact_in_phoneBook("9876343212", name="Shuvam", email="sub@gmail.com")
user1.search_contact_in_phoneBook(name="Hira")
user1.remove_contact_from_phoneBook("987987654")

user1.show_all_contacts()


    