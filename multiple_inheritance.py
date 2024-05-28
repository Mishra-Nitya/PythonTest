class Teacher:
    def Teacher(self):
        print("this person is a teacher")
class Student:
    def Student(Self):
        print("this persn is a student")
class YouTuber:
    def YouTuber(self):
        print("this person is a YouTuber")
class Person(Teacher, Student, YouTuber):
    pass
a = Person()
a.Student()
a.Teacher()
a.YouTuber()