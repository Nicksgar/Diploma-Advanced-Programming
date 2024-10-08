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
    def test_player_uid(self):
        """
        Test if the player's unique ID is set and retrieved correctly.
        """
        player = Player("1", "John")
        self.assertEqual(player.uid, "1")  # Check if the UID is correct

    def test_player_name(self):
        """
        Test if the player's name is set and retrieved correctly.
        """
        player = Player("1", "John")
        self.assertEqual(player.name, "John")  # Check if the name is correct

    def test_add_password(self):
        player = Player("1", "John")
        player.add_password("Banana123!")
        self.assertTrue(player._password is not None) # Check if the password was hashed and stored

    def test_verify_password(self):
        player = Player("1", "John")
        player.add_password("Banana123!")
        self.assertTrue(player.verify_password("Banana123!")) # Correct password
        self.assertFalse(player.verify_password("WrongPassword!")) # Incorrect password

if __name__ == "__main__":
    unittest.main()  # Run the unit tests
