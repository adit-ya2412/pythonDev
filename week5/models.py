from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Employee(Base):

    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    department_id=Column(
        Integer,
        ForeignKey("departments.id")
    )
    department=relationship(
        "Department",
        back_populates="employees"
    )
    
    salary = Column(Integer)


class Department(Base):
    __tablename__ = "departments"
    
    id=Column(
        Integer,
        primary_key=True,
        index=True
    )
    name=Column(
        String,
        unique=True
    )

    employees=relationship("Employee",
                           back_populates="department")

