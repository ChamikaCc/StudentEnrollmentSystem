class Student:
    def __init__(self, studentId, name, email):
        self.studentId = studentId
        self.name = name
        self.email = email
        self.courses = []

    def registerCourse(self, course):
        self.courses.append(course)
        print(f"{self.name} has registered for {course.courseName}")
