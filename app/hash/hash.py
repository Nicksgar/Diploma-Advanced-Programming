#app/hashing.py

"""


"""
array_size = 15

"""
def ten_hash(data: str, size: int) -> int:
    sum_digit = 0
    for c in data:
        sum_digit += int(c)  # Assuming data contains digits
    return sum_digit % size

array_size = 10  # Define the size of the array
array = [None] * array_size

my_dict = {"110": "john", "151": "Tanmay", "205": "raj"}
print(my_dict{"110"})
print my_dict.values()
print my_dict.keys()
print my_dict.items()
print(my_dict.get("110"))

for k,v in my_dict.items():
    array[ten_hash(k)] = v
    print(array[ten_hash(k)]) f (ten_hash(k) =)')
    print(array)

"""

def ten_hash(data: str, size: int) -> int:
    sum_digit = 0
    for c in data:
        sum_digit += int(c)  # Assuming data contains digits
    return sum_digit % size

array_size = 10  # Define the size of the array
array = [None] * array_size

my_dict = {"110": "john", "151": "Tanmay", "205": "raj"}

# Corrected print statements
print(my_dict["110"])
print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())
print(my_dict.get("110"))

for k, v in my_dict.items():
    hashed_index = ten_hash(k, array_size)
    array[hashed_index] = v
    print(f"{v} stored at array index {hashed_index}")
    print(array)
