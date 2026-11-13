
students = {}


def Add_Student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    if roll in students:
        print("Student already exists!")
        return

    marks = []
    subjects = int(input("How many subjects? "))

    for i in range(subjects):
        mark = int(input(f"Enter mark for subject {i + 1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / subjects

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
    elif average >= 35:
        grade = "E"
    else:
        grade = "Fail"

    students[roll] = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    print("Student added successfully!")


def View_All_Students():
    if not students:
        print("No students found!")
        return

    print("\n===== ALL STUDENTS =====")

    for roll, student in students.items():
        print("--------------------------")
        print("Roll Number:", roll)
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])


def Search_Student():
    roll = input("Enter roll number to search: ")

    if roll in students:
        student = students[roll]

        print("\nStudent Details")
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
    else:
        print("Student not found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Add_Student()

    elif choice == "2":
        View_All_Students()

    elif choice == "3":
        Search_Student()

    elif choice == "4":
        print("Program closed!")
        break

    else:
        print("Invalid choice! Try again.")

