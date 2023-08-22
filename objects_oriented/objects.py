#define the obejcts and creat, things that store the data


class Student:
    def __int__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    def average(self):
        return sum(self.grades) / len(self.grades)
    
student_one = Student('Agatha', [70, 80,98, 100])
student_one = Student('Barros', [50, 80,98, 100])

print(student_one.average())
