from datetime import date
from models.attendance import Attendance
from models.student import Student
from models.enrollment import Enrollment
from models.grade_report import GradeReport
from models.assignment import Assignment
from models.course import Course
from models.department import Department
from models.instructor import Instructor

if __name__ == "__main__":
    # Create instances
    student = Student(1, "Achira Nadeeshan", "22ug1-0723@sltc.ac.lk")
    course = Course(101, "Python Programming", 3)
    instructor = Instructor(201, "Mr. Vishwa Sandun", "vishwasandun@sltc.ac.lk")

    # Register student and add to course
    student.registerCourse(course)
    course.addStudent(student)
    course.assignInstructor(instructor)

    # Create and submit an assignment
    assignment = Assignment(1, "Tutorial 01", "Net Present Value Analysis", date(2024, 12, 3), course)
    instructor.createAssignment(assignment)
    assignment.submitAssignment()

    # Generate grade report
    grade_report = GradeReport(1, student, course, "A")
    grade_report.generateReport()

    # Mark attendance
    attendance = Attendance(1, student, course, date(2024, 11, 29))
    attendance.markPresent()

input("Press Enter to continue...")