class GradeReport:
    def __init__(self, reportId, student, course, grade):
        self.reportId = reportId
        self.student = student
        self.course = course
        self.grade = grade

    def generateReport(self):
        print(f"Grade Report for {self.student.name}:\nCourse: {self.course.courseName}\nGrade: {self.grade}")