employees = [
    {"name": "Aditya", "department": "Engineering", "salary": 85000},
    {"name": "Priya", "department": "HR", "salary": 60000},
    {"name": "Rohan", "department": "Engineering", "salary": 95000},
    {"name": "Neha", "department": "Finance", "salary": 75000},
    {"name": "Aman", "department": "Engineering", "salary": 70000}
]


employee_names=[employee["name"] for employee in employees]

employee_names_with_salary_greater_than_80k =[employee["name"] for employee in employees if employee["salary"]>80000]

salaries_after_10_increase=[ employee["salary"]+(employee["salary"] * 0.1) for employee in employees]

engneering_employee_names=[employee["name"].upper() for employee in employees if employee["department"]== "Engineering"]



departments=set(emp["department"] for  emp in employees )

department_summary={
    dept:len([emp for emp in employees if emp["department"]==dept])
    for dept in departments
}

employee_summary={
    employee["name"]:employee["salary"]
    for employee in employees
}

nested_list=[[1,2],[3,4],[5]]


matrix = [
 [1,2,3],
 [4,5,6]
]

flattend_matrix=[num for nums in matrix for num in nums]


flattend_list=[num for nums in nested_list for num in nums]

list_of_name_lengths=[len(emp["name"]) for emp in employees]


print(employee_names)
print(employee_names_with_salary_greater_than_80k)
print(salaries_after_10_increase)
print(engneering_employee_names)
print(department_summary)
print(flattend_list)
print(list_of_name_lengths)
print(employee_summary)
print(flattend_matrix)