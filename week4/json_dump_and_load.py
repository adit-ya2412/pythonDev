import json
from functools import reduce
from dataclasses import dataclass
employee_json = '''
[
    {
        "name":"Aditya",
        "department":"Engineering",
        "salary":85000
    },
    {
        "name":"Priya",
        "department":"HR",
        "salary":60000
    },
    {
        "name":"Rohan",
        "department":"Engineering",
        "salary":95000
    }
]
'''
json_data=json.loads(employee_json)
print(f"Total Employees: {len(json_data)}")
total_salary=sum([emp["salary"] for emp in json_data])
average_salary=total_salary/len(json_data)
print(f"Average Salary : {average_salary}")
highest_paid= reduce(lambda s1,s2: s1 if s1["salary"]>s2["salary"] else s2 ,json_data)
print(f"Highest paid employee {highest_paid['name']}")
# could have done highest_paid = max(
#     json_data,
#     key=lambda emp: emp["salary"]
# )
json.dumps(json_data,indent=4)


@dataclass
class Employee:
    name:str
    department:str
    salary:int


employee_list=[]
for employee in json_data:
    employee_list.append(Employee(employee['name'],employee['department'],employee['salary']))

print(employee_list)

