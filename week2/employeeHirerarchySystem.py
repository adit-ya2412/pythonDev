class Employee:
    empId_counter=1001
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.employee_id=Employee.empId_counter
        Employee.empId_counter+=1
        
    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    def give_raise(self,percentage):
        self.salary+=(self.salary)*percentage/100


class Developer(Employee):

    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.programming_language=programming_language

    def display_info(self):
        return  f"{super().display_info() },and codes in :{self.programming_language}"
    
    def write_code(self):
        return f"{self.name} is coding in {self.programming_language}"
    

class Manager(Employee):
    def __init__(self, name, salary,team_count):
        self.team_count=team_count
        super().__init__(name, salary)
    def display_info(self):
        parent_info=super().display_info()
        return f"{parent_info} and manages : {self.team_count} people"
    def manage_team(self):
        return f"{self.name} managing {self.team_count} people"
    def give_raise(self, percentage):
        return super().give_raise(percentage+10) 

class BonusEmployee(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus=bonus
    def display_info(self):
        return f"The employee name is {self.name} and yearly bonus is {self.bonus}"


m1=Manager("Rohan",100000,12)
e1=Developer("Aditya",100000,"Java")
b1=BonusEmployee("Aditi",100023,10009)

employees=[
    Manager("Rohan",100000,12),
    Developer("Aditya",100000,"Java"),
    BonusEmployee("Aditi",100023,10009)
]
for e in employees:
    print(e.display_info())

print(m1.employee_id)
print(e1.employee_id)
print(e1.display_info())
print(e1.write_code())
print(m1.display_info())
print(m1.manage_team())
print(m1.give_raise(10))
print(e1.give_raise(10))
print(m1.display_info())
print(e1.display_info())
