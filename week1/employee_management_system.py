employees = [
    {"id": 101, "name": "Aditya", "department": "Engineering", "salary": 85000},
    {"id": 102, "name": "Priya", "department": "HR", "salary": 60000},
    {"id": 103, "name": "Rohan", "department": "Engineering", "salary": 95000},
    {"id": 104, "name": "Neha", "department": "Finance", "salary": 75000},
    {"id": 105, "name": "Aman", "department": "Engineering", "salary": 70000}
]

def find_employee_by_id(employees, employee_id):

    for employee in employees:

        if employee["id"] == employee_id:
            return employee

    return None


def get_department_employees(employees, department):

    employee_list = []

    for employee in employees:

        if employee["department"].lower() == department.lower():
            employee_list.append(employee)

    return employee_list


def get_highest_paid_employee(employees):

    max_salary = 0
    highest_paid_employee = None

    for employee in employees:

        if employee["salary"] > max_salary:

            max_salary = employee["salary"]
            highest_paid_employee = employee

    return highest_paid_employee


def get_average_salary(employees):
    return sum(employee["salary"] for employee in employees)/len(employees)

def sort_employee_by_salary(employees):

    return sorted(
        employees,
        key=lambda employee: employee["salary"],
        reverse=True
    )
def sort_employee_by_name(employees):
    return sorted(
     employees,
     key=lambda employee: employee["name"]  
    )


def department_salary_summary(employees):
    department_summary={
        
    }

    for employee in employees:
        department=employee["department"]
        if department not in department_summary:
            department_summary[employee["department"]]={
                "total_employees":0,
                "total_salary":0
            }
        department_summary[department]["total_employees"]+=1
        department_summary[department]["total_salary"]+=employee["salary"]
        
    
    for department in department_summary:
        total_employees=department_summary[department]["total_employees"]
        total_salary=department_summary[department]["total_salary"]
        average=total_salary/total_employees
        department_summary[department]["average_salary"]=average

    return department_summary





department_summary=department_salary_summary(employees)

for department,data in department_summary.items():
    print(f"{department}")
    for field,value in data.items():
        print(f"-{field}:{value}")