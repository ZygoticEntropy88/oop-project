from menu import Menu

class MenuCatalogoGenerico(Menu):
    id = 3
    opciones = [
        "Listar canciones"
    ]

    @classmethod
    def ejecutar(cls, opcion:int):
        pass

    @classmethod
    def listar_canciones(cls):
        pass