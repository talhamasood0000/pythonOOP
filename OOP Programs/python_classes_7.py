## Practice of OOP

class MyClass:
    a=10
    def __init__(self,name:str,classs:str):
        self.name=name
        self.classs=classs
    
    def comment(self):
        return "This is a comment"
    def check(self):
        a=5

student1=MyClass("Talha","sec-B")

# print(student1.classs)
# print(MyClass.a)
# print(student1.check())

class Employee:                                             #Example:2
   'Common base class for all employees'          #docstring
   empCount = 0                                            # Class attribute
 # Initializer / Instance attributes
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
 # instance method
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
# instance method
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)































