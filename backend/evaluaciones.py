import json
import citas

def consultar_calificaciones_por_alumno(file, documento_alumno):
    
    # Cargar los datos del archivo JSON
    datos = citas.cargar_citas(file)
    
    # Filtrar las citas por documento del alumno y que tengan calificación
    calificaciones = []
    for cita in datos:
        if cita["documento_alumno"] == documento_alumno and cita["calificacion"] is not None:
            calificaciones.append(cita)
    # Si no se encontraron calificaciones para el alumno, mostrar mensaje
    if not calificaciones:
        print(f"\nNo se encontraron calificaciones para el alumno con documento {documento_alumno}.")
        return
    # Imprimir las calificaciones encontradas
    for calificacion in calificaciones:
        print(f"\nAlumno: {calificacion['nombre_alumno']} | Instructor: {calificacion['nombre_instructor']} | Calificación: {calificacion['calificacion']} | Fecha: {calificacion['fecha']} | Observaciones: {calificacion.get('observaciones', '-')}")
    return calificaciones

def calcular_promedio_general(file):
    # Cargar los datos del archivo JSON
    datos = citas.cargar_citas(file)
    calificaciones = []
    # Filtrar las citas que tengan calificación
    for cita in datos:
        if cita["calificacion"] is not None:
            calificaciones.append(cita["calificacion"])
    
    if not calificaciones:
        print("No se encontraron calificaciones para calcular el promedio.")
        return None
    # Imprimir el promedio general de calificaciones

    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Promedio general de calificaciones: {promedio:.2f}")
    return promedio