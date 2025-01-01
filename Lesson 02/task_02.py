class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []
    
    def enroll_student(self, name):
        self.students.append(name)
        print(f"{name} has been enrolled in the {self.course} course.")
    
    def course_details(self):
        print(f"Course: {self.course}")
        print(f"Instructor: {self.instructor}")
        print(f"Number of students: {len(self.students)}")

    def completed_course(self, name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} has completed the course!")
        else:
            print(f"{name} is not enrolled in the course")
        
    def average_grade(self, grades):
        total = sum(grades)
        average = total / len(grades)
        print(f"The average grade is {average}.")


course_input = input("Enter a course: ").lower()
name = input("Enter an instrucuctor: ").lower()
student = input("Enter a name: ").lower()

course = OnlineCourse(course_input, name)
grades = [90, 85, 92, 78, 80]

course.enroll_student(student)
course.course_details()
course.average_grade(grades)