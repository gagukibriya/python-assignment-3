class Student :
    def __init__(self,name,student_id,email,age,department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department

    def get_mail(self):
        return self.__email

    def display_info(self):
        print("Student Name :", self.name)
        print("Student ID:", self.student_id)
        print("Email :",self.__email)
        print("Student Age :",self.age)
        print("Department :",self.department)

    def calculate_result(self,year_1=0,year_2=0,year_3=0,year_4=0):
        total = year_1 + year_2 + year_3 + year_4
        return total

    def get_student_type(self):
        print("The are not valid.")


class UndergraduateStudent(Student):
    def __init__ (self,name,student_id,email,age,department,semester):
        super().__init__(name,student_id,email,age,department)
        self.semester = semester

    def get_student_type (self):
        print("This student are Undergraduate.")


class GraduateStudent(Student):
    def __init__(self,name,student_id,email,age,department,research_topic):
        super().__init__(name,student_id,email,age,department)
        self.research_topic = research_topic

    def get_student_type(self):
        print("This Student are Graduated.")


student_1 = Student("Kibriya",1201,"test@gmail.com","24","CSE")

# print(student_1.calculate_result(20,20,30))

std_2 = GraduateStudent(
    name="Bokkar",
    email="test2@gmail.com",
    student_id=1202,
    age=67,
    department="English",
    research_topic="News"
)

# print(std_2.name)

std_3 = UndergraduateStudent(
    name="Sakib",
    email="sakib@gmail.com",
    student_id=1200,
    age=22,
    department="BBA",
    semester="6th"
)


# std_2.get_student_type()
# std_3.get_student_type()

# student_1.display_info()
# std_2.display_info()
# std_3.display_info()