
##===================================================================================

Employee Service Management API

REST API for employee management built with Python and FastAPI, following a layered architecture and using PostgreSQL as the relational database.

The project provides CRUD operations for employees, data validation, database migrations, automated tests and interactive API documentation through Swagger/OpenAPI.

Technologies
Python
FastAPI
PostgreSQL
SQLAlchemy
Alembic
Pydantic
Pytest
Swagger / OpenAPI
Architecture

The application follows a layered architecture to separate responsibilities and improve maintainability.


app/
│
├── models/
│   └── Database models
│
├── schemas/
│   └── Pydantic schemas
│
├── repositories/
│   └── Database access
│
├── services/
│   └── Business logic
│
├── routers/
│   └── API endpoints
│
├── database.py
└── main.py


Main layers:

Routers — Define the HTTP endpoints and handle API requests.
Services — Contain the application and business logic.
Repositories — Manage database operations.
Models — Define SQLAlchemy database models.
Schemas — Define request and response validation using Pydantic.



Features:

Employee CRUD operations
Employee and department models
Request and response validation
PostgreSQL database integration
SQLAlchemy ORM
Alembic database migrations
HTTP error handling
Automated tests with Pytest
Interactive Swagger/OpenAPI documentation



Installation
1. Clone the repository
git clone https://github.com/wilmerfi235/employee-service-management.git
cd employee-service-management
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
Windows — Git Bash
source .venv/Scripts/activate
Windows — CMD
.venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
Environment variables

Create a .env file based on .env.example.

Example:

DATABASE_URL=postgresql://username:password@localhost:5432/employee_db

Do not commit the .env file to Git. It contains environment-specific configuration and credentials.



Database migrations:

Run the existing Alembic migrations with:

alembic upgrade head
Run the application

Start the FastAPI development server with:

uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000



API Documentation:

FastAPI automatically generates interactive API documentation using Swagger/OpenAPI.

Swagger UI
http://127.0.0.1:8000/docs

ReDoc
http://127.0.0.1:8000/redoc



API Endpoints:

Employees

Method	Endpoint	Description
GET	/employees	Get all employees
GET	/employees/{id}	Get an employee by ID
POST	/employees	Create an employee
PUT	/employees/{id}	Update an employee
DELETE	/employees/{id}	Delete an employee



Tests:

The project uses Pytest for automated testing.

Run the complete test suite with:

pytest

Current test status:

14 passed



Project Status:

Current implementation:

FastAPI application

PostgreSQL integration

SQLAlchemy ORM

Alembic migrations

Employee CRUD

Pydantic validation

Basic error handling

Automated tests

Swagger/OpenAPI documentation

Git version control

GitHub repository



Future improvements may include:

Authentication and authorization

JWT security

Advanced API documentation

Docker

Docker Compose

CI/CD

Cloud deployment

Additional domain entities

Improved test coverage



GitHub: https://github.com/wilmerfi235
