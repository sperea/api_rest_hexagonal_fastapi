# Aplicación CRUD de usuarios

Esta aplicación es una implementación de un sistema CRUD (Create, Read, Update, Delete) de usuarios utilizando FastAPI, DDD y la arquitectura hexagonal.

## Requisitos

- Python 311.1 o superior
- PostgreSQL

## Instalación

1. Clona este repositorio
```bash
git clone https://github.com/tu_usuario/crud-users.git
```

2. Crea un entorno virtual y activa
```bash
python3 -m venv env
source env/bin/activate
```

3. Instala las dependencias
```bash
pip install -r requirements.txt
```

4. Crea un archivo .env con las siguientes variables de entorno:

* DATABASE_URI: la URI de conexión a la base de datos
* SECRET_KEY: una clave secreta para la aplicación

5. Crea la base de datos

```bash
python main.py create_db
```

## Ejecución
Para ejecutar la aplicación, ejecuta el siguiente comando

```bash
uvicorn main:app --reload
```

## Uso
La aplicación tiene las siguientes rutas:

* POST /users/: crea un nuevo usuario
* GET /users/{user_id}: obtiene un usuario por ID
* PUT /users/{user_id}: actualiza un usuario por ID
* DELETE /users/{user_id}: elimina un usuario por ID

## Licencia
Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.

Espero que esto te sea de ayuda. Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar.