from fastapi.testclient import TestClient
from config.database import get_db,Base
from main import app
from config import models
from auth import create_access_token
from tests.database import TestingSessionLocal,engine
import pytest
import csv
from datetime import datetime



@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def overide_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db]=overide_get_db
    yield TestClient(app)

@pytest.fixture()
def test_user(client):
    user_data = {"email":"n@n.com","password":"password"}
    res = client.post(
        "/auth/register/",json=user_data
        )
    new_user = res.json()
    # print(res.json())
    new_user['password']=user_data['password']
    assert new_user["email"]=="n@n.com"
    assert res.status_code==201
    return new_user


@pytest.fixture()
def token(test_user):
    token = create_access_token({"sub": str(test_user['id'])})
    return token

@pytest.fixture()
def authorized_client(client, token):
    client.headers.update({
        "Authorization": f"Bearer {token}"
    })
    print("Authorized client headers:", client.headers)
    return client
    


@pytest.fixture()
def test_employees(session):
    employees_list = [
        {
            "name": "Alice Johnson",
            "email": "alice.johnson@example.com",
            "department": "engineering",
            "role": "developer"
        },
        {
            "name": "Bob Smith",
            "email": "bob.smith@example.com",
            "department": "sales",
            "role": "analyst"
        },
        {
            "name": "Charlie Davis",
            "email": "charlie.davis@example.com",
            "department": "sales",
            "role": "manager"
        },
        {
            "name": "Dana White",
            "email": "dana.white@example.com",
            "department": "engineering",
            "role": "manager"
        },
        {
            "name": "Evan Lee",
            "email": "evan.lee@example.com",
            "department": "hr",
            "role": "manager"
        },
        {
            "name": "Fiona Brown",
            "email": "fiona.brown@example.com",
            "department": "hr",
            "role": "analyst"
        },
        {
            "name": "George Clark",
            "email": "george.clark@example.com",
            "department": "engineering",
            "role": "developer"
        },
        {
            "name": "Hannah Adams",
            "email": "hannah.adams@example.com",
            "department": "hr",
            "role": "analyst"
        },
        {
            "name": "Ian Thompson",
            "email": "ian.thompson@example.com",
            "department": "engineering",
            "role": "developer"
        },
        {
            "name": "Jane Roberts",
            "email": "jane.roberts@example.com",
            "department": "hr",
            "role": "manager"
        }
    ]

    def create_employee_model(employee):
        return models.Employee(**employee)
    
    employees = list(map(create_employee_model, employees_list))
    
    session.add_all(employees)
    
    session.commit()
    empl = session.query(models.Employee).all()
    print(empl)  
    return empl






# def pytest_html_report_title(report):
#     report.title = "Test Results Summary"


# def pytest_runtest_logreport(report):
#         write_to_csv(report.nodeid, report.outcome, report.capstdout)


# def write_to_csv(test_name, outcome, output):
#     fieldnames = ['Test Name', 'Status', 'Output', 'Timestamp']
#     with open('test_results.csv', mode='a', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         if file.tell() == 0:
#             writer.writeheader()
#         writer.writerow({
#             'Test Name': test_name,
#             'Status': outcome,
#             'Output': output.strip(),
#             'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         })


# @pytest.fixture(scope="session", autouse=True)
# def setup_reports():
#     with open('test_results.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Test Name', 'Status', 'Output', 'Timestamp'])

