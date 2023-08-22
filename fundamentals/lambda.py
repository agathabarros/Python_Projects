
avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
   "average": avg,
   "total": total,
   "top": top
}
students = [
    {"name": "Agatha", "grades": (80, 20, 80, 100)},
    {"name": "Cyntia", "grades": (70, 26, 80, 100)},
    {"name": "Bruno", "grades": (45, 23, 60, 100)},
    {"name": "Pedro", "grades": (25, 27, 90, 100)},
]

for student in students:
   name = student["name"] 
   grades = student["grades"]

   operation = input("Enter 'average', 'total', or 'top':")
   
   operation_function = operations[operation]
   print(operation_function(grades))

        
