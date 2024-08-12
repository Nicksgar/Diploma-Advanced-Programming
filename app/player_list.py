# app/player_list.py

"""Notes:

__init__ is the constructor method that initializes a new instance
of the PlayerList class with head and tail pointers set to None.

head and tail properties are used to access the head and tail nodes of the list.

is_empty method checks if the list is empty by verifying if the head pointer is None.

"""
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        """
        Initialize an empty player list with a head pointer.
        """
        self._head = None  # Head of the linked list
        self._tail = None  # Tail of the linked list

    def is_empty(self):
        return self._head is None

    def insert_at_head(self, player):
        new_node = PlayerNode(player)  # Creating a new PlayerNode
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

    def insert_at_tail(self, player):
        """
        Inserts the player at the tail of the list.
        :param self:
        :param player: player object to be added to the list.
        :return:
        """
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
    def delete_from_head(self):
        if self.is_empty():
            return None
        removed_node = self._head
        if self._head == self._tail: # Only one node
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = none
        return removed_node

    def delete_from_tail(self):
        if self.is_empty():
            return None
        removed_node = self._tail
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        return removed_node





    @property
    def head(self):
        """
        Get the head node of the list.
        Returns:
            PlayerNode: The head node of the list.
        """
        return self._head

    @property
    def tail(self):
        """
        Get the tail node of the list.
        Returns:
            PlayerNode: The tail node of the list.
        """
        return self._tail
