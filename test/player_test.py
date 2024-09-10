# test/player_test.py

""" Notes:

unittest is a built-in Python module used for creating and running unit tests.

TestPlayer is a test case class that inherits from unittest.TestCase.

test_player_uid and test_player_name are test methods that verify
if the Player class correctly sets and retrieves the player's unique ID and name

unittest.main() is used to run the unit tests when the script is executed.

"""

import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("1", "John")

    def test_player_uid(self):
        self.assertEqual(self.player.uid, "1")

    def test_player_name(self):
        self.assertEqual(self.player.name, "John")

if __name__ == "__main__":
    unittest.main()  # Run the unit tests
