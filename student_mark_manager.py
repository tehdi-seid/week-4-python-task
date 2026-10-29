student_marks = [75, 80, 65, 90, 85]

new_student_marks=student_marks

student_marks_copy = student_marks.copy()

student_marks_copy.append(95)


print(student_marks)
print(new_student_marks)
print(student_marks_copy)

print(student_marks is new_student_marks)
print(student_marks is student_marks_copy)
print(student_marks == student_marks_copy)