import json
from typing import List, Dict

def leer_json(ruta: str) -> List[Dict]:
    try:
        with open(ruta, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def escribir_json(ruta: str, data: List[Dict]) -> None:
    with open(ruta, "w") as f:
        json.dump(data, f, indent=4)
