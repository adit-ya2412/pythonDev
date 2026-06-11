from fastapi import APIRouter
from fastapi import status,Depends
from  sqlalchemy.orm import Session
from schemas import EmployeeCreate,EmployeeResponse

from dependencies import get_db
from services import create_department,getDepartments, get_department_employees, get_employee,get_employees,create_employee,update_employee,delete_employee
router= APIRouter()


@router.get("/departments/{department_id}/employess")
def get_department_employeees(department_id:int,db:Session=Depends(get_db)):
      return get_department_employees(department_id,db)

@router.get("/employee/{employee_id}",
            response_model=EmployeeResponse)
def get_employee_by_id(employee_id: int,db:Session =Depends(get_db)):
    return get_employee(employee_id,db)

@router.get("/employees}",
            response_model=list[EmployeeResponse])
def get_employees_by_department(
    department:str |None = None,
    db:Session=Depends(get_db)
    ):
    return get_employees(db,department)

@router.put("/employees/{employee_id}",
         status_code=status.HTTP_200_OK)
def update_employee_method(
    employee_id:int,
    updated_employee:EmployeeCreate,
    db:Session=Depends(get_db)
):
    return update_employee(employee_id,updated_employee,db)
    

@router.post("/employees",
          status_code=status.HTTP_201_CREATED,
          response_model=EmployeeResponse)
def create_employee_method(employee: EmployeeCreate,
                           db:Session=Depends(get_db)):
            return create_employee(employee,db)


@router.delete("/employees/{employee_id}",
           status_code=status.HTTP_204_NO_CONTENT )
def delete_employee_method(employee_id:int,db:Session=Depends(get_db)):
    return delete_employee(employee_id,db)


@router.get("/departments")
def get_departments(
    db: Session = Depends(get_db)
):
    return getDepartments(db)

@router.post("/department/{department_name}")
def create_department_for_employee(
     department_name:str,db:Session=Depends(get_db)):
     return create_department(department_name,db)
