import json

def cargar_citas(file):
    try:
        with open(file, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
def guardar_citas(name,data):
    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def leer_cita_por_id(file, id_cita):
    # Cargar los datos del archivo JSON
    datos = cargar_citas(file)
    # Buscar la cita por id
    for cita in datos:
        if cita["id"] == id_cita:
            return cita
    return None

def actualizar_cita(file, id_cita, nuevo_dato):
    # Cargar los datos del archivo JSON
    datos = cargar_citas(file)
    # Buscar la cita por id y actualizarla
    for i, cita in enumerate(datos):
        if cita["id"] == id_cita:
            datos[i] = nuevo_dato
            guardar_citas(file, datos)
            return True
        else:
            print(f"No se encontró ninguna cita con el id {id_cita}.")
    return False

def eliminar_cita(file, id_cita):
    # Cargar los datos del archivo JSON
    datos = cargar_citas(file)
    # Filtrar las citas que no coincidan con el id a eliminar
    nuevos_datos = [cita for cita in datos if cita["id"] != id_cita]
    if len(nuevos_datos) < len(datos):
        guardar_citas(file, nuevos_datos)
        return True
    else:
        print(f"No se encontró ninguna cita con el id {id_cita}.")
    return False