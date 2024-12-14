class Course:
    def __init__(self, course_id, name, year, section):
        self.course_id = course_id
        self.name = name
        self.year = year
        self.section = section
        self.enrolled_students = []

    def __str__(self):
        return (f"ID: {self.course_id}, Name: {self.name}, Year: {self.year}, "
                f"Section: {self.section}, Enrolled Students: {len(self.enrolled_students)}")

def add_course(courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        year = int(input("Enter year level: "))
        section = input("Enter section: ")
        course = Course(course_id, name, year, section)
        courses.append(course)
        print("Course added successfully!")

def enroll_student(courses):
        course_id = input("Enter course ID to enroll a student in: ")
        for course in courses:
            if course.course_id == course_id:
                student_name = input("Enter student name: ")
                course.enrolled_students.append(student_name)
                print(f"Student '{student_name}' enrolled successfully in {course.name}.")
                return
        print("Course not found.")

def display_courses(courses):
        if not courses:
            print("No courses available.")
        else:
            print("Courses List:")
            for course in courses:
                print(course)

def display_students_in_course(courses):
        course_id = input("Enter course ID to display enrolled students: ")
        for course in courses:
            if course.course_id == course_id:
                if not course.enrolled_students:
                    print(f"No students enrolled in {course.name}.")
                else:
                    print(f"Students enrolled in {course.name}:")
                    for student in course.enrolled_students:
                        print(student)
                return
        print("Course not found.")

def main():
        courses = []
        while True:
            print("\nCourse Enrollment Menu")
            print("1. Add Course")
            print("2. Enroll Student")
            print("3. Display Courses")
            print("4. Display Students in Course")
            print("5. Exit")
            choice = input("Enter your choice: ")
           
            if choice == "1":
                add_course(courses)
            elif choice == "2":
                enroll_student(courses)
            elif choice == "3":
                display_courses(courses)
            elif choice == "4":
                display_students_in_course(courses)
            elif choice == "5":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
        main()