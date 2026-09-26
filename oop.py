class Student :
    def __init__(self,name,student_id,email,age,department):
        self.name = name
        self.student_id = student_id
        self._email = email
        self.age = age
        self.department = department

    def get_mail(self):
        return self._email

    def display_info(self):
        print(self)

    def calculate_result(self,year_1=0,year_2=0,year_3=0,year_4=0):
        sum = year_1 + year_2 + year_3 + year_4
        return sum

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

print(std_2.name)

