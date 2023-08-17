'''functions that would be embedded in this python file include:
Gradepoint, current semester, good'''

Grade_dictionary = {"A":5, "B":4, "C":3, "D":2, "E":1, "F":0}

def course_grade_point():
    No_of_courses = int(input("How many courses did you take this semeseter: ")) 
    new_gp = 0 
    t_c_unit = 0
    for i in range(No_of_courses):
        course_title = input("Kindly input your course title: ")
        course_grade = int(input("Kindly input your course grade: "))
        course_unit = int(input("Kindly input the course unit: "))
        cogp = course_grade * course_unit 
        new_gp = new_gp + cogp 
        t_c_unit = t_c_unit + course_unit 
    gp = (new_gp * 5)/ (5*t_c_unit) 
    print("Your gp for this semester is: "+ str(gp))
course_grade_point()