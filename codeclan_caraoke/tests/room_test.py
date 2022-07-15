import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Room 1", 5)
        self.room2 = Room("Room 2", 1)
                
        self.song1 = Song("Take on Me", "Aha")
        self.song2 = Song("Africa", "Toto")
        self.song3 = Song("Thriller", "Michael Jackson")
        self.song4 = Song("Bohemiam Raphsody", "Queen")
        
        self.guest1 = Guest("Juan", [self.song1, self.song2], 100.00, self.song2)
        self.guest2 = Guest("Diego", [self.song3, self.song4], 200.00, self.song3)

    def test_create_room(self):
        self.assertEqual("Room 1", self.room1.name)

    def test_room_can_check_in_guests(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(self.guest1, self.room1.guests[0])

    def test_room_can_check_out_one_guest(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_out(self.guest1)
        self.assertEqual("Diego", self.room1.guests[0].name)
    
    def test_rooms_have_playlist(self):
        self.room1.add_song(self.song3)
        self.assertEqual("Michael Jackson", self.room1.playlist[0].artist)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room1.capacity)
    
    def test_capacity_decreases_when_guest_checks_in(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(4, self.room1.capacity)
    
    def test_capacity_increases_when_guest_checks_out(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_out(self.guest1)
        self.assertEqual(4, self.room1.capacity)
    
    def test_when_room_full_you_cant_check_another_guest_in(self):
        self.room2.check_in(self.guest1)
        self.room2.check_in(self.guest2)
        self.assertEqual(1, len(self.room2.guests))

    def test_when_room_is_empty_capacity_does_not_increase_if_check_out(self):
        self.assertRaises(ValueError, self.room2.check_out, self.guest2)
        self.assertEqual(1, self.room2.capacity)