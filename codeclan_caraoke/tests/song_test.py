import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Take on Me", "Aha")
        self.song2 = Song("Africa", "Toto")
    
    def test_song_has_name(self):
        self.assertEqual("Take on Me", self.song1.name)

    def test_song_has_artist(self):
        self.assertEqual("Toto", self.song2.artist)