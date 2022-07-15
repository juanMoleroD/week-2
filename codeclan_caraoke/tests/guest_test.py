import unittest
from src.guest import Guest 
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.song1 = Song("Take on Me", "Aha")
        self.song2 = Song("Africa", "Toto")
        self.song3 = Song("Thriller", "Michael Jackson")
        self.song4 = Song("Bohemiam Raphsody", "Queen")

        self.guest1 = Guest("Juan", [self.song1, self.song2], 100.00, self.song2)
        self.guest2 = Guest("Diego", [self.song3, self.song4], 200.00, self.song3)

    
    def test_guest_has_name(self):
        self.assertEqual("Juan", self.guest1.name)

    def test_guest_has_songs(self):
        self.assertEqual("Africa", self.guest1.songs[1].name)
    
    def test_guests_have_wallets(self):
        self.assertEqual(100.00, self.guest1.wallet)
    
    def test_guest_can_pay_fee(self):
        self.guest1.pay_fee()
        self.assertEqual(90.00, self.guest1.wallet)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Africa", self.guest1.favourite_song.name)
    
    def test_guest_cheers_if_favourite_song_on_room_playlist(self):
        self.assertEqual("Whoo!!", self.guest1.check_for_favourite_song(self.room1))
