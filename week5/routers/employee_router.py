from fastapi import APIRouter
from fastapi import status,Depends
from  sqlalchemy.orm import Session
from schemas import Employee,EmployeeCreate
from services import get_employee,get_employees,create_employee,update_employee,delete_employee,get_db
router= APIRouter()

@router.get("/employees")
def get_all_employees():
      return get_employees()

@router.get("/employee/{employee_id}")
def get_employee_by_id(employee_id: int):
    return get_employee(employee_id)

@router.get("/employees/{department}")
def get_employees_by_department(
    department:str |None = None
    ):
    return get_employees(department)

@router.put("/employees/{employee_id}",
         status_code=status.HTTP_200_OK)
def update_employee_method(
    employee_id:int,
    updated_employee:Employee
):
    return update_employee(employee_id,updated_employee)
    

@router.post("/employees",
          status_code=status.HTTP_201_CREATED)
def create_employee_method(employee: EmployeeCreate,db:
                           Session=Depends(get_db)):
            return create_employee(employee)


@router.delete("/employees/{employee_id}",
           status_code=status.HTTP_204_NO_CONTENT )
def delete_employee_method(employee_id:int):
    return delete_employee(employee_id)