def GpaCalculation(grades):
    points = 0
    i = 0
    gradepoints = {"A":4.00, "A-":3.67, "B+":3.33, "B":3.00, "B-": 2.67, "C+":2.33, "C": 2.00, "C-":1.67, "D":1.00, "F":0.00}
    # Gpa values
    if grades != []:
        for grade in grades:
            points += gradepoints[grade]
        gpa = points / len(grades)
        return gpa
    else:
        return None
# algorithm of grading

grades = ["A", "C+", "B-", "A", "F"]
print(GpaCalculation(grades))

grades = ["B-", "B", "C+", "A-", "B+", "C"]
print(GpaCalculation(grades))
grades = ["A", "A+", "A-", "B", "B+", "B-"]
print(GpaCalculation(grades))
# and pre-created grade them selfs