from .menu import Menu


class MenuInicio(Menu):
    id = 0
    opciones = [
        "Registrar un usuario",
        "Login con usuario y contraseña",
        "Continuar sin identificarse"
    ]

    @classmethod
    def ejecutar(cls, opcion:int):
        pass

    @classmethod
    def login(cls):
        pass

    @classmethod
    def registrar(cls):
        pass

    @classmethod
    def continuar_como_invitado(cls):
        pass
