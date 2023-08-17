# this helps to create a module for our school calculations

class Unicourse:
    
    def __init__(self, course_code, course_title, course_unit, moderator, prerequisite, origin):
        self.code = course_code
        self.title = course_title
        self.unit = course_unit 
        self.moderator = moderator
        self.precourse = prerequisite
        self.origin = origin

class Student:

    def __init__(self, course_code, grade):
        self.code = course_code
        self.grade = grade

    
    def grade_point(self):
        Grade_dictionary = {"A":5, "B":4, "C":3, "D":2, "E":1, "F":0}
        cogp = Grade_dictionary[self.grade.upper()]
        return cogp

    c_grade_point = property(grade_point)

    