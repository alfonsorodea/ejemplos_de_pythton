class User:
    name = None
    email = None
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def send_email(self):
        if self.email is not None:
            print("sending email: "+self.email)
        else:
            print("Error")
    def __str__(self):
        return "User: "+self.name+", "+self.email
class Student(User):
        def is_approved(self):
            return self.score>=8
        score = 0
        def __init__(self,name,email, score):
            super().__init__(name, email)
            self.score= score

        def __str__(self):
            return "Student: "+self.name+", "+self.email+" , Score: "+str(self.score)
student1= Student("estudiante1","estq1@utsc.edu.mx", 7)
student1.send_email()
print(user1)
print(student1)
list1= list()
for i in range(10):
    list1.append(
          Student(
                "student" +str(i),
                "email"+str(i)+"@utsc.edu.mx",
                random.randint(6,10)
                )
          )

