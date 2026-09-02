
import json

FILE = "usuarios.json"


def cargar_usuarios(FILE):
    
    # Abrir y cargar el archivo JSON
    with open(FILE, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)
    

def guardar_usuarios(name,data):
    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)