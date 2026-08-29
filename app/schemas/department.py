# define cómo viajará la información de los departamentos:

from pydantic import BaseModel, Field
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.schemas.employee import EmployeeResponse

class DepartmentBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Nombre del departamento")

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class DepartmentWithEmployeesResponse(DepartmentResponse):
    # Usamos comillas '"EmployeeResponse"' para romper el ciclo de importación
    employees: list["EmployeeResponse"] = []


# --- LÍNEA DE SOLUCIÓN INDISPENSABLE ---
# Fuerza a Pydantic a resolver la referencia de texto de EmployeeResponse
from app.schemas.employee import EmployeeResponse
DepartmentWithEmployeesResponse.model_rebuild()