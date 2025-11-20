from canciones import Cancion
from usuarios import Usuario, UsuarioPremium
from persistencia import GestorPersistencia
from listas import Catalogo, CatalogoPersonal, Lista




class Memoria:
    def __init__(self, ruta="db/"):

        self.ruta = ruta

        self.__gp = GestorPersistencia()

        # ESTABLEZCO LOS USUARIOS
        usuarios: dict[str : "Usuario"] = dict()
        for usuario_info in self.__gp.leer_json(f"{ruta}usuarios.json"):

            if usuario_info["Tipo usuario"] == "REGULAR":
                usuario = Usuario()
                usuario.diccionario_a_objeto(usuario_info)

            elif usuario_info["Tipo usuario"] == "PREMIUM":
                usuario = UsuarioPremium()
                usuario.diccionario_a_objeto(usuario_info)

                # ESTABLEZO LOS CATÁLOGOS PERSONALES
                lista_canciones_catalogo_personal = list()
                for cancion_info in self.__gp.leer_csv(
                    f"{ruta}catalogos_personales/{usuario.get_nombre_usuario()}.csv"
                ):
                    cancion = Cancion()
                    cancion.diccionario_a_objeto(cancion_info)
                    lista_canciones_catalogo_personal.append(cancion)
                usuario.set_catalogo_personal(
                    CatalogoPersonal(lista_canciones_catalogo_personal)
                )

            usuarios[usuario.get_nombre_usuario()] = usuario

            # CARGO LAS LISTAS DE REPRODUCCIÓN
            listas_reproduccion_usuario: list[Lista] = list()
            for lista_info in self.__gp.leer_json(
                f"{ruta}listas_reproduccion/{usuario.get_nombre_usuario()}.json"
            ):
                lista = Lista()
                lista.diccionario_a_objeto(lista_info)
                listas_reproduccion_usuario.append(lista)
            usuario.set_listas_reproduccion(listas_reproduccion_usuario)

        self._usuarios = usuarios

        # CARGO EL CATÁLOGO GENÉRICO
        lista_canciones_catalogo_generico = list()
        for cancion_info in self.__gp.leer_csv(f"{ruta}catalogo_generico.csv"):
            cancion = Cancion()
            cancion.diccionario_a_objeto(cancion_info)
            lista_canciones_catalogo_generico.append(cancion)
        self._catalogo_generico = Catalogo(lista_canciones_catalogo_generico)

    def __str__(self):
        msg = "===================================MEMORIA=========================================\n"
        msg += f"\t ·USUARIOS = \n\n"
        for usuario in self._usuarios.values():
            msg += f"\t{usuario}\n"
        msg += "\n"

        msg += f"\t ·CATÁLOGO GENÉRICO = [\n"
        for cancion in self.get_catalogo_generico().get_lista_canciones():
            msg += f"\t\t{cancion}\n"
        msg += "\n"
        """
        msg += f"\t ·LISTAS REPRODUCCIÓN =  \n"
        for usuario in self._listas_reproduccion.values():
            msg += f"\t\t {usuario}"
        msg += "\n"
        """

        return msg

    def get_usuarios(self):
        return self._usuarios

    def get_catalogo_generico(self):
        return self._catalogo_generico

    def guardar_en_disco(self):
        """Este método se ejecuta antes de salir de la aplicación: guarda toda la memoria en el disco duro"""

        # GUARDADO DE LOS USUARIOS
        try:
            usuarios_info = list()
            for usuario in self.get_usuarios().values():
                usuarios_info.append(usuario.objeto_a_diccionario())

                # GUARDO EL CATÁLOGO PERSONAL DE CADA USUARIO
                print("DEEEBUG", usuario)
                if (
                    usuario.comprobar_acceso_premium()
                    and usuario.get_catalogo_personal()
                ):
                    self.__gp.resetear_csv_manteniendo_cabeceras(
                        f"{self.ruta}catalogos_personales/{usuario.get_nombre_usuario()}.csv"
                    )
                    for (
                        cancion_info
                    ) in usuario.get_catalogo_personal().objeto_a_diccionario():
                        self.__gp.guardar_csv(
                            contenido=cancion_info,
                            ruta=f"{self.ruta}catalogos_personales/{usuario.get_nombre_usuario()}.csv",
                        )

                if (
                    usuario.get_listas_reproduccion()
                    and usuario.get_listas_reproduccion() != []
                ):
                    usuario_listas_reproduccion = list()
                    for lista_reproduccion in usuario.get_listas_reproduccion():
                        usuario_listas_reproduccion.append(
                            lista_reproduccion.objeto_a_diccionario()
                        )
                    self.__gp.guardar_json(
                        contenido= usuario_listas_reproduccion,
                        ruta=f"{self.ruta}listas_reproduccion/{usuario.get_nombre_usuario()}.json",
                    )

            # GUARDO TODOS LOS USUARIOS COMO UN <<CONGLOMERADO>> DE USUARIOS, ES DECIR HAGO UN ÚNICO DUMP
            self.__gp.guardar_json(
                contenido=usuarios_info, ruta=f"{self.ruta}usuarios.json"
            )

        except Exception as e:
            print(e)

        # EL CATÁLOGO GENÉRICO NO CAMBIA, ES FIJO. POR TANTO NO TENGO QUE INTERACTUAR CON ÉL EN DISCO

    def anyadir_usuario(self, usuario: "Usuario"):
        self._usuarios[usuario.get_nombre_usuario()] = usuario

    def comprobar_usuario_registrado(self, nombre: str) -> bool:
        """Dado un nombre de usuario, verifica que esté en la base de datos"""
        return (
            True
            if nombre in self.get_usuarios() and self.get_usuarios()[nombre]
            else False
        )

    def comprobar_cancion_en_catalogo(self, id_cancion: str):
        for cancion in self.get_catalogo_generico().get_lista_canciones():
            if cancion.get_identificador() == id_cancion:
                return True
        return False

    def comprobar_cancion_en_catalogo_premium(
        self, id_cancion: str, nombre_usuario: str
    ):
        if self.get_usuarios()[nombre_usuario].comprobar_acceso_premium() != "PREMIUM":
            return False
        for cancion in self.get_usuarios()[nombre_usuario].get_catalogo_personal().get_lista_canciones():
            if cancion.get_identificador() == id_cancion:
                return True
        return False


    def comprobar_credenciales_validas(self, nombre: str, contrasenya: str) -> bool:
        """Comprueba que el usuario esté registrado y que la contraseña coincida con la guardada en la base de datos"""
        if self.comprobar_usuario_registrado(nombre):
            if contrasenya == self.get_usuarios()[nombre].get_contrasenya():
                return True
            print("Contraseña no válida.")
        else:
            print(f"Usuario {nombre} no registrado en la base de datos.")
        return False

    def cargar_usuario_por_nombre_y_contrasenya(self, nombre: str, contrasenya: str):
        if self.comprobar_credenciales_validas(nombre, contrasenya):
            return self.get_usuarios()[nombre]
