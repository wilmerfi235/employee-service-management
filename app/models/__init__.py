#Paso 3: Registrar el modelo en app/models/__init__.py
#Esto te permitirá importarlo de forma mucho más limpia en el futuro desde cualquier parte de tu aplicación:

from app.models.employee import Employee

#Actualiza el archivo app/models/__init__.py para exponer ambos modelos
from app.models.department import Department

# Esto facilita importar todo el módulo de modelos junto
__all__ = ["Employee", "Department"]