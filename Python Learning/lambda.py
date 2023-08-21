divide = lambda x, y: x / y

print(divide(5,2))

def average(sequence):
    return sum(sequence) / len(sequence)

students = [
    {"name": "Agatha", "grades": (80, 20, 80, 100)},
    {"name": "Cyntia", "grades": (70, 26, 80, 100)},
    {"name": "Bruno", "grades": (45, 23, 60, 100)},
    {"name": "Pedro", "grades": (25, 27, 90, 100)},
]

for student in students:
    print(average(student["grades"]))