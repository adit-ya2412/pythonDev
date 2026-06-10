from pydantic import BaseModel

class Employee(BaseModel):
    id:int
    name:str
    department:str
    salary:int

class EmployeeCreate(BaseModel):
    name:str
    department:str
    salary:int

class EmployeeResponse(BaseModel):
    id:int
    name:str
    department:str
    salary:int