from fastapi import APIRouter, HTTPException
from fastapi import status,Depends
from  sqlalchemy.orm import Session
from schemas import EmployeeCreate,EmployeeResponse,UserResponse,UserCreate,LoginRequest
from get_token_util import get_current_user
from models import User
from dependencies import get_db
from fastapi import BackgroundTasks
from fastapi import UploadFile,File
import os
from services import create_department,getDepartments, get_department_employees, get_employee,get_employees,create_employee,update_employee,delete_employee,create_user,login_user,send_email,process_document
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

@router.post("/register",
             response_model=UserResponse,
             status_code=201)
def register(
     user:UserCreate,
     db:Session =Depends(get_db)
):
     return create_user(
          user,
          db)


@router.post("/login")
def login(
     login_request:LoginRequest,
     db: Session = Depends(get_db)
     ):
     return login_user(
          login_request,
          db
     )

@router.get("/me")
def get_me(
     current_user:User =Depends(get_current_user)
):
     return current_user


@router.post("/send-email")
def send_email_endpoint(
     username:str,
     background_tasks:BackgroundTasks
):
     background_tasks.add_task(
          send_email,
          username
     )

     return {
          "message":"Email queued"
     }


@router.post("/process-document")
def process_document_endpoint(
    document_name: str,
    background_tasks: BackgroundTasks
):

    background_tasks.add_task(
        process_document,
        document_name
    )

    return {
        "message": "Document processing started"
    }


@router.post("/upload")
def upload_file(
    file:UploadFile =File(...)
):
     if not file.filename:
        raise HTTPException(
        status_code=400,
        detail="No file uploaded"
    )
     
     os.makedirs(
          "uploads",
          exist_ok=True
     )

     contents = file.file.read()

     if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(
        status_code=400,
        detail="File too large"
        )
    
     allowed = {".pdf", ".txt"}

     extension = os.path.splitext(
                file.filename
            )[1]

     if extension not in allowed:
        raise HTTPException(
        status_code=400,
        detail="Unsupported file type"
         )
    
     
     with open(
          f"uploads/{file.filename}",
          "wb"
     ) as buffer:
          buffer.write(
               file.file.read()
          )
     return {
          "filename":file.filename
     }
