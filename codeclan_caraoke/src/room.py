class Room():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.playlist = []

    
    def check_in(self, guest):
        if self.capacity > 0:
            self.guests.append(guest)
            self.capacity -= 1
    
    def check_out(self, guest_to_check_out):
        self.guests.remove(guest_to_check_out)
        self.capacity += 1

    def add_song(self, song):
        self.playlist.append(song)