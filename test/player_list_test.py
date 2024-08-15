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

    def test_insert_at_tail(self):
        player_list = PlayerList()
        player1 = Player("1", "John")
        player2 = Player("2", "Bob")

        # Insert into an empty list
        player_list.insert_at_tail(player1)
        self.assertEqual(player_list._head.player.uid, "1")
        self.assertEqual(player_list._tail.player.uid, "1")

        # Insert into a non-empty list
        player_list.insert_at_tail(player2)
        self.assertEqual(player_list._tail.player.uid, "2")
        self.assertEqual(player_list._head.player.uid, "1")

    def test_delete_from_head(self):
        player_list = PlayerList()
        player1 = Player("1", "John")
        player_list.insert_at_head(player1)
        removed_node = player_list.delete_from_head()
        self.assertEqual(removed_node.player.uid, "1")
        self.assertTrue(player_list.is_empty())

    def test_delete_from_tail(self):
        player_list = PlayerList()
        player1 = Player("1", "John")
        player_list.insert_at_tail(player1)
        removed_node = player_list.delete_from_tail()
        self.assertEqual(removed_node.player.uid, "1")
        self.assertTrue(player_list.is_empty())

    def test_delete_by_key(self):
        player_list = PlayerList()
        player1 = Player("1", "John")
        player2 = Player("2", "Bob")
        player_list.insert_at_head(player1)
        player_list.insert_at_tail(player2)

        # Deleting head
        removed_node = player_list.delete_by_key("1")
        self.assertEqual(removed_node.player.uid, "1")
        self.assertEqual(player_list._head.player.uid, "2")

        # Deleting tail
        removed_node = player_list.delete_by_key("2")
        self.assertEqual(removed_node.player.uid, "2")
        self.assertTrue(player_list.is_empty())

    def test_display(self):
        player_list = PlayerList()
        player1 = Player("1", "John")
        player2 = Player("2", "Bob")
        player3 = Player("3", "Alice")

        player_list.insert_at_head(player1)
        player_list.insert_at_tail(player2)
        player_list.insert_at_tail(player3)

        # Test display forward
        print("\nDisplaying list forward:")
        player_list.display(forward=True)

        # Test display backward
        print("\nDisplaying list backward:")
        player_list.display(forward=False)

if __name__ == "__main__":
    unittest.main()

"""
The test checks if the list is empty initially.

It then tests inserting nodes into both an empty list and a non-empty list, 
ensuring that the head and tail pointers are correctly updated.
"""
