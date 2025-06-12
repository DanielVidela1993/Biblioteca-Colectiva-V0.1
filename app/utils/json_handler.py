import json
from typing import Any

def leer_json(ruta: str) -> Any:
    """
    Lee datos desde un archivo JSON y devuelve los datos en formato Python (lista o dict).
    Si el archivo no existe o está vacío/corrupto, devuelve una lista vacía para evitar errores.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def escribir_json(ruta: str, datos: Any) -> None:
    """
    Escribe datos (lista o dict) en un archivo JSON con indentado legible y codificación UTF‑8.
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


