from .menu import Menu

class MenuInicio(Menu):
    numero_menu = 0
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
        

        """
        Introducimos correo y contraseña.
        Compruebo en qué csv (si premium o regular) está el correo
        Si está en premium, mi variable vale x
        Si está en regular, mi variable vale y

        """

        pass

    @classmethod
    def continuar_como_invitado(cls):
        pass
