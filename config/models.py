from config.database import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime
from passlib.hash import bcrypt
from sqlalchemy.sql import func
from config.common import DepartmentEnum, RoleEnum


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime,nullable=True,default=func.now())
    
    def verify_password(self, password: str):
        return bcrypt.verify(password, self.password)


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(Enum(DepartmentEnum), nullable=True)
    role = Column(Enum(RoleEnum), nullable=True)
    date_joined = Column(DateTime, nullable=False,default=func.now())

