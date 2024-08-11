# app/player_node.py

class player_node:
    def __init__(self, player):
        """
        Initialize a node to hold a player and pointers to the next and previous nodes.
        Args:
        player (Player): The player object contained in the node.
        """
        self.player = player  # The player object
        self._next = None # Pointer to the next node
        self._prev = None # Pointer to the previous node
@property
def player(self):
    """
     Get the player object in the node.
        Returns:
            Player: The player object.
            :param: This keyword is used to describe a parameter of a function or method.
            :return: This keyword is used to describe the return value of a function or method.
    :param self:
    :return:
    """
@property
def next(self):
    """
    Get the next node in the node.
    playernode: The next node in the node.
    :return: This keyword is used to describe a parameter of a function or method.
    """
    return self._next

@next.setter
def next(self, node):
    """
    Set the next node in the node.
    node (PlayerNode): The next node to set.
    """
    self._next = node
@property
    def prev(self):
        """
        Get the previous node.
        Returns:
            PlayerNode: The previous node.
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