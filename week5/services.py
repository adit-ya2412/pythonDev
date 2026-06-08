from fastapi import HTTPException,status

from schemas import Employee


def get_employee(employee_id: int):
    for emp in employees:
        if emp.id == employee_id:
            return emp
    
    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

def get_employees(
    department: str | None = None
):

    if department:

        return [
            emp
            for emp in employees
            if emp.department == department
        ]

    return employees
    
def update_employee(
    employee_id:int,
    updated_employee:Employee
):
    for index,emp in   enumerate(employees):
        if emp.id == employee_id:
            employees[index]=(updated_employee)
            return updated_employee    
    raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )
    


def create_employee(employee: Employee):

    employees.append(employee)

    return employee

def delete_employee(employee_id:int):
    for emp in employees:
        if emp.id == employee_id:
            employees.remove(emp)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    ) 


employees = [
    Employee(
        id=1,
        name="Aditya",
        department="Engineering",
        salary=100000
    ),
    Employee(
        id=2,
        name="Rohan",
        department="Engineering",
        salary=120000
    )
]