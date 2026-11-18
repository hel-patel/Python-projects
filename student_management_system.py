
class Student:
    def __init__(self):
        self.students = []

    # Add Student
    def add_student(self):
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = [roll, name, age, course]
        self.students.append(student)

        print("Student Added Successfully!")

    # Display Students
    def display_student(self):
        if len(self.students) == 0:
            print("No Student Found!")
        else:
            for s in self.students:
                print("\nRoll Number:", s[0])
                print("Name:", s[1])
                print("Age:", s[2])
                print("Course:", s[3])

    # Search Student
    def search_student(self):
        roll = input("Enter Roll Number: ")

        for s in self.students:
            if s[0] == roll:
                print("Student Found!")
                print("Name:", s[1])
                print("Age:", s[2])
                print("Course:", s[3])
                return

        print("Student Not Found!")

    # Delete Student
    def delete_student(self):
        roll = input("Enter Roll Number: ")

        for s in self.students:
            if s[0] == roll:
                self.students.remove(s)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")


# Main Program
obj = Student()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        obj.add_student()

    elif choice == "2":
        obj.display_student()

    elif choice == "3":
        obj.search_student()

    elif choice == "4":
        obj.delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
