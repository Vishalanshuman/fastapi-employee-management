from fastapi import FastAPI
from auth.auth import router as auth_router 
from employee.employee import router as tasks_router
from config import Base,engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(tasks_router)

