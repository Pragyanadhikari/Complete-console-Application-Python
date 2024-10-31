# 6. School Management System
# • Description: Develop a console application to manage student records. Implement classes for Student, Course, and Teacher. Include methods for enrolling students in courses and generating grade reports.
# • OOP Concepts: Inheritance (different types of students), Composition (students enrolled in courses), and Encapsulation (managing student information).
from abc import ABC,abstractmethod
class Student(ABC):
    student_count=1
    def __init__(self,name,level,section,roll_number):
        self.student_id='S-12345'+str(Student.student_count)
        Student.student_count+=1
        self.name=name
        self.level=level
        self.section=section
        self.roll_number=roll_number
        self.courses={}
        self.studentType=self.typeOfStudent()
    @abstractmethod
    def typeOfStudent(self):
        pass
    def enroll_courses(self,course):
        if course.course_name not in self.courses:
            self.courses[course.course_name]=0
            course.add_students(self)
        else:
            print(f'Student already enrolled in course.')

    def setGrade(self,course_name,grade):
        if course_name in self.courses:
            self.courses[course_name]=grade
        else:
            print(f'Student not in this course.')
    
    def getGrade(self):
        print(f'Grade of {self.name} are:')
        for course,grade in self.courses.items():
            print(f'Course-{course} Grade-{grade}')
        print()
    def __str__(self):
        return f'Name:{self.name}\nLevel:{self.level}\nRoll number:{self.roll_number}\n'
class TechnicalStudent(Student):
    def __init__(self, name, level, section, roll_number):
        super().__init__(name, level, section, roll_number)
    def typeOfStudent(self):
        self.typeOfStudent="Technical Student"
class TheoryStudent(Student):
    def __init__(self, name, level, section, roll_number):
        super().__init__(name, level, section, roll_number)
    def typeOfStudent(self):
        self.typeOfStudent="Theoretical Student"
class Teacher:
    teacher_count=1
    def __init__(self,name,subject_teaching):
        self.name=name
        self.teacher_id='T-12345'+str(Teacher.teacher_count)
        Teacher.teacher_count+=1
        self.subject_teaching=subject_teaching
    
    def __str__(self):
        return f'Teacher ID:{self.teacher_id}\nTeacher Name:{self.name}\nSubject:{self.subject_teaching}'

class Course:
    def __init__(self,course_name,teacher):
        self.course_name=course_name
        self.teacher=teacher
        self.students=[]
    
    def add_students(self,student):
        if student not in self.students:
            self.students.append(student)
        else:
            print("Student already enrolled.")
    
    def show_students(self):
        if not self.students:
            print(f"No any student enrolled in course {self.course_name}.")
        else:
            print(f'Students enrolled in course {self.course_name}:')
            for student in self.students:
                print(student)
            print()
    
    def __str__(self):
        return f'Course: {self.course_name} \nTeacher name: {self.teacher}\n'

teacher1=Teacher('Hira','OOP')
teacher2=Teacher("Jasmine",'Mathematics')
course1=Course('OOP',teacher1)
course2=Course('Mathematic',teacher2)
student1=TechnicalStudent("Pragyan",'BE','B',56)
student2=TheoryStudent('Gini','BCT','C',1)
course1.add_students(student1)
course1.add_students(student2)
course2.add_students(student2)
student1.enroll_courses(course1)
student2.enroll_courses(course2)
student2.enroll_courses(course1)
student1.setGrade('OOP',90)
student2.setGrade('OOP',87)
student2.setGrade('Mathematic',98)

student2.getGrade()
print(course1)
course1.show_students()
print(course2)
course2.show_students()

