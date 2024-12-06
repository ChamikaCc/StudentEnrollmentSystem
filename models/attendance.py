class Attendance:
    def __init__(self, attendanceId, student, course, attendDate):
        self.attendanceId = attendanceId
        self.student = student
        self.course = course
        self.attendDate = attendDate

    def markPresent(self):
        print(f"Marked {self.student.name} as present on {self.attendDate}")

    def markAbsent(self):
        print(f"Marked {self.student.name} as absent on {self.attendDate}")
