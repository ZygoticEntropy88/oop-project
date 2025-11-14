from abc import ABC, abstractmethod
from usuarios import Usuario

def print_opcion(numero:int, opcion:str) -> None:
    print(f"[{numero}]: {opcion}")

class Menu(ABC):

    numero_menu:int = 0
    opciones = []
    nombre_menu:str = ""

    @classmethod
    def imprimir(cls):
        print(cls.get_nombre_menu())
        print_opcion(0, "Salir de la aplicación")
        print_opcion(1, "Volver al menú anterior")
        for opcion_id in range(len(cls.opciones)):
            print_opcion(opcion_id+2, cls.opciones[opcion_id])

    @classmethod
    def get_numero_menu(cls) -> int:
        return cls.numero_menu

    @classmethod
    def get_nombre_menu(cls) -> str:
        return f"\n================================== {cls.nombre_menu} =================================="

    @classmethod
    @abstractmethod
    def ejecutar(cls, opcion:int):
        assert isinstance(opcion, int) and opcion >= 0, "La selección de opción debe ser un número positivo mayor que cero"


class MenuInicio(Menu):
    numero_menu = 0
    opciones = [
        "Registrar un usuario",
        "Login con usuario y contraseña",
        "Continuar como invitado"
    ]
    nombre_menu = "MENÚ INICIO"

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
    def registrar(cls) -> 'Usuario':
        nuevo_usuario = Usuario()
        nuevo_usuario.crear_nuevo_usuario_por_consola()
        return nuevo_usuario


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


class MenuPrincipal(Menu):
    numero_menu = 1
    opciones = [
        "Menu reproducción",
        "Menu catálogo genérico",
        "Menu catálogo personal",
        "Menu listas reproducción"
    ]
    nombre_menu = "MENÚ PRINCIPAL"

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

class MenuReproduccion(Menu):
    numero_menu = 2
    opciones = [
        "Reproducir canción por ID",
        "Pausar reproducción de la canción",
        "Renaudar reproducción"
    ]
    nombre_menu = "MENÚ REPRODUCCIÓN"

    @classmethod
    def ejecutar(cls, opcion:int):
        pass

    @classmethod
    def reproducir_por_id(cls):
        pass

    @classmethod
    def pausar_cancion(cls):
        pass

    @classmethod
    def renaudar_cancion(cls):
        pass

class MenuCatalogoGenerico(Menu):
    numero_menu = 3
    opciones = [
        "Listar canciones"
    ]
    nombre_menu = "MENÚ CATÁLOGO GENÉRICO"

    @classmethod
    def ejecutar(cls, opcion:int):
        pass

    @classmethod
    def listar_canciones(cls):
        pass


class MenuCatalogoPersonal(Menu):
    numero_menu = 4
    opciones = [
        "Listar canciones",
        "Añadir canción",
        "Eliminar canción"
    ]
    nombre_menu = "MENÚ CATÁLOGO PERSONAL"

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

class MenuListasReproduccion(Menu):
    numero_menu = 5
    opciones = [
        "Mostrar todas las listas",
        "Mostrar canciones en una lista",
        "Crear lista",
        "Eliminar lista",
        "Añadir canción a la lista",
        "Eliminar canción de la lista"
    ]
    nombre_menu = "MENÚ LISTAS REPRODUCCIÓN"

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