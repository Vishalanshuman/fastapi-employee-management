from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from config.common import  DepartmentEnum, RoleEnum


class EmployeeOutput(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: Optional[DepartmentEnum] = None
    role: Optional[RoleEnum] = None
    date_joined: datetime

    class Config:
        from_attributes = True 


class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    department: Optional[DepartmentEnum] = None
    role: Optional[RoleEnum] = None


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[DepartmentEnum] = None
    role: Optional[RoleEnum] = None

class PaginatedEmployees(BaseModel):
    total: int
    skip: int
    limit: int
    employees: List[EmployeeOutput]


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginForm(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserOutput(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime  # Use `datetime` from the standard library

    class Config:
        from_attributes = True
