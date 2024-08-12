#app/pearson_hash.py

#first create an empty table of 25 bytes
#shuffle the hash table
#perform exort operations between the hash value and the given character

#hash table project 2
"""
class Pearsonhasher:
    def __init__(self):
        self._table = list(range(0, 256))

def shuffle_table(self):
    shuffle(self._table)

def pearson_hash(self, data: str):
  if isinstance(data, str)
    data = bytes(data, encoding='utf8')
    hash_value = 0
    e in data
    for byte in data:
        hash_value = self._table{hash_value ^ byte}
    return hash_value

#declare everify method

def verify_method(self, data: str. hash_value: str) -> bool
return pearson_hash(data) == hash_value

"""

import random

class PearsonHasher:
    def __init__(self):
        self._table = list(range(0, 256))
        self.shuffle_table()

    def shuffle_table(self):
        random.shuffle(self._table)

    def pearson_hash(self, data: str) -> int:
        if isinstance(data, str):
            data = bytes(data, encoding='utf8')
        hash_value = 0
        for byte in data:
            hash_value = self._table[hash_value ^ byte]
        return hash_value

    # Declare verify method
    def verify_method(self, data: str, hash_value: int) -> bool:
        return self.pearson_hash(data) == hash_value

# Example usage
hasher = PearsonHasher()
data = "hello"
hash_value = hasher.pearson_hash(data)
print(f"Hash value for '{data}' is {hash_value}")

# Verify the hash value
is_valid = hasher.verify_method(data, hash_value)
print(f"Verification result for '{data}': {is_valid}")




