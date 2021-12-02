import datetime

class Event():

    def __init__(self, date, name, guest_number, room_location, description, recurring):
        self.date = date
        self.name = name
        self.guest_number = guest_number
        self.room_location = room_location
        self.description = description
        self.recurring = recurring

