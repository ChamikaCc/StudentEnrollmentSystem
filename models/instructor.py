class Instructor:
    def __init__(self, instructorId, name, email):
        self.instructorId = instructorId
        self.name = name
        self.email = email

    def assignCourse(self, course):
        print(f"Instructor {self.name} assigned to course {course.courseName}")

    def createAssignment(self, assignment):
        print(f"Assignment '{assignment.title}' created for course {assignment.course.courseName}")
