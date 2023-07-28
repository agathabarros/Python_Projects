friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

for name, age in friends:
    print(f"{name} is {age} years old.")

# Path: structs.py

friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name in friend_ages:
    print(name)

friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for age in friend_ages.values():
    print(age)

