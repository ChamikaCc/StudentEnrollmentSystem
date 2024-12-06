class Department:
    def __init__(self, departmentId, departmentName):
        self.departmentId = departmentId
        self.departmentName = departmentName
        self.courses = []
        self.instructors = []

    def addCourse(self, course):
        self.courses.append(course)
        print(f"Course {course.courseName} added to department {self.departmentName}")

    def addInstructor(self, instructor):
        self.instructors.append(instructor)
        print(f"Instructor {instructor.name} added to department {self.departmentName}")
