# Crear el archivo __init__.py para registrar el módulo
# Registrar el servicio en app/services/__init__.py

from app.services.employee_service import EmployeeService

__all__ = ["EmployeeService"]