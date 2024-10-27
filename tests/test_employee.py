import pytest
from config.schema import EmployeeOutput,PaginatedEmployees


employee_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "department": "engineering",
    "role": "developer"
}

updated_employee_data = {
    "name": "John Updated",
    "email": "john.updated@example.com",
    "department": "sales",
    "role": "analyst"
}

@pytest.mark.parametrize("name, email, department, role,status_code", [
    ("Suman Menon", "suman@email.com", "sales", "analyst",201),
    ("Suman Menon", "suman@email.com", "engineering", "developer",201),
    ("Anita Gupta", "anita.gupta@email.com", "marketing", "manager",422),
    ("John Doe", "john.doe@email.com", "finance", "accountant",422),
])
def test_create_employee(authorized_client,session, name, email,department, role, status_code):
    employee_data = {
        "name": name,
        "email": email,
        "department": department,
        "role": role
    }
    response = authorized_client.post(
        "/api/employees/",
        json=employee_data  
    )
    
    print(response.json())
    assert response.status_code == status_code

def test_create_employee(authorized_client):
    employee_data = {
        "name": "New Employee",
        "email": "new.employee@example.com",
        "department": "engineering",
        "role": "developer"
    }
    response = authorized_client.post("/api/employees/", json=employee_data)
    assert response.status_code == 201
    new_employee = EmployeeOutput(**response.json())
    assert new_employee.name == employee_data["name"]
    assert new_employee.email == employee_data["email"]
    assert new_employee.department == employee_data["department"]
    assert new_employee.role == employee_data["role"]

def test_create_employee_invalid_data(authorized_client):
    invalid_data = { "name": "OnlyName" }
    response = authorized_client.post("/api/employees/", json=invalid_data)
    assert response.status_code == 422  

def test_create_employee_unauthorized(client):
    employee_data = {
        "name": "Unauthorized Employee",
        "email": "unauthorized.employee@example.com",
        "department": "engineering",
        "role": "developer"
    }
    response = client.post("/api/employees/", json=employee_data)
    assert response.status_code == 401  


### Get All Employees Tests ###

def test_get_all_employees(authorized_client, test_employees):
    response = authorized_client.get("/api/employees/")
    assert response.status_code == 200  # Found
    employees = PaginatedEmployees(**response.json())
    assert len(employees.employees) == len(test_employees)

def test_get_all_employees_filtered(authorized_client, test_employees):
    response = authorized_client.get("/api/employees/", params={"department": "engineering", "role": "developer"})
    assert response.status_code == 200
    employees = PaginatedEmployees(**response.json())
    for emp in employees.employees:
        assert emp.department == "engineering"
        assert emp.role == "developer"


### Get Employee by ID Tests ###

def test_get_employee_by_id(authorized_client, test_employees):
    print(test_employees)
    employee_id = test_employees[0].id 
    response = authorized_client.get(f"/api/employees/{employee_id}")
    assert response.status_code == 200
    employee = EmployeeOutput(**response.json())
    assert employee.name == test_employees[0].name

def test_get_employee_not_found(authorized_client):
    response = authorized_client.get("/api/employees/99999")  
    print(response.json())
    assert response.json()['status_code'] == 404
    assert response.json()['detail']=='404: Employee Not Found'



def test_update_employee(authorized_client, test_employees):
    employee_id = test_employees[0].id  
    response = authorized_client.put(f"/api/employees/{employee_id}", json=updated_employee_data)
    assert response.status_code == 200
    updated_employee = EmployeeOutput(**response.json())
    assert updated_employee.name == updated_employee_data["name"]

def test_update_employee_partial(authorized_client, test_employees):
    employee_id = test_employees[0].id  
    partial_data = {"name": "Partial Update"}
    response = authorized_client.put(f"/api/employees/{employee_id}", json=partial_data)
    assert response.status_code == 200
    updated_employee = EmployeeOutput(**response.json())
    assert updated_employee.name == "Partial Update"

def test_update_employee_not_found(authorized_client):
    response = authorized_client.get("/api/employees/99999")  
    print(response.json())
    assert response.json()['status_code'] == 404
    assert response.json()['detail']=='404: Employee Not Found'




def test_delete_employee(authorized_client, test_employees):
    employee_id = test_employees[0].id  
    response = authorized_client.delete(f"/api/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Employee deleted successfully"}

def test_delete_employee_not_found(authorized_client):
    response = authorized_client.get("/api/employees/99999")  
    print(response.json())
    assert response.json()['status_code'] == 404
    assert response.json()['detail']=='404: Employee Not Found'


def test_delete_employee_unauthorized(client, test_employees):
    employee_id = test_employees[0].id  
    response = client.delete(f"/api/employees/{employee_id}")
    assert response.status_code == 401
