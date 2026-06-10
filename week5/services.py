from fastapi import HTTPException,status,Depends
from schemas import Employee,EmployeeCreate
from models import Employee
from sqlalchemy.orm import Session
from database import SessionLocal

def get_db():
    db=SessionLocal()
    try :
        yield db
    finally:
        db.close()
    


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
    


def create_employee(employee: EmployeeCreate,
                    db:Session=Depends(get_db)):

        db_employee=Employee(
            name=employee.name,
            department=employee.department,
            salary=employee.salary
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)

        return db_employee

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