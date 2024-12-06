class Course:
    def __init__(self, courseId, courseName, credits):
        self.courseId = courseId
        self.courseName = courseName
        self.credits = credits
        self.students = []
        self.instructors = []

    def addStudent(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to course {self.courseName}")

    def assignInstructor(self, instructor):
        self.instructors.append(instructor)
        print(f"Instructor {instructor.name} assigned to course {self.courseName}")
