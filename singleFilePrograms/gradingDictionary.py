student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
# print(student_scores)
# for keys in student_scores:
#     print(keys)
#     print(student_scores[keys])

student_grades = {

}

for keys in student_scores:
    if student_scores[keys] >= 91:
        student_grades[keys] = keys
        student_grades[keys] = "Outstanding"
    elif student_scores[keys] >= 81 :
        student_grades[keys] = keys
        student_grades[keys] = "Exceeds Expectations"
    elif student_scores[keys] >= 71 :
        student_grades[keys] = keys
        student_grades[keys] = "Acceptable"
    elif student_scores[keys] <= 70 :
        student_grades[keys] = keys
        student_grades[keys] = "Fail"

print(student_grades)
