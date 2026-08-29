#Crear el archivo de lógica para los empleados

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.models.employee import Employee

class EmployeeService:

    @staticmethod
    def create(db: Session, employee_in: EmployeeCreate) -> Employee:
        """Lógica de negocio para registrar un empleado. Valida que el email sea único."""
        # 1. Regla de negocio: No pueden existir dos empleados con el mismo correo
        existing_employee = EmployeeRepository.get_employee_by_email(db, email=employee_in.email)
        if existing_employee:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El correo electrónico '{employee_in.email}' ya se encuentra registrado."
            )
        
        # 2. Si pasa la validación, delega la creación al repositorio
        return EmployeeRepository.create_employee(db, employee_in)

    @staticmethod
    def get_by_id(db: Session, employee_id: int) -> Employee:
        """Obtiene un empleado por ID o lanza un error 404 si no existe."""
        employee = EmployeeRepository.get_employee(db, employee_id)
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encontró ningún empleado con el ID {employee_id}."
            )
        return employee

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[Employee]:
        """Obtiene el listado de empleados utilizando paginación."""
        return EmployeeRepository.get_employees(db, skip=skip, limit=limit)

    @staticmethod
    def update(db: Session, employee_id: int, employee_in: EmployeeUpdate) -> Employee:
        """Lógica para actualizar los datos de un empleado existente."""
        # 1. Verificar si el empleado existe
        db_employee = EmployeeService.get_by_id(db, employee_id)
        
        # 2. Regla de negocio: Si se intenta cambiar el email, validar que no esté duplicado
        if employee_in.email and employee_in.email != db_employee.email:
            existing_email = EmployeeRepository.get_employee_by_email(db, email=employee_in.email)
            if existing_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"El correo electrónico '{employee_in.email}' ya pertenece a otro empleado."
                )
                
        # 3. Delegar la actualización al repositorio
        return EmployeeRepository.update_employee(db, db_employee, employee_in)

    @staticmethod
    def delete(db: Session, employee_id: int) -> None:
        """Lógica para eliminar de forma definitiva a un empleado."""
        
        # 1. Verificar si existe
        db_employee = EmployeeService.get_by_id(db, employee_id)
        
        # 2. Delegar la eliminación al repositorio
        EmployeeRepository.delete_employee(db, db_employee)