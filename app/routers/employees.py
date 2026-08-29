#Crear el archivo para los endpoints del recurso de empleados

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services.employee_service import EmployeeService

# Configuración del enrutador con un prefijo común y etiquetas para la documentación Swagger
router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.get("/", response_model=list[EmployeeResponse], status_code=status.HTTP_200_OK,
            summary="Obtener todos los empleados",
            description="Obtiene la lista de todos los empleados registrados en el sistema. "
                        "Permite aplicar paginación mediante los parámetros skip y limit.",
            response_description="Lista de empleados.")
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene la lista de todos los empleados (Soporta paginación)."""
    return EmployeeService.get_all(db, skip=skip, limit=limit)


@router.get("/{id}", response_model=EmployeeResponse, status_code=status.HTTP_200_OK,
            summary="Obtiene un empleado por su ID",
            description="Obtiene un empleado existente mediante su identificador.",
            response_description="Datos del empleado encontrado.",
            responses={
                    404: {
                        "description": "Empleado no encontrado."
                    }
            })
def read_employee(id: int, db: Session = Depends(get_db)):
    """Obtiene un único empleado buscando por su ID."""
    return EmployeeService.get_by_id(db, employee_id=id)


@router.post("/", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED,
            summary="Crear un empleado",
            description="Registra un nuevo empleado en el sistema.",
            response_description="Empleado creado correctamente.",
            responses={
                400: {
                    "description": "El correo electrónico ya se encuentra registrado."
                }
            })
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Registra un nuevo empleado en el sistema."""
    return EmployeeService.create(db, employee_in=employee)


@router.put("/{id}", response_model=EmployeeResponse, status_code=status.HTTP_200_OK,
            summary="Actualizar un empleado",
            description="Actualiza la información de un empleado existente.",
            response_description="Empleado actualizado correctamente.")
def update_employee(id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    """Actualiza de forma parcial o total la información de un empleado existente."""
    return EmployeeService.update(db, employee_id=id, employee_in=employee)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,
            summary="Eliminar un empleado",
            description="Elimina permanentemente un empleado de la base de datos.")
def delete_employee(id: int, db: Session = Depends(get_db)):
    """Elimina de forma permanente un empleado de la base de datos."""
    return EmployeeService.delete(db, employee_id=id)