from menu import Menu


class MenuListasReproduccion(Menu):
    id = 5
    opciones = [
        "Mostrar todas las listas",
        "Mostrar canciones en una lista",
        "Crear lista",
        "Eliminar lista",
        "Añadir canción a la lista",
        "Eliminar canción de la lista"
    ]

    @classmethod
    def ejecutar(cls, opcion:int):
        pass

    @classmethod
    def mostrar_todas_las_listas(cls):
        pass

    @classmethod
    def mostrar_canciones_en_lista(cls):
        pass

    @classmethod
    def crear_lista(cls):
        pass

    @classmethod
    def eliminar_lista(cls):
        pass

    @classmethod
    def anyadir_cancion_a_lista(cls):
        pass

    @classmethod
    def eliminar_cancion_de_lista(cls):
        pass