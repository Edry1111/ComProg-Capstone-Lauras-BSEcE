class Student:
    def __init__(self, student_id, name, course, grade1, grade2, grade3, grade4):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grades = [grade1, grade2, grade3, grade4]

    def update_grade(self, grade_index, new_grade):
        if 0 <= grade_index < len(self.grades):
            self.grades[grade_index] = new_grade
        else:
            print("Invalid Grade.")

    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
def add_student(students):
        student_id = input("Enter your Student ID: ")
        name = input("Enter Student Name: ")
        course = input("Enter course: ")
        grades = [float(input(f"Enter grade {i+1} (0-100): ")) for i in range(4)]
        students.append(Student(student_id, name, course, *grades))
        print(f"Student {name} added successfully!")

def update_student_grade(students):
        student_id = input("Enter the student ID to update grades: ")
        for student in students:
            if student.student_id == student_id:
                print(f"Grades: {student.grades}")
                grade_index = int(input("Enter grade index to update (0-4): "))
                new_grade = float(input("Enter new grade (0-100): "))
                student.update_grade(grade_index, new_grade)
                print("Grade updated Successfully!")
                return
            print("Student not found.")

def display_students(students):
        if not students:
            print("No students to display.")
            return
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, Course: {student.course}, Grades: {student.grades}")

def calculate_class_average(students):
        if not students:
            print("No students to calculate average.")
            return
        total_average = sum(student.average_grade() for student in students) / len(students)
        print(f"Class average grade: {total_average:.2f}")

def main():
        students = []
        while True:
            print("Menu:")
            print("1. Add a student")
            print("2. Update a student's grade")
            print("3. Display all students with their grades")
            print("4. Calculate and display class average")
            print("5. Exit")
            choice = input("Enter your choice: ")
           
            if choice == "1":
                add_student(students)
            elif choice == "2":
                update_student_grade(students)
            elif choice == "3":
                display_students(students)
            elif choice == "4":
                calculate_class_average(students)
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
        main()
