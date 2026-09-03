import json

def cargar_vehiculos(file):
    try:
        with open(file, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
def guardar_vehiculos(name,data):
    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def leer_vehiculo_por_placa(file, placa):
    # Cargar los datos del archivo JSON
    datos = cargar_vehiculos(file)
    # Buscar el vehículo por placa
    for vehiculo in datos:
        if vehiculo["placa"] == placa:
            return vehiculo
    return None

def actualizar_vehiculo(file, placa, nuevo_dato):
    # Cargar los datos del archivo JSON
    datos = cargar_vehiculos(file)
    # Buscar el vehículo por placa y actualizarlo
    for i, vehiculo in enumerate(datos):
        if vehiculo["placa"] == placa:
            datos[i] = nuevo_dato
            guardar_vehiculos(file, datos)
            return True
        else:
            print(f"No se encontró ningún vehículo con la placa {placa}.")
    return False

def eliminar_vehiculo(file, placa):
    # Cargar los datos del archivo JSON
    datos = cargar_vehiculos(file)
    # Filtrar los vehículos que no coincidan con la placa a eliminar
    nuevos_datos = [vehiculo for vehiculo in datos if vehiculo["placa"] != placa]
    if len(nuevos_datos) < len(datos):
        guardar_vehiculos(file, nuevos_datos)
        return True
    else:
        print(f"No se encontró ningún vehículo con la placa {placa}.")
    return False

