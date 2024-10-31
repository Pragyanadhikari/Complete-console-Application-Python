# 15. Personal Journal Application
# • Description: Develop a console application to manage personal journal entries. Implement classes for Entry, Journal, and User. Include methods for adding, editing, and deleting journal entries.
# • OOP Concepts: Composition (journals contain entries), Inheritance (different entry types), and Encapsulation (managing user information).

class Entry:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def edit_entry(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\n"

class Journal:
    def __init__(self, user):
        self.user = user
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)
        print(f"Entry '{entry.title}' added.")

    def edit_entry(self, entry_title):
        for entry in self.entries:
            if entry.title.lower() == entry_title.lower():
                new_title = input(f"Dear user {self.name},enter new title for entry '{entry_title}': ")
                new_content = input(f"Enter new content for entry '{entry_title}': ")
                entry.edit_entry(new_title, new_content)
                print(f"Entry '{entry_title}' has been updated.")
                return
        print(f"Entry '{entry_title}' not found.")

    def delete_entry(self, entry_title):
        for entry in self.entries:
            if entry.title.lower() == entry_title.lower():
                self.entries.remove(entry)
                print(f"Entry '{entry.title}' deleted.")
                return
        print(f"Entry '{entry_title}' not found.")

    def view_entries(self):
        if not self.entries:
            print("No entries in the journal.")
        else:
            print(f"\n--- {self.user.name}'s Journal Entries ---")
            for entry in self.entries:
                print(entry)
        print()

class User:
    def __init__(self, name):
        self.name = name
        self.journal = Journal(self)

    def add_journal_entry(self):
        title = input(f"Dear user {self.name}, enter the title of the entry: ")
        content = input("Enter the content of your entry: ")
        entry = Entry(title, content)
        self.journal.add_entry(entry)

    def edit_journal_entry(self, entry_title):
        self.journal.edit_entry(entry_title)

    def delete_journal_entry(self, entry_title):
        self.journal.delete_entry(entry_title)

    def view_journal_entries(self):
        self.journal.view_entries()

class JournalSystem:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' added to the journal system.")

    def display_users(self):
        if not self.users:
            print("No users found.")
        else:
            print("Users:")
            for user in self.users:
                print(f"  - {user.name}")
        print()

def run_journal_system():
    system = JournalSystem()
    u1 = User("Pragyan")
    u2 = User("Hira")
    system.add_user(u1)
    system.add_user(u2)
    u1.add_journal_entry() 
    u2.add_journal_entry()  
    u1.view_journal_entries()  
    u2.view_journal_entries()  

    u1.edit_journal_entry("Blog") 
    u1.view_journal_entries()

    u2.delete_journal_entry("My Day") 
    u2.view_journal_entries()

    system.display_users()
run_journal_system()