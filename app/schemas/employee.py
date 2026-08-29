#Crear el archivo para los esquemas de empleados

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, TYPE_CHECKING

# Si Python está en fase de chequeo de tipos, importamos el departamento de forma segura
if TYPE_CHECKING:
    from app.schemas.department import DepartmentResponse

class EmployeeBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    position: Optional[str] = Field(None, max_length=150)

class EmployeeCreate(EmployeeBase):
    department_id: Optional[int] = Field(None, description="ID del departamento asignado")

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    position: Optional[str] = None
    is_active: Optional[bool] = None
    department_id: Optional[int] = None

class EmployeeResponse(EmployeeBase):
    id: int
    is_active: bool
    # Usamos comillas como texto '"DepartmentResponse"' para romper el ciclo de importación
    department: Optional["DepartmentResponse"] = None 

    model_config = {
        "from_attributes": True
    }

# --- LÍNEA DE SOLUCIÓN INDISPENSABLE ---
# Fuerza a Pydantic a resolver la referencia de texto de DepartmentResponse
from app.schemas.department import DepartmentResponse
EmployeeResponse.model_rebuild()