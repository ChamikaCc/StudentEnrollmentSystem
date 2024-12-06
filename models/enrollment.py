class Enrollment:
    def __init__(self, enrollmentId, student, course, enrollmentDate):
        self.enrollmentId = enrollmentId
        self.student = student
        self.course = course
        self.enrollmentDate = enrollmentDate

    def assignGrade(self, grade):
        print(f"Assigned grade {grade} to {self.student.name} for {self.course.courseName}")
