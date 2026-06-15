from pydantic import BaseModel

class Employee(BaseModel):
    id:int
    name:str
    department:str
    salary:int

class EmployeeCreate(BaseModel):
    name:str
    department_id:int
    salary:int

class DepartmentResponse(BaseModel):

    id: int
    name: str

    class Config:
        from_attributes = True

class EmployeeResponse(BaseModel):
    id:int
    name:str
    department:DepartmentResponse | None=None
    salary:int

    class Config:
        from_attributes=True


class UserCreate(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    id:int
    username:str
    role:str
    class Config:
        from_attributes=True

class LoginRequest(BaseModel):
    username:str
    password:str

