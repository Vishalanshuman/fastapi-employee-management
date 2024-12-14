
# FastAPI Employee Management System

## Overview

This project is a RESTful API built with FastAPI for managing employee records and user authentication. It supports the creation, retrieval, updating, and deletion of employee data, along with user registration and authentication functionalities.

## Features

- **Employee Management**: 
  - Create, Read, Update, and Delete employee records.
  - Support for pagination and filtering by department and role.

- **User Authentication**:
  - User registration and login with secure password handling.
  - JWT (JSON Web Token) authentication for protected routes.

- **Automated Testing**:
  - Comprehensive test coverage for key functionalities.
  - Unit tests using `pytest` for `employee` and `user` endpoints.

## Technologies Used

- FastAPI
- SQLAlchemy (for ORM)
- Pydantic (for data validation)
- SQLite (or other databases)
- JWT for authentication
- Pytest (for testing)

## Installation

### Prerequisites

- Python 3.7+
- SQLite (or any other database)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Vishalanshuman/fastapi-employee-management.git
   cd fastapi-employee-management
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**: 
   - Create a PostgreSQL database for the application.

6. **Configure environment variables**:
   - Set up a `.env` file for database connection details and JWT secret key.

## Usage

1. **Run the application**:

   ```bash
   uvicorn main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

2. **API Documentation**: 
   - Access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Authentication Endpoints

- **Register User**: `POST /auth/register/`
  - Request Body: `UserCreate`
  - Response: `UserCreate`

- **Login**: `POST /auth/login/`
  - Request Body: `LoginForm`
  - Response: `Token`

### Employee Endpoints

- **Create Employee**: `POST /api/employees/`
  - Request Body: `EmployeeCreate`
  - Response: `EmployeeOutput`

- **Get All Employees**: `GET /api/employees/`
  - Query Parameters: `page`, `department`, `role`
  - Response: `PaginatedEmployees`

- **Get Employee by ID**: `GET /api/employees/{employee_id}`
  - Response: `EmployeeOutput`

- **Update Employee**: `PUT /api/employees/{employee_id}`
  - Request Body: `EmployeeUpdate`
  - Response: `EmployeeOutput`

- **Delete Employee**: `DELETE /api/employees/{employee_id}`
  - Response: `{"message": "Employee deleted successfully"}`

## Testing

The project includes unit tests for key functionalities. Tests are written using `pytest`, with the following structure:

- **tests/**: Contains all test files and configurations.
  - **tests/test_employees.py**: Test cases for employee management, including parameterized tests.
  - **tests/test_users.py**: Test cases for user registration and authentication.
  - **tests/conftest.py**: Sets up fixtures and shared test resources, including database setup.

### Running Tests

1. **Ensure the virtual environment is activated**.
2. **Run the tests**:

   ```bash
   pytest -v -s
   ```

   The test suite will execute all test cases, using fixtures defined in `conftest.py` and parameterized tests within individual test modules.

### Test Report Generation (HTML & CSV)

1. **To generate an HTML test report: You can run the following command to get a self-contained HTML report of your tests:**

```bash
pytest tests/ --html=reports/test_report.html --self-contained-html
```
This will create a `test_report.html` file in the `reports` folder.

2. **To generate a CSV test report: To save the test results in CSV format, use the following command:**

```bash
pytest tests/ --csv=reports/test_report.csv
```
This will generate a `test_report.csv` file in the reports folder.

`Note`: You can run both the HTML and CSV report generation commands together by appending both flags:

```bash
pytest tests/ --html=reports/test_report.html --csv=reports/test_report.csv --self-contained-
```
