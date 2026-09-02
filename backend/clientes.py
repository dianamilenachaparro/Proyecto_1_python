
import json

def cargar_usuarios(file):
    try:
        with open(file, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
def guardar_usuarios(name,data):
    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def documento_existe(file, documento):
    # Cargar los datos del archivo JSON
    datos = cargar_usuarios(file)
    # Verificar si el documento ya existe, any devuelve True si encuentra al menos un elemento que cumpla la condición, de lo contrario devuelve False
    return any(usuario["documento"] == documento for usuario in datos)

 
   
       

#eliminar usuario por documento, si existe lo elimina y si no devuelve None
def eliminar_usuario(file, documento):
    datos = cargar_usuarios(file)
    nuevos_datos = [u for u in datos if u ["documento"] != documento]
    guardar_usuarios(file, nuevos_datos)

#actualizar usuario por documento, si existe lo actualiza y si no devuelve None
def actualizar_usuario(file, documento , nuevos_datos):
    datos_nuevos = cargar_usuarios(file)
    for i in range(len(datos_nuevos)):
        if datos_nuevos[i]["documento"] == documento:
            datos_nuevos[i] = nuevos_datos
            break
        guardar_usuarios(file, datos_nuevos)


            
