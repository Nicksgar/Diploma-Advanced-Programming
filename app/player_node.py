# app/player_node.py
from app.player import Player # importing player class

class PlayerNode:
    def __init__(self, player: Player):
        """
        Initialize a node to hold a player and pointers to the next and previous nodes.
        Args:
            player (Player): The player object contained in the node.
        """
        self._player = player  # The player object
        self._next = None  # Pointer to the next node
        self._prev = None  # Pointer to the previous node

    @property
    def player(self):
        """
        Get the player object in the node.
        Returns:
            Player: The player object.
        """
        return self._player

    @property
    def next(self):
        """
        Get the next node.
        Returns:
            PlayerNode: The next node in the list.
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Set the next node.
        Args:
            node (PlayerNode): The next node to set.
        """
        self._next = node

    @property
    def prev(self):
        """
        Get the previous node.
        Returns:
            PlayerNode: The previous node in the list.
        """
        return self._prev

    @prev.setter
    def prev(self, node):
        """
        Set the previous node.
        Args:
            node (PlayerNode): The previous node to set.
        """
        self._prev = node

    @property
    def key(self):
        """
        Get the unique ID of the player.
        Returns:
            str: The player's unique ID.
        """
        return self._player.uid

    def __str__(self):
        """
        Return a string representation of the node.
        Returns:
            str: Human-readable string representing the node.
        """
        return str(self._player)
