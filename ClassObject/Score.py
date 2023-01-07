class Student:
    def __init__(self, name, python, cpp, db, java, html):

        self.name = name
        self.python = python
        self.cpp = cpp
        self.db = db
        self.java = java
        self.html = html

    def getTotal(self):

        return self.python + self.cpp + self.db + self.java + self.html

    def getAverage(self):

        return self.getTotal() / 5

    def getGrade(self):

        averge = self.getAverage()
        if averge >= 90:
            grade = 'A'
        elif averge >= 80:
            grade = 'B'
        elif averge >= 70:
            grade = 'C'
        elif averge >= 60:
            grade = 'D'
        elif averge >= 50:
            grade = 'E'
        else:
            grade = 'F'
        return grade

    def display(self):

        print("name =", self.name, " ,Python =", self.python, " ,CPP =", self.cpp, " ,Database =", self.db,
              ",Java =", self.java, ",Total =", self.getTotal(), ",Average =", self.getAverage(), ",Grade =",
              self.getGrade())


print("Name of Student.....")

n = input("input name     : ")
p = int(input("input python   : "))
c = int(input("input cpp      : "))
d = int(input("input database : "))
j = int(input("input java     : "))
h = int(input("input html     : "))
student = Student(n, p, c, d, j, h)
student.display()
