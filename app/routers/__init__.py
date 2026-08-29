# Crear el archivo __init__.py para registrar el módulo
#Registrar el enrutador en app/routers/__init__.py

from app.routers.employees import router as employee_router

__all__ = ["employee_router"]