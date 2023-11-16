class Student:
    def __init__(self, id, name, group, year):
        self.id = id
        self.name = name
        self.group = group
        self.year = year

    def display(self):
        print("ID =", self.id, "Name =", self.name, ",Group =", self.group, ",Year = ", self.year)


student = Student(101, "Chorn Thoen", "A5", 2)
student.display()

# class Triangle:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def triangle(self):
#         return self.x*self.y*self.z
#
#     def display(self):
#         print("Triangle = ",self.triangle())
#
#
# tr = Triangle(2,4,4)
# tr.display()
# tr1 = Triangle
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z: "))
#
# tr1 = Triangle(x,y,z)
# tr1.display()
