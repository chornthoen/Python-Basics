from Inheritance.Person import Person


class Teacher(Person):
    def __init__(self, id, name, salary, subject):
        super().__init__(id, name)
        self.salary = salary
        self.subject = subject

    def display(self):
        print("ID =", self.id, "Name =", self.name,
              "Salary =", self.salary, "Subject =", self.subject)


teacher = Teacher(1010, "Heng sok", 500, "Python")
teacher.display()
