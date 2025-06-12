import json
from typing import Any

def leer_json(ruta: str) -> Any:
    """
    Lee un archivo JSON y devuelve su contenido como un objeto de Python.
    
    :param ruta: Ruta al archivo JSON.
    :return: Datos cargados desde el archivo JSON.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía (o dict vacío según contexto)
        return []
    except json.JSONDecodeError:
        # Si el JSON está corrupto o vacío, devolver lista vacía para evitar errores
        return []

def guardar_json(ruta: str, datos: Any) -> None:
    """
    Guarda datos en un archivo JSON.
    
    :param ruta: Ruta al archivo JSON.
    :param datos: Datos a guardar (lista, dict, etc.).
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

