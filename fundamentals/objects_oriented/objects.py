#define the obejcts and creat, things that store the data

print("1. class - student")
class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)
    
student_one = Student('Agatha', [70, 80,98, 100])
student_two = Student('Barros', [50, 80,98, 100])

print(student_one.average())

print("\n2. class - movie")

class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    def print_info(self):
        return print(f"<<{self.name}>> by {self.director}")

my_movie = Movie('The Matrix', 'Wachowski')

my_movie.print_info()

print("\n3. class - car")

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
ford = Garage()
ford.cars.append('fiesta')
ford.cars.append('focus')

print(len(ford))
print(ford[0])

for car in ford:
    print(car)

