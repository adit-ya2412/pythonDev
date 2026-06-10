
from fastapi import FastAPI

from routers.employee_router import router
from database import Base
from database import engine
import models
app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
