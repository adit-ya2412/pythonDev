from http.client import HTTPException

from fastapi import FastAPI, status
from models  import Employee
app=FastAPI()

@app.get("/")

def home():
    return{"message":"Hello Fast API"}


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in employees:
        if emp.id == employee_id:
            return emp
    
    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

@app.get("/employees")
def get_employees(
    department:str |None = None
    ):
    if department :
        for emp in employees:
            if emp.department == department:
                return emp
    else:
        return employees
    
@app.put("/employees/{employee_id}",
         status_code=status.HTTP_200_OK)
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
    

@app.post("/employees",
          status_code=status.HTTP_201_CREATED)
def create_employee(employee: Employee):

    employees.append(employee)

    return employee


@app.delete("/employees/{employee_id}",
           status_code=status.HTTP_204_NO_CONTENT ,
           summary="Employee deleted successfully")
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