import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Cargar las variables de entorno del archivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("La variable de entorno DATABASE_URL no está configurada")

# 2. Crear el motor de conexión (Engine)
# Nota: A diferencia de SQLite, PostgreSQL no necesita el argumento 'connect_args={"check_same_thread": False}'
engine = create_engine(DATABASE_URL)

# 3. Crear la fábrica de sesiones (SessionLocal)
# Cada instancia de SessionLocal será una sesión de base de datos única
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Crear la clase Base para los modelos ORM
# De esta clase heredarán todos los modelos de base de datos (tablas)
Base = declarative_base()


# 5. Dependencia para obtener la sesión de la Base de Datos en los endpoints de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()