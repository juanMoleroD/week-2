from unicodedata import name


class Guest():
    def __init__(self, name, songs, wallet, favourite_song):
        self.name = name
        self.songs = songs
        self.wallet = wallet
        self.favourite_song = favourite_song

    def pay_fee(self):
        self.wallet -= 10

    def check_for_favourite_song(self, room):
        for song in room.playlist:
            if song.name == self.favourite_song.name and song.artist == self.favourite_song.artist:
                return "Whoo!!"