# # app/player_node.py
# from app.player import Player # importing player class
#
# class PlayerNode:
#     def __init__(self, data=None):
#         """
#         Initialize a node to hold a player and pointers to the next and previous nodes.
#         Args:
#             player (Player): The player object contained in the node.
#         """
#         self.data = data  # Store the data ino the node
#         self._next = None  # Pointer to the next node
#         self.next = None  # Pointer to the previous node     # correction
#
#     def __repr__(self):
#         """
#         Return the string representation of the PlayerNode inmstance !
#         :return:
#         """
#
#         return f"PlayerNode(data={self.data})"
#
#     def display(self):
#         """ to display the node's data and it's connections
#         """
#         print(f"DATA: {self.data}")    # To Show the data of the prev node if exists
#
#         if self.prev:
#             print(f"PREV: {self.prev.data}")   # Indicate taht there is no prev node
#         else:
#             print(f"PREV : NONE ")
#
#         if self.next:
#             print(f"NEXT: {self.next.data}")  # To Show the data of the next node if exists
#         else:
#             print(f"NEXT : NONE ")
#
#
#
#     @property
#     def player(self) -> Player:
#         """
#         Get the player object in the node.
#         Returns:
#             Player: The player object.
#         """
#         return self._player
#
#
#     # Added-----------
#     @player.setter
#     def player(self, value):
#         """
#         Set the player object in the node.
#         Args:
#             value (Player): The player object to set.
#         """
#         self._player = value
#
#     @property
#     def next(self) -> 'PlayerNode':
#         """
#         Get the next node.
#         Returns:
#             PlayerNode: The next node in the list.
#         """
#         return self._next
#
#     @next.setter
#     def next(self, node: 'PlayerNode'):
#         """
#         Set the next node.
#         Args:
#             node (PlayerNode): The next node to set.
#         """
#         self._next = node
#
#     @property
#     def prev(self) -> 'PlayerNode':
#         """
#         Get the previous node.
#         Returns:
#             PlayerNode: The previous node in the list.
#         """
#         return self._prev
#
#     @prev.setter
#     def prev(self, node: 'PlayerNode'):
#         """
#         Set the previous node.
#         Args:
#             node (PlayerNode): The previous node to set.
#         """
#         self._prev = node
#
#     @property
#     def key(self) -> str:
#         """
#         Get the unique ID of the player.
#         Returns:
#             str: The player's unique ID.
#         """
#         return self._player.uid
#
#     def __str__(self) -> str:
#         """
#         Return a string representation of the node.
#         Returns:
#             str: Human-readable string representing the node.
#         """
#         return str(self._player)


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

