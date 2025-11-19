from abc import ABC, abstractmethod
from usuarios import Usuario, UsuarioPremium


def print_opcion(numero: int, opcion: str) -> None:
    print(f"[{numero}]: {opcion}")


class Menu(ABC):

    numero_menu: int = 0
    opciones = []
    nombre_menu: str = ""

    @classmethod
    def imprimir(cls):
        print(cls.get_nombre_menu())
        print_opcion(0, "Salir de la aplicación")
        print_opcion(1, "Volver al menú anterior")
        for opcion_id in range(len(cls.opciones)):
            print_opcion(opcion_id + 2, cls.opciones[opcion_id])

    @classmethod
    def get_numero_menu(cls) -> int:
        return cls.numero_menu

    @classmethod
    def get_nombre_menu(cls) -> str:
        return f"\n================================== {cls.nombre_menu} =================================="


class MenuInicio(Menu):
    numero_menu = 0
    opciones = [
        "Registrar un usuario",
        "Login con usuario y contraseña",
        "Continuar como invitado",
    ]
    nombre_menu = "MENÚ INICIO"

    @classmethod
    def registrar(cls) -> "Usuario":
        nuevo_usuario = Usuario()
        nuevo_usuario.crear_nuevo_usuario_por_consola()
        opcion_registrar_usuario_premium = (
            input("Quieres hacer tu cuenta premium? (s/n): ").lower().strip()
        )
        if opcion_registrar_usuario_premium == "s":
            nuevo_usuario_premium = UsuarioPremium()
            nuevo_usuario_premium.crear_nuevo_usuario_premium_por_consola(
                usuario_base=nuevo_usuario
            )
            return nuevo_usuario_premium
        else:
            return nuevo_usuario

    @classmethod
    def login(cls):
        nuevo_usuario = Usuario()
        nuevo_usuario.solicitar_login_por_consola()
        return nuevo_usuario

    @classmethod
    def continuar_como_invitado(cls):
        pass


# ======================================== MENU PRINCIPAL ==============================================
class MenuPrincipal(Menu):
    numero_menu = 1
    opciones = [
        "·Menu reproducción",
        "·Menu catálogo genérico",
        "+Menu catálogo personal",
        "-Menu listas reproducción",
    ]
    nombre_menu = "MENÚ PRINCIPAL"


# ======================================== MENU REPRODUCCIÓN ==============================================
class MenuReproduccion(Menu):
    numero_menu = 2
    opciones = [
        "Reproducir canción por ID",
        "Pausar reproducción de la canción",
        "Renaudar reproducción",
    ]
    nombre_menu = "MENÚ REPRODUCCIÓN"

    @classmethod
    def reproducir_por_id(cls):
        pass

    @classmethod
    def pausar_cancion(cls):
        pass

    @classmethod
    def renaudar_cancion(cls):
        pass


# ================================= MENU CATÁLOGO GENÉRICO ==========================================
class MenuCatalogoGenerico(Menu):
    numero_menu = 3
    opciones = [
        "Listar canciones",
    ]
    nombre_menu = "MENÚ CATÁLOGO GENÉRICO"

    @classmethod
    def listar_canciones(cls, catalogo_generico: "Catalogo"):
        filtrar_por_genero: str = input(
            "Escriba el género que desea filtrar (presione Enter si desea ver todos los géneros): "
        )
        filtrar_por_artista: str = input(
            "Escriba el artista que desea filtrar (presione Enter si desea ver todos los artistas): "
        )
        filtrar_por_genero = (
            filtrar_por_genero.lower() if filtrar_por_genero != "" else None
        )
        filtrar_por_artista = (
            filtrar_por_artista.lower() if filtrar_por_artista != "" else None
        )
        catalogo_generico.listar_canciones(
            filtrar_por_genero=filtrar_por_genero,
            filtrar_por_artista=filtrar_por_artista,
        )


# ====================================== MENU CATÁLOGO PERSONAL =====================================
class MenuCatalogoPersonal(Menu):
    numero_menu = 4
    opciones = ["Listar canciones", "Añadir canción", "Eliminar canción"]
    nombre_menu = "MENÚ CATÁLOGO PERSONAL"

    @classmethod
    def listar_catalogo_personal(cls, catalogo_personal: "CatalogoPersonal"):
        filtrar_por_genero: str = input(
            "Escriba el género que desea filtrar (presione Enter si desea ver todos los géneros): "
        )
        filtrar_por_artista: str = input(
            "Escriba el artista que desea filtrar (presione Enter si desea ver todos los artistas): "
        )
        filtrar_por_genero = (
            filtrar_por_genero.lower() if filtrar_por_genero != "" else None
        )
        filtrar_por_artista = (
            filtrar_por_artista.lower() if filtrar_por_artista != "" else None
        )
        catalogo_personal.listar_canciones(
            filtrar_por_genero=filtrar_por_genero,
            filtrar_por_artista=filtrar_por_artista,
        )

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
        "Eliminar canción de la lista",
    ]
    nombre_menu = "MENÚ LISTAS REPRODUCCIÓN"

    @classmethod
    def ejecutar(cls, opcion: int):
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
