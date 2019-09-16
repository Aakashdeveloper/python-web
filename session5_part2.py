class Person():

    def __init__(self,name):
        self.name = name 

    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False


class Employee(Person):
    def isEmployee(self):
        return True


emp = Person('John')
print(emp.getName(), emp.isEmployee())

emp = Employee('Sarah')
print(emp.getName(), emp.isEmployee())



'''class lang():
    pass


javascript = lang()
python = lang()

javascript.framework = 'Angular'
javascript.year= 1992


python.framework = 'Flask'
python.year = 1988

print(javascript.__dict__)
print(python.__dict__)'''