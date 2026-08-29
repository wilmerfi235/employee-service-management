#Crear el archivo __init__.py para registrar el módulo
# Registrar los esquemas en app/schemas/__init__.py

from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse

#agregado
from app.schemas.department import DepartmentCreate, DepartmentUpdate, DepartmentResponse, DepartmentWithEmployeesResponse

__all__ = ["EmployeeCreate", "EmployeeUpdate", "EmployeeResponse",
            "DepartmentCreate", "DepartmentUpdate", "DepartmentResponse", "DepartmentWithEmployeesResponse"]