# DriveSafe 🚗🏍️

Aplicación de consola en Python para gestionar una escuela de conducción: registro de instructores y alumnos, inventario de vehículos, y programación de citas de práctica con control de disponibilidad y asistencia.

## Integrantes:
Diana Milena Chaparro Macias
Nicolas Archila
Juan Sebastián Lesmes


## Índice

- [Funcionalidades](#funcionalidades)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Cómo ejecutar](#cómo-ejecutar)
- [Menú de la aplicación](#menú-de-la-aplicación)
- [Modelo de datos](#modelo-de-datos)
- [Reglas de negocio](#reglas-de-negocio)

## Funcionalidades

### Gestión de usuarios (instructores y alumnos)
- Crear instructores (nombre, edad, sexo, especialidad, documento, teléfono, jornada de disponibilidad).
- Crear alumnos (nombre, edad, sexo, tipo de vehículo, documento, teléfono, fecha de registro automática).
- Listar instructores y alumnos.
- Editar instructor o alumno por documento (deja en blanco un campo para no modificarlo).
- Validación de documento único y de rangos de edad (18-100 para instructores, 16-100 para alumnos).

### Gestión de vehículos
- Registrar vehículos (marca, modelo, placa, tipo, estado).
- Listar vehículos con su estado de disponibilidad.
- Validación de placa única.

### Gestión de citas
- **Programar cita**: selecciona alumno, fecha, tipo de vehículo (autodetectado si el alumno no maneja "Ambas") y jornada; el sistema filtra automáticamente los instructores y vehículos disponibles para ese cruce de fecha/jornada/tipo y evita dobles reservas.
- **Consultar citas**: por documento de alumno o por fecha.
- **Registrar asistencia y observaciones**: marca cada cita como Asistió / No asistió / Cancelada y permite dejar observaciones; también sirve como historial de práctica.

## Estructura del proyecto

```
Proyecto_1_python/
├── backend/
│   ├── main.py         # Punto de entrada y toda la interacción por consola
│   ├── clientes.py     # CRUD de instructores y alumnos (usuarios.json / instructores.json)
│   ├── vehiculos.py    # CRUD de vehículos (vehiculos.json)
│   └── citas.py        # CRUD de citas + reglas de disponibilidad (citas.json)
└── datos/
    ├── usuarios.json
    ├── instructores.json
    ├── vehiculos.json
    └── citas.json
```

Las rutas a los archivos JSON se calculan a partir de la ubicación de `main.py`, así que la aplicación siempre lee y escribe en `datos/` sin importar desde qué carpeta se ejecute.

## Menú de la aplicación

```
Menú principal
├── 1. Gestión de usuario (cliente/instructor)
│   ├── 1. Crear Instructor
│   ├── 2. Crear Alumno
│   ├── 3. Ver listado de instructores
│   ├── 4. Ver listado de alumnos
│   ├── 5. Editar instructor
│   ├── 6. Editar alumno
│   └── 7. Salir
├── 2. Gestión de vehículo
│   ├── 1. Crear Vehículo
│   ├── 2. Ver listado de vehículos
│   └── 3. Salir
├── 3. Gestión de citas
│   ├── 1. Programar cita
│   ├── 2. Consultar citas (por cliente / por fecha)
│   ├── 3. Registrar asistencia y observaciones
│   └── 4. Salir
├── 4. Historial de práctica (consulta de citas)
└── 5. Salir
```

## Modelo de datos

### `instructores.json`
```json
{
  "nombre_completo": "string",
  "edad": "int (18-100)",
  "sexo": "Masculino | Femenino",
  "especialidad": "Moto | Carro | Ambas",
  "documento": "int (único)",
  "telefono": "int",
  "disponibilidad": "Manana | Tarde | Noche"
}
```

### `usuarios.json` (alumnos)
```json
{
  "nombre_completo": "string",
  "edad": "int (16-100)",
  "sexo": "Masculino | Femenino",
  "tipo_vehiculo": "Moto | Carro | Ambas",
  "documento": "int (único)",
  "telefono": "int",
  "fecha_registro": "AAAA-MM-DD"
}
```

### `vehiculos.json`
```json
{
  "marca": "string",
  "modelo": "string",
  "placa": "string (única)",
  "tipo": "Moto | Carro",
  "estado": "Disponible | ..."
}
```

### `citas.json`
```json
{
  "id": "int (autoincremental)",
  "fecha": "AAAA-MM-DD",
  "jornada": "Manana | Tarde | Noche",
  "tipo_vehiculo": "Moto | Carro",
  "documento_alumno": "int",
  "nombre_alumno": "string",
  "documento_instructor": "int",
  "nombre_instructor": "string",
  "placa_vehiculo": "string",
  "estado": "Programada | Realizada",
  "asistencia": "null | Asistió | No asistió | Cancelada",
  "observaciones": "string"
}
```

## Reglas de negocio

- **Un instructor "Ambas"** aparece como opción disponible tanto para citas de Moto como de Carro.
- **Sin doble reserva**: un instructor o un vehículo no pueden quedar asignados a dos citas en la misma fecha y jornada (`citas.instructor_ocupado` / `citas.vehiculo_ocupado`).
- **Tipo de vehículo del alumno**: si el alumno tiene un tipo fijo ("Moto" o "Carro"), la cita lo usa automáticamente sin volver a preguntarlo; solo se pregunta cuando el alumno es "Ambas".
- **Fechas**: no se permite programar citas en fechas anteriores a hoy.
- **Documentos y placas únicos**: no se puede registrar dos veces el mismo documento (instructor/alumno) ni la misma placa (vehículo).
