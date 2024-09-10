# app/player.py

""" Notes:
__init__ is the constructor method that initializes a new instance
of the Player class with a unique ID (uid) and a name (name).

@property decorators are used to define
getter methods for the private instance variables _uid and _name.

__str__ is a special method that returns
a human-readable string representation of the player object.

"""

class Player:
    def __init__(self, uid, name):
        """
        Initialize a new player with a unique ID and name.
        Args:
            uid (str): Unique identifier for the player.
            name (str): Name of the player.
        """
        self._uid = uid  # Private instance variable for player ID
        self._name = name  # Private instance variable for player name

    @property
    def uid(self):
        """
        Get the player's unique ID.
        Returns:
            str: The player's unique ID.
        """
        return self._uid

    @property
    def name(self):
        """
        Get the player's name.
        Returns:
            str: The player's name.
        """
        return self._name

    def __str__(self):
        """
        Return a string representation of the player.
        Returns:
            str: Human-readable string representing the player.
        """
        return f"Player(uid={self._uid}, name={self._name})"

if __name__ == "__main__":
    # Example usage: create and print a player
    player = Player("1", "Alice")
    print(player)