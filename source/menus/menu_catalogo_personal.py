from menu import Menu

class MenuCatalogoPersonal(Menu):
    id = 4
    opciones = [
        "Listar canciones",
        "Añadir canción",
        "Eliminar canción"
    ]

    @classmethod
    def ejecutar(cls, opcion:int):
        pass

    @classmethod
    def listar_catalogo_personal(cls):
        pass

    @classmethod
    def anyadir_cancion(cls):
        pass

    @classmethod
    def eliminar_cancion(cls):
        pass