# Hotel Management System Project


class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def display_details(self):
        """Display details of the room."""
        status = "Booked" if self.is_booked else "Available"
        print(f"Room {self.room_number}: Type: {self.room_type}, Price: ${self.price}, Status: {status}")



class Person:
    def __init__(self, name):
        self.name = name



class Admin(Person):
    def __init__(self, name, hotel):
        super().__init__(name)
        self.hotel = hotel

    def add_room(self, room_number, room_type, price):
        """Add a room to the hotel."""
        self.hotel.add_room(Room(room_number, room_type, price))
        print(f"Room {room_number} added to the hotel.")

    def remove_room(self, room_number):
        """Remove a room from the hotel."""
        if self.hotel.remove_room(room_number):
            print(f"Room {room_number} removed from the hotel.")
        else:
            print(f"Room {room_number} not found.")



class Guest(Person):
    def __init__(self, name, hotel):
        super().__init__(name)
        self.hotel = hotel

    def view_available_rooms(self):
        """View all available rooms."""
        print(f"Available rooms for {self.name}:")
        self.hotel.display_available_rooms()

    def book_room(self, room_number):
        """Book a room."""
        if self.hotel.book_room(room_number):
            print(f"{self.name} successfully booked room {room_number}.")
        else:
            print(f"Room {room_number} is not available.")

    def cancel_booking(self, room_number):
        """Cancel a room booking."""
        if self.hotel.cancel_booking(room_number):
            print(f"{self.name} canceled the booking for room {room_number}.")
        else:
            print(f"Room {room_number} is not booked.")



class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        """Add a room to the hotel."""
        self.rooms.append(room)

    def remove_room(self, room_number):
        """Remove a room from the hotel."""
        for room in self.rooms:
            if room.room_number == room_number:
                self.rooms.remove(room)
                return True
        return False

    def display_available_rooms(self):
        """Display all available rooms."""
        available_rooms = [room for room in self.rooms if not room.is_booked]
        if available_rooms:
            for room in available_rooms:
                room.display_details()
        else:
            print("No rooms available.")

    def book_room(self, room_number):
        """Book a room."""
        for room in self.rooms:
            if room.room_number == room_number and not room.is_booked:
                room.is_booked = True
                return True
        return False

    def cancel_booking(self, room_number):
        """Cancel a booking."""
        for room in self.rooms:
            if room.room_number == room_number and room.is_booked:
                room.is_booked = False
                return True
        return False


# Testing the Hotel Reservation System
if __name__ == "__main__":
    # Create a Hotel instance
    hotel = Hotel()

    # Create an Admin
    admin = Admin("Alice", hotel)

    # Admin adds rooms
    admin.add_room(101, "Single", 100)
    admin.add_room(102, "Double", 150)
    admin.add_room(103, "Suite", 250)

    # Create a Guest
    guest = Guest("Bob", hotel)

    # Display available rooms
    print("\nAvailable Rooms:")
    guest.view_available_rooms()

    # Guest books a room
    print("\nBooking a Room:")
    guest.book_room(101)

    # Display available rooms after booking
    print("\nAvailable Rooms After Booking:")
    guest.view_available_rooms()

    # Guest cancels the booking
    print("\nCanceling Booking:")
    guest.cancel_booking(101)

    # Display available rooms after canceling
    print("\nAvailable Rooms After Canceling:")
    guest.view_available_rooms()
