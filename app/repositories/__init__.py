#Crear el archivo __init__.py para registrar el módulo
# Registrar el repositorio en app/repositories/__init__.py

from app.repositories.employee_repository import EmployeeRepository

__all__ = ["EmployeeRepository"]