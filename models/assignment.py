class Assignment:
    def __init__(self, assignmentId, title, description, dueDate, course):
        self.assignmentId = assignmentId
        self.title = title
        self.description = description
        self.dueDate = dueDate
        self.course = course

    def submitAssignment(self):
        print(f"Assignment '{self.title}' submitted for course {self.course.courseName}")
