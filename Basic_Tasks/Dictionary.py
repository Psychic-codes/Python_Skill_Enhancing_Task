students = {}

def create(student_id, name, age, grades):
    students[student_id] = {"student_id": student_id , "name": name, "age": age, "grades": grades}
    print(f"Student {name} added.")

def view(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"Student_id : {student['student_id']}, Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")
    else:
        print("Student not found.")

def update(student_id,  name=None, age=None, grades=None):
    if student_id in students:
        if name:
            students[student_id]['name'] = name
        if age:
            students[student_id]['age'] = age
        if grades:
            students[student_id]['grades'] = grades
        print("Student updated.")
    else:
        print("Student not found.")

def delete(student_id):
    if student_id in students:
        del students[student_id]
        print("Student deleted.")
    else:
        print("Student not found.")

create(1, "Raj", 20, [85, 90, 78])
create(2, "Om", 22, [88, 92, 85])

view(1)

update(1, age=21, grades=[90, 92, 80])

view(1)

delete(2)

view(2)
