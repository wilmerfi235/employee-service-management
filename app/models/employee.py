# abre tu archivo existente app/models/employee.py y modifícalo para añadir la llave foránea
# (department_id) y conectar la relación a la inversa:

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    position = Column(String(150), nullable=True)
    is_active = Column(Boolean, default=True)

    # 1. Crear la llave foránea que apunta al ID del departamento
    department_id = Column(Integer, ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)

    # 2. Relación Muchos a Uno: Muchos empleados pertenecen a un departamento
    department = relationship("Department", back_populates="employees")