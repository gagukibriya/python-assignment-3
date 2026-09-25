class Student :
    def __init__(self,name,student_id,email,age,department):
        self.name = name
        self.student = student_id
        self.email = email
        self.age = age
        self.department = department

    def desplay_info(self,needs):
        print(needs)

    def calculate_result(self,year_1,year_2,year_3,year_4):
        sum = year_1 + year_2 + year_3 + year_4
        return sum

    def get_student_type(self):
        print("The are not valid.")


class UndergraduateStudent(Student):
    def __init__ (self,semester):
        self.semester = semester

    def get_student_type (self):
        print("This student are Undergraduate.")


class GraduateStudent(Student):
    def __init__(self,research_topic):
        self.research_topic = research_topic

    def get_student_type(self):
        print("This Student are Graduated.")


student_1 = Student("Kibriya",1201,"test@gmail.com","24","CSE")

# student_1.desplay_info(student_1.name)

student_2 = GraduateStudent()