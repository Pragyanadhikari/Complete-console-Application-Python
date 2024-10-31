# 10. Text-Based Adventure Game
# • Description: Develop a simple text-based adventure game. Implement classes for Player, Room, and Item. Include features for navigating rooms, collecting items, and completing quests.
# • OOP Concepts: Composition (rooms contain items), Inheritance (different player types), and Encapsulation(managing player stats).

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"Item: {self.name} - {self.description}"

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.connected_rooms = {}

    def add_item(self, item):
        self.items.append(item)

    def connect_room(self, direction, room):
        self.connected_rooms[direction] = room

    def get_description(self):
        return f"{self.name}: {self.description}"

    def __str__(self):
        return f"Room: {self.name}\nDescription: {self.description}\n"

class Player:
    def __init__(self, name, player_type):
        self.name = name
        self.player_type = player_type
        self.health = 100
        self.inventory = []
        self.current_room = None

    def setCurrentRoom(self,room):
        self.current_room=room

    def move(self, direction):
        if direction in self.current_room.connected_rooms:
            self.current_room = self.current_room.connected_rooms[direction]
            print(f"\n{self.name} moved to {self.current_room.name}.")
            print(self.current_room.get_description())
        else:
            print(f"\nCan't move {direction} from here.")

    def pick_up_item(self, item_name):
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print(f"\n{self.name} picked up {item.name}.")
                return
        print(f"\n{item_name} not found in this room.")

    def show_inventory(self):
        if not self.inventory:
            print(f"\n{self.name}'s inventory is empty.")
        else:
            print(f"\n{self.name}'s Inventory:")
            for item in self.inventory:
                print(f"  - {item}")

    def show_stats(self):
        print(f"\nPlayer: {self.name}")
        print(f"Type: {self.player_type}")
        print(f"Health: {self.health}")
        print(f"Current Room: {self.current_room.name}")


class Online(Player):
    def __init__(self, name):
        super().__init__(name, "Online")


class Offline(Player):
    def __init__(self, name):
        super().__init__(name, "Offline")

def game_setup():
    room1=Room("Sword Room","A room with full of sword can be used for defense.")
    room2=Room("Shield Room","A room full of sword for defense.")
    room3=Room("Health Room","A room full of health kit item to restore health.")
    room4=Room("Exit","Exit from here.")

    item1=Item("Sword","Used for combat.")
    item2=Item("Shield","Used for defense.")
    item3=Item("Health","To increase the health bar.")

    room1.add_item(item1)
    room2.add_item(item2)
    room3.add_item(item3)

    room1.connect_room("north", room2)
    room2.connect_room("south", room1)
    room2.connect_room("east", room3)
    room3.connect_room("west", room2)
    room3.connect_room("north", room4)

    return room1

def start_game():
    starting_room = game_setup()
    player = Online("Hira") 
    player.setCurrentRoom(starting_room)
    
    print(player.current_room.get_description()) 
    
    while True:
        command = input("\nEnter a command (move, pick up, inventory, stats, quit): ").strip().lower()

        if command.startswith("move"):
            direction = command.split()[-1]
            player.move(direction)

        elif command.startswith("pick up"):
            item_name = command.replace("pick up ", "")
            player.pick_up_item(item_name)

        elif command == "inventory":
            player.show_inventory()

        elif command == "stats":
            player.show_stats()

        elif command == "quit":
            print("Thanks for playing!")
            break

        else:
            print("Invalid command, try again.")

start_game()