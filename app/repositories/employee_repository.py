#Crear el archivo específico para las operaciones de empleados

from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

class EmployeeRepository:
    
    @staticmethod
    def get_employee(db: Session, employee_id: int) -> Employee | None:
        """Busca un empleado por su ID único."""
        return db.query(Employee).filter(Employee.id == employee_id).first()

    @staticmethod
    def get_employee_by_email(db: Session, email: str) -> Employee | None:
        """Busca un empleado por su correo electrónico (útil para validaciones)."""
        return db.query(Employee).filter(Employee.email == email).first()

    @staticmethod
    def get_employees(db: Session, skip: int = 0, limit: int = 100) -> list[Employee]:
        """Obtiene una lista de empleados con paginación."""
        return db.query(Employee).offset(skip).limit(limit).all()

    @staticmethod
    def create_employee(db: Session, employee_in: EmployeeCreate) -> Employee:
        """Registra un nuevo empleado en la base de datos."""
        db_employee = Employee(
            first_name=employee_in.first_name,
            last_name=employee_in.last_name,
            email=employee_in.email,
            position=employee_in.position
        )
        db.add(db_employee)
        db.commit()      # Guarda los cambios de forma permanente en PostgreSQL
        db.refresh(db_employee)  # Recarga el objeto para obtener el ID autogenerado
        return db_employee

    @staticmethod
    def update_employee(db: Session, db_employee: Employee, employee_in: EmployeeUpdate) -> Employee:
        """Actualiza los datos de un empleado existente de forma dinámica."""
        # Convertimos el esquema a diccionario ignorando los valores no enviados (None)
        update_data = employee_in.model_dump(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(db_employee, field, value)  # Modifica los campos en el objeto
            
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee

    @staticmethod
    def delete_employee(db: Session, db_employee: Employee) -> bool:
        """Elimina físicamente un empleado de la base de datos."""
        db.delete(db_employee)
        db.commit()
        return True