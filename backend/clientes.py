
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