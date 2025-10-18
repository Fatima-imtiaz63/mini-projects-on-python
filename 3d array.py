import numpy as np
marks = np.array([[78, 89, 65],
                  [76, 87, 65],
                  [45, 65, 76],
                  [98, 92, 56],
                  [34, 56, 78]])
print("Students Marks:\n", marks)
Total_marks = np.sum(marks, axis=1)
print("\nTotal marks of each student:", Total_marks)
average_marks = np.mean(marks, axis=1)
print("\n ")