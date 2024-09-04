# player_list_test.py

import unittest
from app.player_list import PlayerList
from app.player import Player

class TestPlayerList(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("1", "John")
        self.player2 = Player("2", "Bob")
        self.player3 = Player("3", "Alice")

        self.player_list = PlayerList()    # create an instance of playerList

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

        # check forward display:
        current = self.player_list._head  # start from the head of the list
        prev_uid = None    # Prev UID is None initially for the head Node

        while current:
            next_uid = current.next.player.uid if current.next else None   # Determine the next UID if it exists, None

            self.assertEqual(current.prev.player.uid if current.prev else None, prev_uid)
            # Assert the current node's prev pointer matches the prev UID

            self.assertEqual(current.next.player.uid if current.next else None, next_uid)
            # Assert the current node's next pointer matches the next UID

            prev_uid = current.player.uid     # updating the prev_uid to teh current node's UID for the next Iteration
            current = current.next    # Move to the next node in the list

        # check Backward Display:
        current = self.player_list._tail
        next_uid = None
        while current:
            prev_uid = current.prev.player.uid if current.prev else None  # Determine the prev  UID if it exists, None

            self.assertEqual(current.next.player.uid if current.next else None, next_uid)
            # Assert the current node's prev pointer matches the prev UID

            self.assertEqual(current.prev.player.uid if current.prev else None, prev_uid)
            # Assert the current node's next pointer matches the next UID

            next_uid = current.player.uid  # updating the next_uid to teh current node's UID for the next Iteration
            current = current.prev  # Move to the prev node in the list

        # Print and check forward display
        print("\nDisplaying list forward after inserting players:")
        print(player_list.display(forward=True))  # Ensure this actually prints the output

        # Print and check backward display
        print("\nDisplaying list backward after inserting players:")
        print(player_list.display(forward=False))  # Ensure this actually prints the output

        if __name__ == "__main__":
            unittest.main()

        """
        The test checks if the list is empty initially.

        It then tests inserting nodes into both an empty list and a non-empty list, 
        ensuring that the head and tail pointers are correctly updated.
        """

    # The print functions werent printing correctly below because they
    # where missing print before player_list.display(forward=True)

    # Test display forward
    # print("\nDisplaying list forward:")
    # player_list.display(forward=True)

    # Test display backward
    # print("\nDisplaying list backward:")
    # player_list.display(forward=False)
