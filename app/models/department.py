#Configurar los Modelos de Base de Datos (SQLAlchemy) en department.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False, index=True)

    # Relación Uno a Muchos: Un departamento tiene muchos empleados
    # 'back_populates' vincula esta propiedad con el campo 'department' en el modelo Employee
    employees = relationship("Employee", back_populates="department", cascade="all, delete-orphan")