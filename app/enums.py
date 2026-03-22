from enum import Enum

class Estado(str, Enum):
    disponible = "disponible"
    en_uso = "en_uso"
    mantenimiento = "mantenimiento"
    sin_bateria = "sin_bateria"