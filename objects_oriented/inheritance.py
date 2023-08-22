from typing import Any


print("1. property")
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    

class WorkingStudent(Student): #inheritance, because gets stufs from student to use in workingstudents
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property #validate something to interact 
    def weekly_salary(self):
        return self.salary * 37.5
    
        
rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.weekly_salary)

print("2. staticmethod")

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
       return f'<FixedFloat {self.amount:.2f}>'
    
    @staticmethod 
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)
    
new_number = FixedFloat.from_sum(19.574, 0.789)
print(new_number)

print("3. fix euro")

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'
    
money = Euro(18.7566)
print(money)