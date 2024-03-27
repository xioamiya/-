class Student:
    def __init__(self, name, student_id, courses=None):
        self.name = name
        self.student_id = student_id
        self.courses = courses if courses is not None else []

    def view_courses(self):
        print(f"Student {self.name}'s Courses:")
        for course in self.courses:
            print(course)

    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in the course: {course}")

class Administrator:
    def __init__(self):
        self.students = []

    def create_student(self, name, student_id):
        new_student = Student(name, student_id)
        self.students.append(new_student)
        print(f"Student {name} with ID {student_id} created.")
        return new_student

    def view_students(self):
        print("List of Students:")
        for student in self.students:
            print(f"{student.name} - ID: {student.student_id}")

    def assign_course(self, student, course):
        student.enroll_course(course)

def main():
    print("Welcome to the Student Management System!")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    admin = Administrator()

    while True:
        print("\nChoose an option:")
        print("1. Create a new student")
        print("2. View list of students")
        print("3. Enroll student in a course")
        print("4. View student's courses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            admin.create_student(student_name, student_id)

        elif choice == "2":
            admin.view_students()

        elif choice == "3":
            student_id = input("Enter student's ID: ")
            course = input("Enter the course name: ")
            student = next((s for s in admin.students if s.student_id == student_id), None)
            if student:
                admin.assign_course(student, course)
            else:
                print(f"Student with ID {student_id} not found.")

        elif choice == "4":
            student_id = input("Enter student's ID: ")
            student = next((s for s in admin.students if s.student_id == student_id), None)
            if student:
                student.view_courses()
            else:
                print(f"Student with ID {student_id} not found.")

        elif choice == "5":
            print("Exiting the Student Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
