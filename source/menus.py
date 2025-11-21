from abc import ABC
from usuarios import Usuario, UsuarioPremium
from listas import Lista, Catalogo, CatalogoPersonal
from canciones import Cancion
from fecha import Fecha


def print_opcion(numero: int, opcion: str) -> None:
    print(f"[{numero}]: {opcion}")


class Menu(ABC):

    numero_menu: int = 0
    opciones = []
    nombre_menu: str = ""

    @classmethod
    def imprimir(cls, nombre_usuario:str):
        print(f"{cls.get_nombre_menu()} | Usuario: {nombre_usuario}")
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
from reproductor import *  # Me traigo del módulo reproductor todas sus clases, incluidas las excepciones


class MenuReproduccion(Menu):
    numero_menu = 2
    opciones = [
        "Reproducir canción por ID",
        "Pausar reproducción de la canción",
        "Renaudar reproducción",
    ]
    nombre_menu = "MENÚ REPRODUCCIÓN"

    reproductor: Reproductor = (
        Reproductor()
    )  # Cuando llamo al menú, instancio un objeto de la clase reproductor

    @classmethod
    def reproducir_por_id(cls):
        id_cancion: str = input("Introduzca el id de la canción que desea reproducir: ")
        if not id_cancion or id_cancion == "":
            raise EntradaInvalidaError("El id introducido no es válido.")
        else:
            MenuReproduccion.reproductor.reproducir_desde_youtube(id_cancion)
        return id_cancion

        # Voy filtrando de los errores más específicos a los más genéricos y capturo y lanzo excepciones para que el programa se corte
        # y el error no se propague

    @classmethod
    def pausar_cancion(cls):
        if (
            MenuReproduccion.reproductor.obtener_estado_reproductor()
            != EstadoReproductor.REPRODUCIENDO
        ):
            raise PlayError("La canción no está sonando")
        # Compruebo que la canción está reproduciéndose
        else:
            MenuReproduccion.reproductor.pausar()

    @classmethod
    def reanudar_cancion(cls):
        if (
            MenuReproduccion.reproductor.obtener_estado_reproductor()
            != EstadoReproductor.PAUSADO
        ):
            raise PlayError("Error al reanudar")
        else:
            MenuReproduccion.reproductor.reanudar()


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
    opciones = ["Listar catálogo personal", "Añadir canción", "Eliminar canción"]
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
        nueva_cancion = Cancion()
        nueva_cancion.solicitar_usuario_por_consola()
        return nueva_cancion

    @classmethod
    def eliminar_cancion(cls):
        cancion_a_eliminar = Cancion()
        cancion_a_eliminar.solicitar_usuario_por_consola(
            "(Que desea eliminar)", eliminar=True
        )
        return cancion_a_eliminar

# ====================================== MENU LISTAS REPRODUCCIÓN =====================================
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
    def mostrar_todas_las_listas(cls, listas_de_reproduccion: list['Lista']):
        contador: int = 1
        for lista in listas_de_reproduccion:
            print(f"Lista {contador} : {lista} \n")
            contador += 1

    @classmethod
    def mostrar_canciones_en_lista(cls, listas_de_reproduccion: list['Lista']):
        nombre_lista: str = input("Introduzca el nombre de la lista que desea mostrar: ")
        contador: int = 0
        lista_encontrada: bool = False
        while contador < len(listas_de_reproduccion) and not lista_encontrada:
            if listas_de_reproduccion[contador].get_nombre() == nombre_lista:
                lista_encontrada = True
                canciones:list['Cancion'] = listas_de_reproduccion[contador].get_lista_canciones()
                if canciones and canciones != []:
                    for cancion in canciones:
                        print(f"{cancion} \n")
                else:
                    print("Lista vacía")
            contador += 1
        if not lista_encontrada:
            print("Lista no encontrada")

    @classmethod
    def crear_lista(cls):
        nombre_lista = input("Introduzca el nombre de la lista: ")
        descripcion_lista = input("Introduzca la descripcion de la lista: ")
        fecha = Fecha()
        fecha.solicitar_usuario("(Fecha actual)")
        id_canciones:list['str'] = list()
        seguir_anyadiendo:bool = True
        while seguir_anyadiendo:
            id_cancion:str = input("Introduzca el ID de la canción que desea añadir (presione enter para terminar el proceso): ")
            if id_cancion == "":
                seguir_anyadiendo = False
            else: 
                id_canciones.append(id_cancion)
        return (nombre_lista, descripcion_lista, fecha, id_canciones)


    @classmethod
    def eliminar_lista(
        cls, usuario_actual : 'Usuario'
    ):
        nombre_lista : str = input("Introduzca el nombre de la lista que desea eliminar: ")
        contador : int = 0
        encontrada : bool = False
        while contador < len(usuario_actual.get_listas_reproduccion()) and not encontrada:
            if usuario_actual.get_listas_reproduccion()[contador].get_nombre() == nombre_lista:
                usuario_actual.get_listas_reproduccion().remove(usuario_actual.get_listas_reproduccion()[contador])
                encontrada = True
            contador += 1
        if not encontrada:
            print("No se ha encontrado la lista")

    @classmethod
    def anyadir_cancion_a_lista(
        cls
    ):
        id_cancion:str = input("Introduzca el ID de la canción que desea añadir: ")
        nombre_lista:str = input("Introduzca el nombre de la lista a la que quiere añadir la cancion: ")
        return id_cancion, nombre_lista

    @classmethod
    def solicitar_lista_a_eliminar(
        cls
    ):
        nombre_lista:str = input("Introduce el nombre de la lista donde quieres borrar una cancion: ")
        return nombre_lista

    @classmethod
    def solicitar_cancion_a_eliminar(
        cls
    ):
        nombre_cancion:str = input("Introduce el ID de la canción que quieres borrar: ")
        return nombre_cancion