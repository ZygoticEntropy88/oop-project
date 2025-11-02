from menu import Menu


class MenuPrincipal(Menu):
    id = 1
    opciones = [
        "Menu reproducción",
        "Menu catálogo genérico",
        "Menu catálogo personal",
        "Menu listas reproducción"
    ]

    @classmethod
    def ejecutar(cls, opcion:int):
        pass

    @classmethod
    def menu_reproduccionn(cls):
        pass

    @classmethod
    def menu_catalogo_general(cls):
        pass

    @classmethod
    def menu_catalogo_personal(cls):
        pass

    @classmethod
    def menu_listas_reproduccion(cls):
        pass