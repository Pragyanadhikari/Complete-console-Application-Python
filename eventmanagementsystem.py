# 13. Event Management System
# • Description: Create a console application for managing events. Implement classes for Event, Venue, and Attendee. Include features for creating events, registering attendees, and managing venues.
# • OOP Concepts: Composition (events occur at venues), Inheritance (different types of events), and Encapsulation (managing attendee details).
class Event:
    def __init__(self, name, date, time, venue):
        self.name = name
        self.date = date
        self.time = time
        self.venue = venue
        self.attendees = []

    def register_attendee(self, attendee):
        if attendee not in self.attendees:
            self.attendees.append(attendee)
            print(f"{attendee.name} has registered for {self.name}.")
        else:
            print(f"{attendee.name} is already registered for {self.name}.")

    def show_attendees(self):
        if self.attendees:
            print(f"\nAttendees for {self.name}:")
            for attendee in self.attendees:
                print(f"  - {attendee.name}")
        else:
            print(f"No audience have registered for {self.name} yet.")

    def __str__(self):
        return f"Event: {self.name}\nDate: {self.date}\nTime: {self.time}\nVenue: {self.venue.name}\n"


class Venue:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

    def __str__(self):
        return f"Venue: {self.name}\nLocation: {self.location}\nCapacity: {self.capacity}\n"

class Attendee:
    def __init__(self, name, email, phone):
        self.name = name
        self.__email = email  
        self.__phone = phone  

    def __str__(self):
        return f"Audience name: {self.name}\nEmail: {self.__email}\nPhone: {self.__phone}"

class ConcertEvent(Event):
    def __init__(self, name, date, time, venue, artist):
        super().__init__(name, date, time, venue)
        self.artist = artist

    def __str__(self):
        return f"Concert: {self.name}\nArtist: {self.artist}\nDate: {self.date}\nTime: {self.time}\nVenue: {self.venue.name}\n"

class LateNightEvent(Event):
    def __init__(self, name, date, time, venue, main_dancer):
        super().__init__(name, date, time, venue)
        self.main_dancer = main_dancer

    def __str__(self):
        return f"Late Night: {self.name}\nMain Dancer: {self.main_dancer}\nDate: {self.date}\nTime: {self.time}\nVenue: {self.venue.name}\n"

class EventManagementSystem:
    def __init__(self):
        self.events = []
        self.venues = []
        self.attendees = []

    def add_venue(self, venue):
        self.venues.append(venue)
        print(f"Venue '{venue.name}' added.")

    def create_event(self, event):
        self.events.append(event)
        print(f"Event '{event.name}' created at {event.venue.name}.")

    def register_attendee(self, event_name, attendee_name):
        event = next((e for e in self.events if e.name == event_name), None)
        attendee = next((a for a in self.attendees if a.name == attendee_name), None)
        
        if not event:
            print(f"Event {event_name} not found.")
            return
        if not attendee:
            print(f"Attendee {attendee_name} not found.")
            return
        
        if len(event.attendees) < event.venue.capacity:
            event.register_attendee(attendee)
        else:
            print(f"The event {event_name} is full and cannot register more attendees.")

    def add_attendee(self, attendee):
        self.attendees.append(attendee)
        print(f"Attendee '{attendee.name}' added.")

    def show_events(self):
        print("\n--- Events ---")
        for event in self.events:
            print(event)

    def show_venues(self):
        print("\n--- Venues ---")
        for venue in self.venues:
            print(venue)

    def show_attendees_for_event(self, event_name):
        event = next((e for e in self.events if e.name == event_name), None)
        if event:
            event.show_attendees()
        else:
            print(f"Event {event_name} not found.")

ems = EventManagementSystem()

v1 = Venue("Dashrat Rangasala", "Tripureshor", 5000)
v2 = Venue("Rastriya nach Ghar", "Kamaladi", 500)
ems.add_venue(v1)
ems.add_venue(v2)
concert = ConcertEvent("Concert with KS", "2024-11-05", "19:00", v1, "Kumai Sagar")
LateNight = LateNightEvent("Late Night Dance", "2024-11-12", "09:00", v2, "Raghav Juyal")
ems.create_event(concert)
ems.create_event(LateNight)

a1 = Attendee("Pragyan", "pragyan@gmail.com", "989898989898")
a2 = Attendee("Rita", "rita@gmail.com", "987654321")
ems.add_attendee(a1)
ems.add_attendee(a2)
ems.register_attendee("Concert with KS", "Pragyan")
ems.register_attendee("Concert with KS", "Rita")
ems.register_attendee("Late Night Dance", "Pragyan")
ems.show_events()
ems.show_venues()
ems.show_attendees_for_event("Concert with KS")
ems.show_attendees_for_event("Late Night Dance")