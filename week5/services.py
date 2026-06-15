from fastapi import HTTPException,status,Depends
from schemas import Employee,EmployeeCreate,UserCreate,LoginRequest
from models import Employee,Department,User
from sqlalchemy.orm import Session
from password_hashing_util import get_password_hash,verify_password
from jwt_config import create_access_token    
import time

def get_employee(employee_id: int,db:Session):

    employee=(
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if employee :
        return employee
   
    
    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

def get_employees(
         db:Session,
    department: str | None = None
):

    if department:
        return(
            db.query(Employee)
            .filter(Employee.department == department)
            .all()
        )
        

    return db.query(Employee).all()
    
def update_employee(
    employee_id:int,
    updated_employee:EmployeeCreate,
    db:Session
):
    
    employee=(
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )
    if not employee:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )
    employee.name=updated_employee.name
    employee.department=updated_employee.department
    employee.salary=updated_employee.salary
    db.commit()
    db.refresh(employee)
    return employee


def create_employee(employee: EmployeeCreate,
                    db:Session):

        db_employee=Employee(
            name=employee.name,
            department_id=employee.department_id,
            salary=employee.salary
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)

        return db_employee

def delete_employee(employee_id:int, db:Session):
       
    employee= (
         db.query(Employee)
         .filter(Employee.id==employee_id)
         .first()
    )
      
    if not employee:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
        )
    db.delete(employee)
    db.commit()
    return {"message":"Employee Deleted"}     

def get_department_employees(
        department_id:int,
        db:Session
        ):
    department=(
        db.query(Department)
        .filter(Department.id== department_id)
        .first()
    )
    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    
    return department.employees

def create_department(department_name:str, db:Session):
    department=Department(name=department_name)
    db.add(department)
    db.commit()
    return {"message":"Department Created"}

def getDepartments(db:Session):
   return db.query(Department).all()

def create_user(
        user:UserCreate,
        db:Session
        ):
    existing_user=(
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if existing_user :
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    hashed_password=get_password_hash(user.password)

    db_user=User(
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def login_user(
        login_request:LoginRequest,
        db:Session
):
    user=(
        db.query(User)
        .filter(
            User.username == login_request.username
        )
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    if not verify_password(
        login_request.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    token= create_access_token(
        {
            "sub":user.username,
            "role":user.role
        }
    )

    return {
        "access_token":token,
        "token_type":"bearer"
    }

def send_email(username:str):
    print(f"Starting email for {username}")
    time.sleep(5)
    print(f"Email sent to {username}")

def process_document(
    document_name: str
):

    print(
        f"Processing {document_name}"
    )

    time.sleep(10)

    print(
        f"Finished {document_name}"
    )

