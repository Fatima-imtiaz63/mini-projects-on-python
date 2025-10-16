def take_student_data():
    student = {}
    n = int(input("How many students do you want to add?"))
    for i in range(n):
        name = input(f"/n enter the name of students {i+1}")
        marks = []
        for j in range(3):
            marks = int(input(f"/n enter marks for subject {j+1} (out of 100): "))
            marks.append(marks)
            student[name] = marks
            return student
        def display_data(students):
            print("/n ---student data ---")
            for name , marks, in students.item():
                print(f"{name}: {marks}")
        def calculate_result(students):
            print("/n---student result---")
            for name, marks in student.items():
                total = sum(marks)
                avg = total / len(marks)
                highest = max(marks)
                lowest = min(marks)
                print(f"/n student: {name}")
                print(f"/n Average: {avg: .2f}")
                print(f"higest marks: {highest}")
                print(f"Lowest marks: {lowest}")