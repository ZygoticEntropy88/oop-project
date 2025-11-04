"""
PROJECTO POO (menu.py) - TECNOLOGÍA DE LA PROGRAMACIÓN
"""
from abc import ABC, abstractmethod

def print_opcion(numero:int, opcion:str) -> None:
    print(f"[{numero}]: {opcion}")

class Menu(ABC):

    id:int = 0
    opciones = []

    @classmethod
    def imprimir(cls):
        print_opcion(0, "Salir de la aplicación")
        print_opcion(1, "Volver al menú anterior")
        for opcion_id in range(0, len(cls.opciones)):
            print_opcion(opcion_id, cls.opciones[opcion_id])

    @classmethod
    @abstractmethod
    def ejecutar(cls, opcion:int):
        assert isinstance(opcion, int) and opcion >= 0, "La selección de opción debe ser un número positivo mayor que cero"

        if opcion == 0:
            cls.salir()
        elif opcion == 1:
            cls.menu_anterior()

    @classmethod
    def menu_anterior(cls) -> int:
        if cls.id == 0:
            return cls.id
        return cls.id - 1

    @classmethod
    def menu_siguiente(cls) -> int:
        if cls.id > 2:
            return cls.id
        return cls.id + 1

    @staticmethod
    def salir():
        quit()