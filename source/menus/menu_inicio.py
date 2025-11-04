from .menu import Menu

class MenuInicio(Menu):
    id = 0
    opciones = [
        "Registrar un usuario",
        "Login con usuario y contraseña",
        "Continuar como invitado"
    ]

    @classmethod
    def ejecutar(cls, opcion:int):
        super().ejecutar(opcion)
        if opcion == 2:
            cls.registrar()
        elif opcion == 3:
            cls.login()
        elif opcion == 4:
            cls.continuar_como_invitado()

    @classmethod
    def registrar(cls):
        nombre:str = input("Ingresa tu nombre: ")
        apellidos:str = input("Ingresa tu apellido: ")
        email:str = input("Ingresa tu email: ")
        fecha_nacimiento:str = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")
        fecha_registro:str = input("Ingresa la fecha de hoy (dd/mm/aaaa): ")
        contrasenya:str = input("Establece una contraseña: ")

        usuario


    @classmethod
    def login(cls):
        pass

    @classmethod
    def continuar_como_invitado(cls):
        pass
