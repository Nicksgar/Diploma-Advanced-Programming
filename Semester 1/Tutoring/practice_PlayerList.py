# app/player_list.py
class Player:
    def __init__(self, name, uid):
        self.__name = name  # Making attributes private - _ = private __ = extra private
        self.__uid = uid

    def get_name(self):
        return self.__name

    def get_uid(self):
        return self.__uid


class Node:
    def __init__(self, player):
        self.__player = player  # The player object
        self.__next = None  # Pointer to the next node in the list
        self.__prev = None  # Pointer to the previous node in the list

    # Getter methods for the private attributes
    def get_player(self):
        return self.__player

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    # Setter methods for the private attributes
    def set_next(self, next_node):
        self.__next = next_node

    def set_prev(self, prev_node):
        self.__prev = prev_node


class PlayerList:
    def __init__(self):
        self.__head = None  # The head (first node) of the list
        self.__tail = None  # The tail (last node) of the list

    def append(self, player):
        new_node = Node(player)
        if self.__head is None:  # If the list is empty
            self.__head = new_node  # The new node is the head
            self.__tail = new_node  # The new node is also the tail
        else:  # If the list is not empty
            self.__tail.set_next(new_node)  # The current tail's next pointer points to the new node
            new_node.set_prev(self.__tail)  # The new node's previous pointer points to the current tail
            self.__tail = new_node  # The new node becomes the new tail

    def print_list(self):
        current = self.__head  # Start from the head of the list
        while current:  # While there are nodes in the list
            player = current.get_player()
            print(f"Player Name: {player.get_name()}, UID: {player.get_uid()}")  # Print player details
            current = current.get_next()  # Move to the next node


# Creating a doubly linked list of Player objects
if __name__ == "__main__":
    player_list = PlayerList()
    player_list.append(Player(name='King', uid='1'))
    player_list.append(Player(name='Sarah', uid='2'))
    player_list.append(Player(name='Greg', uid='3'))
    player_list.append(Player(name='Jess', uid='4'))
    player_list.append(Player(name='Pip', uid='5'))
    player_list.append(Player(name='Jim', uid='6'))
    player_list.append(Player(name='Jimbo', uid='7'))
    player_list.print_list()
