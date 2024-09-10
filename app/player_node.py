# app/player_node.py
from app.player import Player

class PlayerNode:
    def __init__(self, player=None):
        """
        Initialize a node to hold a player and pointers to the next and previous nodes.
        Args:
            player (Player): The player object contained in the node.
        """
        self._player = player  # Store the player object in the node
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

    @player.setter
    def player(self, value):
        """
        Set the player object in the node.
        Args:
            value (Player): The player object to set.
        """
        self._player = value

    @property
    def key(self):
        return self._player.uid if self._player else None

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

    def __str__(self):
        """
        Return a string representation of the node.
        Returns:
            str: Human-readable string representing the node.
        """
        return f"PlayerNode(player={self._player})"

