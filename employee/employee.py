from fastapi import APIRouter, Depends, HTTPException,Query
from typing import Optional
from sqlalchemy.orm import Session
from config import get_db
from config.schema import EmployeeOutput, EmployeeUpdate, PaginatedEmployees, EmployeeCreate
from config.models import Employee, User
from auth import get_current_user

router = APIRouter(
    prefix="/api",
    tags=["Employee"]
    
)

@router.post("/employees/", response_model=EmployeeOutput)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        db_employee = Employee(
            name=employee.name,
            email=employee.email,
            department=employee.department,
            role=employee.role,
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.get("/employees/", response_model=PaginatedEmployees)
def get_all_employees(
    page: int = Query(1, ge=1),
    department: Optional[str] = None,
    role: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        limit = 10 
        skip = (page - 1) * limit
        query = db.query(Employee)

        if department:
            query = query.filter(Employee.department == department)
        if role:
            query = query.filter(Employee.role == role)

        query = query.order_by(Employee.id)
        total = query.count()
        employees = query.offset(skip).limit(limit).all()

        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "employees": employees
        }
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))


@router.get("/employees/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        employee = db.query(Employee).filter(Employee.id==employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee Not Found or You don't have access to this employee")
        return employee
    except Exception as e:
        return HTTPException(status_code=404,detail=str(e))


@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        employee = db.query(Employee).filter(Employee.id==employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee Not Found or You don't have access to this employee")
        
        db.delete(employee)
        db.commit()
        return {"message": "Employee deleted successfully"}
    except Exception as e:
        return HTTPException(status_code=404,detail=str(e))


@router.put("/employees/{employee_id}", response_model=EmployeeOutput)
def update_employee(
    request: EmployeeUpdate,
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        employee = db.query(Employee).filter(Employee.id==employee_id).first()

        if not employee:
            raise HTTPException(status_code=404, detail="Employee Not Found")
        
        if request.name is not None:
            employee.name = request.name
        if request.email is not None:
            employee.email = request.email
        if request.department is not None:
            employee.department = request.department
        if request.role is not None:
            employee.role = request.role

        db.commit()
        db.refresh(employee)

        return EmployeeOutput.from_orm(employee)
        
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

