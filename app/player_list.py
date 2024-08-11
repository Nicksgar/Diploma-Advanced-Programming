# app/player_list.py

"""Notes:

__init__ is the constructor method that initializes a new instance
of the PlayerList class with head and tail pointers set to None.

head and tail properties are used to access the head and tail nodes of the list.

is_empty method checks if the list is empty by verifying if the head pointer is None.

"""

class PlayerList:
    def __init__(self):
        """
        Initialize an empty player list with a head pointer.
        """
        self._head = None  # Head of the linked list
        self._tail = None  # Tail of the linked list

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

    def is_empty(self):
        """
        Check if the list is empty.
        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self._head is None  # Return True if head is None
