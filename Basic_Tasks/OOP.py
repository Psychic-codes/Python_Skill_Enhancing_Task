class Student:
    def __init__(self, name, age, grades):
        self.name = name  
        self.age = age    
        self.grades = grades 

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def average(self):
        if len(self.grades) > 0:
            avg = sum(self.grades) / len(self.grades)
            return avg
        else:
            return 0

student1 = Student("Veer", 20, [85, 90, 78, 92, 88])

student1.display()

avg = student1.average()
print(f"Average Grade: {avg:.2f}")
