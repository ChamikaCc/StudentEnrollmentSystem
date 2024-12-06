# Student Enrollment System

## Overview
The Student Enrollment System is a Python-based application designed to efficiently manage student information, course offerings, enrollments, and related administrative tasks. It streamlines the enrollment process, making it user-friendly for students and administrators alike.

## Features
- Automates the student enrollment process
- Provides real-time access to accurate data
- User-friendly interface for students to:
  - Register for courses
  - View schedules
  - Monitor academic progress
- Administrative tools to:
  - Track enrollments
  - Generate reports
  - Manage course capacities

## Project Structure
```
student_enrollment_system/
├── models/
│   ├── __init__.py            # Initializes the models package
│   ├── attendance.py          # Attendance class
│   ├── student.py             # Student class
│   ├── enrollment.py          # Enrollment class
│   ├── grade_report.py        # GradeReport class
│   ├── assignment.py          # Assignment class
│   ├── course.py              # Course class
│   ├── department.py          # Department class
│   └── instructor.py          # Instructor class
└── main.py                    # Demonstrates the interaction between classes
```

## Key Entities
1. **Student**: Manages student attributes like ID, name, and email, and handles course registration.
2. **Course**: Represents courses with details like course ID, name, and credits, and handles students and instructors.
3. **Enrollment**: Tracks the association between students and courses, along with enrollment dates and grades.
4. **Instructor**: Represents instructors, managing their personal details and assigned courses.
5. **Department**: Handles department-specific operations like managing courses and instructors.
6. **Attendance**: Tracks student attendance for courses.
7. **GradeReport**: Manages grade records for students.
8. **Assignment**: Tracks course assignments and their submissions.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-enrollment-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd student_enrollment_system
   ```
3. Run the `main.py` file to see the interaction between classes:
   ```bash
   python main.py
   ```

## Contributors
### Developed by Group 3

22UG1-0723  H.R.A.N. Dilhara
