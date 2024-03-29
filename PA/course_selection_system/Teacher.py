from User import User
from Mediator import Mediator
from Course import Course
class Teacher(User):
    def __init__(self, name):
        super().__init__(name, "Teacher")

        self.courses = []
    def create_course(self, name, capacity):
        course = Course(super().username, capacity, name)
        self.courses.append(course)
        return course

    def kick_student(self, course, student):
        return Mediator.kick_student(student, course, self.username)


class Admin_teacher(Teacher):
    def create_student(self, name):
        return Student(name)

    def set_global_scr_req(self, scr):
        return scr

    def view_stu_choice(self, stu):
        return stu

