# player_list_test.py

import unittest
from app.player_list import PlayerList
from app.player import Player

class TestPlayerList(unittest.TestCase):
    def test_is_empty(self):
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty())  # List should be empty initially

    def test_insert_at_head(self):
        player_list = PlayerList()
        player1 = Player("1", "John")
        player2 = Player("2", "Bob")

        # Insert into an empty list
        player_list.insert_at_head(player1)
        self.assertEqual(player_list._head.player.uid, "1")
        self.assertEqual(player_list._tail.player.uid, "1")

        # Insert into a non-empty list
        player_list.insert_at_head(player2)
        self.assertEqual(player_list._head.player.uid, "2")
        self.assertEqual(player_list._head.next.player.uid, "1")
        self.assertEqual(player_list._tail.player.uid, "1")

if __name__ == "__main__":
    unittest.main()

"""
The test checks if the list is empty initially.

It then tests inserting nodes into both an empty list and a non-empty list, 
ensuring that the head and tail pointers are correctly updated.
"""
