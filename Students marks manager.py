def calculator_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average
student_name = "Fatima"
age = 20
marks = [85, 90, 78, 98, 88]
avg =calculator_average(marks)
print("Student name:", student_name)
print("Age:", age)
print("marks:", marks)
print("Average Marks;", avg)

if avg >= 85:
    grade = "A"
elif avg >= 70:
    grade = "B"
else:
    grade = "C"
    print("Grade:", grade)