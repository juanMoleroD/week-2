class Guest():
    def __init__(self, name, songs, wallet):
        self.name = name
        self.songs = songs
        self.wallet = wallet

    def pay_fee(self):
        self.wallet -= 10

    def check_for_favourite_song(room):
        