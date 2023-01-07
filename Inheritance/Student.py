from Inheritance.Person import Person


class Student(Person):
    def __init__(self, id, name, class1, year):
        self.class1 =class1
        self.year = year
        Person.__init__(self,id ,name)
    def display(self):
        print("ID =",self.id,",Name =",self.name, ",class =",self.class1," ,year =",self.year)


student = Student(12,"Chorn Thoen","A5",2)
