
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Student(Person):
    def __init__(self, id, name, year):
        super().__init__(id, name)
        self.year = year

    def Display(self):
        print("ID =", self.id, " ,Name =", self.name, ",Year =", self.year)


student = Student(1, "dara", 2)
student.Display()


class Teacher(Person):
    def __init__(self, id, name, salary, subject):
        super().__init__(id, name)
        self.salary = salary
        self.subject = subject

    def display(self):
        print("ID =", self.id, ",Name =", self.name,
              ",Salary =", self.salary, ",Subject =", self.subject)


teacher = Teacher(1010, "Heng sok", 500, "Python")
teacher.display()
