

from fastapi import FastAPI
from app.routers import employee_router

# 1. Inicializar la aplicación FastAPI
app = FastAPI(
    title="Employee Service Management API",
    description="API REST para la gestión y administración de empleados de la empresa",
    version="1.0.0"
)

# 2. Registrar los enrutadores con el prefijo global de versión requerido
app.include_router(employee_router, prefix="/api/v1")

# 3. Ruta base de cortesía o chequeo de salud (Health Check)
@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Bienvenido a la API de Gestión de Empleados",
        "docs": "/docs"
    }