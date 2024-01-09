class Student:
    def __init__(self,id,name,grade):
        self.id=id
        self.name=name
        self.grade=grade
    def  enroll(self,course):
        self.course=course
    def display(self):
        print("Students data are:")
        print('id:',self.id,'name:',self.name,'grade:',self.grade)
class Teacher:
    def __init__(self,T_id,Tname,Sub):
        self.T_id=T_id
        self.Tname=Tname
        self.Sub=Sub
    def  enroll(self,course):
        self.course=course
    def display(self):
        print("Teachers data are:")
        print('id:',self.T_id,'name:',self.Tname,'grade:',self.Sub)
class Course:
    def __init__(self,C_id,Cname):
        self.C_id=C_id
        self.Cname=Cname
    def display(self):
        print("Course details are:")
        print("Course_id:",self.C_id,'Coursename:',self.Cname)

        
        
obj=Student(1,"abcd","A")
obj.enroll("Btech")
obj.display()

obj1=Teacher(1,"pqrs","B")
obj1.display()

obj2=Course(1001,"Btech")
