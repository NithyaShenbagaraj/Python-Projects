#student details
Student_id = int(input("Enter student Id: "))
Student_name = input("Enter student name: ")

Marks = {}
Subjects=["Language","English","Maths","Science","Programming"]

for subject in Subjects:
    mark = float(input(f"Enter marks for {subject} :"))
    Marks[subject] = mark
    print(f"Marks for {subject} : {mark}")

Total = sum(Marks.values())
print(f"Total marks: {Total}")
average = Total / len(Marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")

print("=" * 35)
print("         Student Report Card")
print("=" * 35)
print(f"Student ID   : {Student_id}")
print(f"Student Name : {Student_name}")
print("=" * 35)
print(f"{'Subject':<15}: {'Marks':<10}")
for subject, mark in Marks.items():
    print(f"{subject:<15}: {mark:<10}")
print("=" * 35)

print(f"{'Total Marks':<15}: {Total:<10}")
print(f"{'Average':<15}: {average:<10.2f}")
print(f"{'Grade':<15}: {grade:<10}")
print("=" * 35)
