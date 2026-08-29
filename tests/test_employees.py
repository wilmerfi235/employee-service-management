from fastapi.testclient import TestClient

from app.main import app

# La solución buena es hacer que cada test genere un email único.
# usando uuid:
from uuid import uuid4

client = TestClient(app)


def unique_email(prefix: str) -> str:
    return f"{prefix}.{uuid4()}@example.com"


def test_create_employee():
    email = unique_email("juan.perez")
    
    employee_data = {
    "first_name": "Juan",
    "last_name": "Perez",
    "email": email,
    "position": "Software Developer",
    "department_id": None
    }

    response = client.post("/api/v1/employees/", json=employee_data)

    assert response.status_code == 201

    data = response.json()

    assert data["first_name"] == "Juan"
    assert data["last_name"] == "Perez"
    assert data["email"] == email
    assert data["position"] == "Software Developer"
    assert "id" in data

    # Guardamos el ID para poder reutilizarlo en otros tests si fuera necesario
    assert data["id"] is not None


def test_get_employees():
    response = client.get("/api/v1/employees/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_get_employee():
    email = unique_email("maria.garcia")
    
    # Primero creamos un empleado
    employee_data = {
    "first_name": "Maria",
    "last_name": "Garcia",
    "email": email,
    "position": "Backend Developer",
    "department_id": None
    }

    create_response = client.post(
        "/api/v1/employees/",
        json=employee_data
    )

    assert create_response.status_code == 201

    employee_id = create_response.json()["id"]

    # Después buscamos el empleado por ID
    response = client.get(
        f"/api/v1/employees/{employee_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == employee_id
    assert data["first_name"] == "Maria"
    assert data["last_name"] == "Garcia"
    assert data["email"] == email


def test_update_employee():
    # Creamos un empleado
    employee_data = {
    "first_name": "Carlos",
    "last_name": "Lopez",
    "email": unique_email("carlos.lopez"),  
    "position": "Developer",
    "department_id": None
    }

    create_response = client.post(
        "/api/v1/employees/",
        json=employee_data
    )

    assert create_response.status_code == 201

    employee_id = create_response.json()["id"]

    # Actualizamos algunos campos
    update_data = {
        "first_name": "Carlos",
        "last_name": "Lopez",
        "position": "Senior Developer"
    }

    response = client.put(
        f"/api/v1/employees/{employee_id}",
        json=update_data
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == employee_id
    assert data["position"] == "Senior Developer"


def test_delete_employee():
    # Creamos un empleado
    employee_data = {
    "first_name": "Pedro",
    "last_name": "Martinez",
    "email": unique_email("pedro.martinez"),
    "position": "QA Engineer",
    "department_id": None
    }

    create_response = client.post(
        "/api/v1/employees/",
        json=employee_data
    )

    assert create_response.status_code == 201

    employee_id = create_response.json()["id"]

    # Eliminamos el empleado
    response = client.delete(
        f"/api/v1/employees/{employee_id}"
    )

    assert response.status_code == 204

    # Un 204 NO debe devolver contenido
    assert response.content == b""

    # Comprobamos que ya no existe
    get_response = client.get(
        f"/api/v1/employees/{employee_id}"
    )

    assert get_response.status_code == 404


# ====================================================================================
# Añadir validaciones
# email, first_name, last_name, position

def test_create_employee_invalid_email():
    employee_data = {
    "first_name": "Juan",
    "last_name": "Perez",
    "email": "correo-invalido",
    "position": "Software Developer",
    "department_id": None,
    }

    response = client.post(
        "/api/v1/employees/",
        json=employee_data,
    )

    assert response.status_code == 422


def test_create_employee_duplicate_email():
    email = unique_email("duplicate")

    employee_data = {
        "first_name": "Juan",
        "last_name": "Perez",
        "email": email,
        "position": "Developer"
    }

    first_response = client.post(
        "/api/v1/employees",
        json=employee_data
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/api/v1/employees",
        json=employee_data
    )

    assert second_response.status_code == 400
    assert second_response.json() == {
        "detail": f"El correo electrónico '{email}' ya se encuentra registrado."
    }


def test_create_employee_empty_first_name():
    employee_data = {
    "first_name": "",
    "last_name": "Perez",
    "email": "juan.validation.test@example.com",
    "position": "Software Developer",
    "department_id": None,
    }

    response = client.post(
        "/api/v1/employees/",
        json=employee_data,
    )

    assert response.status_code == 422


def test_create_employee_first_name_too_long():
    employee_data = {
    "first_name": "A" * 101,
    "last_name": "Perez",
    "email": "juan.longname.test@example.com",
    "position": "Software Developer",
    "department_id": None,
    }

    response = client.post(
        "/api/v1/employees/",
        json=employee_data,
    )

    assert response.status_code == 422


def test_create_employee_empty_last_name():
    employee_data = {
    "first_name": "Juan",
    "last_name": "",
    "email": "juan.lastname.test@example.com",
    "position": "Software Developer",
    "department_id": None,
    }

    response = client.post(
        "/api/v1/employees/",
        json=employee_data,
    )

    assert response.status_code == 422


def test_create_employee_last_name_too_long():
    employee_data = {
    "first_name": "Juan",
    "last_name": "A" * 101,
    "email": "juan.longlastname.test@example.com",
    "position": "Software Developer",
    "department_id": None,
    }

    response = client.post(
        "/api/v1/employees/",
        json=employee_data,
    )

    assert response.status_code == 422


def test_create_employee_position_too_long():
    employee_data = {
    "first_name": "Juan",
    "last_name": "Perez",
    "email": "juan.position.test@example.com",
    "position": "A" * 151,
    "department_id": None,
    }

    response = client.post(
        "/api/v1/employees/",
        json=employee_data,
    )

    assert response.status_code == 422
    

# ====================================================================================
def test_get_employee_not_found():
    response = client.get("/api/v1/employees/999999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "No se encontró ningún empleado con el ID 999999."
    }


def test_update_employee_not_found():
    update_data = {
        "first_name": "Carlos",
        "last_name": "Lopez",
        "position": "Senior Developer"
    }

    response = client.put(
        "/api/v1/employees/999999",
        json=update_data
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "No se encontró ningún empleado con el ID 999999."
    }