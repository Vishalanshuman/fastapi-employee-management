
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

## Technologies Used

- FastAPI
- SQLAlchemy (for ORM)
- Pydantic (for data validation)
- PostgreSQL (or other databases)
- JWT for authentication

## Installation

### Prerequisites

- Python 3.7+
- PostgreSQL (or any other database)

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

### Authentication Endpoints

- **Register User**: `POST /auth/register/`
  - Request Body: `UserCreate`
  - Response: `UserCreate`

- **Login**: `POST /auth/login/`
  - Request Body: `LoginForm`
  - Response: `Token`

