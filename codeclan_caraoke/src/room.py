class Room():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests = []
        self.playlist = []
        self.tab = 0.00
    
    def charge_fee(self, guest):
        guest.pay_fee()
        self.tab += 10

    def check_in(self, guest):
        if self.capacity > 0 and guest.wallet >= 10:
            self.guests.append(guest)
            self.capacity -= 1
            self.charge_fee(guest)
    
    def check_out(self, guest_to_check_out):
        self.guests.remove(guest_to_check_out)
        self.capacity += 1

    def add_song(self, song):
        self.playlist.append(song)

    