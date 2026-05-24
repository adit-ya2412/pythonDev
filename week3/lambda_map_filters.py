from functools import reduce
employees = [
    {"name": "Aditya", "department": "Engineering", "salary": 85000},
    {"name": "Priya", "department": "HR", "salary": 60000},
    {"name": "Rohan", "department": "Engineering", "salary": 95000},
    {"name": "Neha", "department": "Finance", "salary": 75000},
    {"name": "Aman", "department": "Engineering", "salary": 70000}
]


capital_names=[ names for names in  map(lambda emp: emp["name"].upper(),employees)]

salary_greater_than_80k=[ names["name"] for names in filter(lambda emp : emp["salary"]> 80000,employees)]

salary_increments =[salaries for salaries in map(lambda sal:sal["salary"]+sal["salary"]*.15 , employees)]
engineering_employees=[names["name"] for names in filter(lambda emp:emp["department"]=="Engineering",employees)]
sorted_employees= sorted(
    employees,
    key=lambda emp : emp["salary"],
    reverse=True
    )

sorted_by_name_length= sorted(
    employees,
    key=lambda emp: len(emp["name"])

)
total_salary= reduce(lambda s1,s2 :s1+s2, map(lambda emp:emp["salary"],employees)) 

engineering_salaries=list(map(lambda emp: emp["salary"], filter(lambda emp:emp["department"]=="Engineering",employees)))

comma_seprated_names=",".join(map(lambda emp: emp["name"].upper(),employees))



highest_salary=reduce(lambda s1,s2: s1 if s1>s2 else s2  ,map (lambda emp:emp["salary"],employees))
print(comma_seprated_names)
print(engineering_salaries)
print(highest_salary)

uppercase_names_sorted_engineering=   list(map(lambda emp :emp["name"].upper(),sorted(
    filter(lambda emp: emp["department"]=="Engineering",employees),
    key=lambda emp: len(emp["name"]))

))


# employee_dictionary={
#     capital_name: list(map(lambda emp: emp["department"],filter(lambda emp:emp["name"].upper()==capital_name,employees)))[0]
#     for capital_name in capital_names
# }

employee_dictionary={
    emp["name"].upper():emp["department"]
    for emp in employees
}

print(employee_dictionary)

print(uppercase_names_sorted_engineering)

print(total_salary)
print(sorted_by_name_length)

print(engineering_employees)
print(salary_increments)
print(capital_names)
print(salary_greater_than_80k)
print(sorted_employees)
