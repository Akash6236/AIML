# Program 1(a): Student Result Analysis using conditional statements

name = input("Enter student name: ")

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter subject {i} marks: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if any(mark < 35 for mark in marks):
    print("Result: FAIL")
else:
    print("Result: PASS")

    if percentage >= 90:
        grade = "O"
    elif percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    print("Grade:", grade)

    if grade == "O":
        print("Eligible for Scholarship")
