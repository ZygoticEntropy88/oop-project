from persistencia import IPersistencia
from fecha import Fecha, Meses 
from tarjeta import TarjetaCredito

from listas import Lista, CatalogoPersonal
from canciones import Cancion
from tarjeta import TarjetaCredito


class Usuario(IPersistencia):
    def __init__(
        self,
        nombre_de_usuario: str = "user",
        fecha_nacimiento: Fecha = Fecha(),
        correo_electronico: str = "",
        contrasenya: str = "12345678",
        fecha_registro: Fecha = Fecha(),
    ):

        self._nombre_de_usuario: str = nombre_de_usuario
        self._fecha_de_nacimiento: Fecha = fecha_nacimiento
        self._correo_electronico: str = correo_electronico
        self._contrasenya: str = contrasenya
        self._fecha_de_registro: Fecha = fecha_registro
        self._tipo_usuario = "REGULAR"
        self._listas_reproduccion: list['Lista'] = []

    def __str__(self):
        return self.objeto_a_texto()

    def get_nombre_usuario(self):
        return self._nombre_de_usuario

    def get_fecha_nacimiento(self):
        return self._fecha_de_nacimiento

    def get_correo_electronico(self):
        return self._correo_electronico

    def get_contrasenya(self):
        return self._contrasenya

    def get_fecha_registro(self):
        return self._fecha_de_registro

    def get_tipo_usuario(self):
        return self._tipo_usuario

    def get_listas_reproduccion(self):
        return self._listas_reproduccion

    def set_nombre_usuario(self, nuevo_nombre: str):
        self._nombre_de_usuario = nuevo_nombre

    def set_fecha_nacimiento(self, nueva_fecha: Fecha):
        self._fecha_de_nacimiento = nueva_fecha

    def set_correo_electronico(self, nuevo_correo: str):
        self._correo_electronico = nuevo_correo

    def set_contrasenya(self, nueva_contrasenya: str):
        self._contrasenya = nueva_contrasenya

    def set_fecha_registro(self, nueva_fecha_registro: Fecha):
        self._fecha_de_registro = nueva_fecha_registro

    def set_listas_reproduccion(self, nueva_lista_reproduccion: list[Lista]):
        self._listas_reproduccion = nueva_lista_reproduccion

    def crear_nuevo_usuario_por_consola(self):
        nombre_de_usuario: str = input("Ingresa tu nombre de usuario: ")
        correo_electronico: str = input("Ingresa tu correo_electronico: ")
        fecha_nacimiento = Fecha()
        fecha_registro = Fecha()
        fecha_nacimiento.solicitar_usuario("(fecha de nacimiento)")
        fecha_registro.solicitar_usuario("(fecha de registro)")
        contrasenya: str = input("Establece una contraseña: ")

        self.set_nombre_usuario(nombre_de_usuario)
        self.set_correo_electronico(correo_electronico)
        self.set_fecha_nacimiento(fecha_nacimiento)
        self.set_fecha_registro(fecha_registro)
        self.set_contrasenya(contrasenya)

    def solicitar_login_por_consola(self):
        nombre_de_usuario: str = input("Ingresa tu nombre de usuario: ")
        contrasenya: str = input("Ingresa tu contraseña: ")
        self.set_nombre_usuario(nombre_de_usuario)
        self.set_contrasenya(contrasenya)

    def crear_lista_reproduccion(self, lista_canciones: list["Cancion"]):
        nombre_lista: str = str(input("Ingrese el nombre de la lista"))
        descripcion_lista: str = str(input("Añade una descripción a la lista"))
        fecha_creacion: "Fecha" = Fecha(10, Meses.NOVIEMBRE, 2025)
        nueva_lista: "Lista" = Lista(
            nombre_lista, descripcion_lista, lista_canciones, fecha_creacion, self
        )
        return nueva_lista

    def devolver_lista_por_nombre(self, nombre_lista):
        encontrada = False
        lista_encontrada = None
        posicion = 0
        while not encontrada and posicion < len(self.get_listas_reproduccion()):
            if self.get_listas_reproduccion()[posicion].get_nombre() == nombre_lista:
                encontrada = True
                lista_encontrada = self.get_listas_reproduccion()[posicion]
            else:
                posicion += 1
        if not encontrada:
            print(f"La lista {nombre_lista} no se pudo encontrar.")
        return posicion, lista_encontrada
    @staticmethod
    def comprobar_acceso_premium():
        return False

    def comprobar_lista_en_listas_de_reproduccion(self, nombre_lista : str):
        contador : int = 0
        encontrada : bool = False
        while contador < len(self.get_listas_reproduccion()) and not encontrada:
            if nombre_lista == self.get_listas_reproduccion()[contador].get_nombre():
                encontrada = True
            contador +=1
        return encontrada
    # ===================================================================================
    #                  IMPLEMENTACIONES DE LA INTERFAZ DE PERSISTENCIA
    # ===================================================================================
    def objeto_a_texto(self):
        usuario_texto: str = f"\tUSUARIO {self.get_tipo_usuario()}| "
        usuario_texto += f"Nombre de usuario:  {self.get_nombre_usuario()} ; "
        usuario_texto += f"Fecha nacimiento:  {self.get_fecha_nacimiento()} ; "
        usuario_texto += f"Correo electronico:  {self.get_correo_electronico()} ; "
        usuario_texto += f"Contrasenya:  {self.get_contrasenya()} ;"
        usuario_texto += f"\n\n \t\tLISTAS DE REPRODUCCIÓN:\n"
        if self.get_listas_reproduccion():
            for lista_reproduccion in self.get_listas_reproduccion():
                usuario_texto += f"\t\t\t{lista_reproduccion}"
        return usuario_texto


    def objeto_a_diccionario(self):
        usuario = {
            "Nombre de usuario": self.get_nombre_usuario(),
            "Correo electronico": self.get_correo_electronico(),
            "Contrasenya": self.get_contrasenya(),
            "Fecha registro": self.get_fecha_registro().objeto_a_diccionario(),
            "Fecha nacimiento": self.get_fecha_nacimiento().objeto_a_diccionario(),
            "Tipo usuario": self.get_tipo_usuario(),
        }
        return usuario

    def diccionario_a_objeto(self, diccionario_usuario: dict):
        try:
            if (
                "Nombre de usuario" in diccionario_usuario
                and diccionario_usuario["Nombre de usuario"]
            ):
                self.set_nombre_usuario(diccionario_usuario["Nombre de usuario"])

            if (
                "Fecha nacimiento" in diccionario_usuario
                and diccionario_usuario["Fecha nacimiento"]
            ):
                fecha_nacimiento = Fecha()
                fecha_nacimiento.diccionario_a_objeto(
                    diccionario_usuario["Fecha nacimiento"]
                )
                self.set_fecha_nacimiento(fecha_nacimiento)

            if (
                "Correo electronico" in diccionario_usuario
                and diccionario_usuario["Correo electronico"]
            ):
                self.set_correo_electronico(diccionario_usuario["Correo electronico"])

            if (
                "Contrasenya" in diccionario_usuario
                and diccionario_usuario["Contrasenya"]
            ):
                self.set_contrasenya(diccionario_usuario["Contrasenya"])

            if (
                "Fecha registro" in diccionario_usuario
                and diccionario_usuario["Fecha registro"]
            ):
                fecha_registro = Fecha()
                fecha_registro.diccionario_a_objeto(
                    diccionario_usuario["Fecha registro"]
                )
                self.set_fecha_registro(fecha_registro)

        except Exception as error:
            raise ValueError(f"Valor erróneo en lo que se haya introducido {error}")


class UsuarioPremium(Usuario):
    def __init__(
        self,
        usuario_base: "Usuario" = Usuario(),
        tarjeta_credito: "TarjetaCredito" = TarjetaCredito(),
        catalogo_personal: "CatalogoPersonal" = None,
    ):

        super().__init__(
            nombre_de_usuario=usuario_base.get_nombre_usuario(),
            fecha_nacimiento=usuario_base.get_fecha_nacimiento(),
            correo_electronico=usuario_base.get_correo_electronico(),
            contrasenya=usuario_base.get_contrasenya(),
            fecha_registro=usuario_base.get_fecha_registro(),
        )
        self._tipo_usuario = "PREMIUM"
        self._tarjeta_de_credito = tarjeta_credito
        self._catalogo_personal = catalogo_personal

    def get_tarjeta_credito(self):
        return self._tarjeta_de_credito

    def get_catalogo_personal(self):
        return self._catalogo_personal

    def set_tarjeta_credito(self, nueva_tarjeta: "TarjetaCredito"):
        self._tarjeta_de_credito = nueva_tarjeta

    def set_catalogo_personal(self, nuevo_catalogo_personal: "CatalogoPersonal"):
        self._catalogo_personal = nuevo_catalogo_personal

    def anyadir_cancion_a_catalogo(self, cancion: Cancion):
        self.get_catalogo_personal().anyadir_cancion_a_catalogo(cancion)

    def eliminar_cancion_de_catalogo(self, cancion: Cancion):
        nuevo_catalogo_personal = (
            self.get_catalogo_personal().eliminar_cancion_de_catalogo(cancion)
        )
        self.set_catalogo_personal(nuevo_catalogo_personal)

    @staticmethod
    def comprobar_acceso_premium():
        return True

    def crear_nuevo_usuario_premium_por_consola(self, usuario_base: Usuario):
        self.set_nombre_usuario(usuario_base.get_nombre_usuario())
        self.set_fecha_nacimiento(usuario_base.get_fecha_nacimiento())
        self.set_correo_electronico(usuario_base.get_correo_electronico())
        self.set_contrasenya(usuario_base.get_contrasenya())
        self.set_fecha_registro(usuario_base.get_fecha_registro())

        tarjeta = TarjetaCredito()
        tarjeta.crear_tarjeta_por_consola()
        self.set_tarjeta_credito(tarjeta)

    def crear_lista_reproduccion(self, lista_canciones: list["Cancion"]):
        contador: int = 0
        pertenece_a_catalogo_personal: bool = True
        while (
            contador < len(lista_canciones) and pertenece_a_catalogo_personal
        ):  # Compruebo que todas las canciones que implemento están en el catálogo personal
            if lista_canciones[contador] not in self.get_catalogo_personal():
                pertenece_a_catalogo_personal = False
        contador += 1
        if pertenece_a_catalogo_personal:
            nombre_lista: str = str(input("Ingrese el nombre de la lista"))
            descripcion_lista: str = str(input("Añade una descripción a la lista"))
            fecha_creacion: "Fecha" = Fecha(10, Meses.NOVIEMBRE, 2025)
            nueva_lista: "Lista" = Lista(
                nombre_lista, descripcion_lista, lista_canciones, fecha_creacion, self
            )
            return nueva_lista
        else:
            return -1

    def diccionario_a_objeto(self, diccionario_usuario_premium: dict):
        super().diccionario_a_objeto(diccionario_usuario_premium)
        if (
            "Tarjeta de credito" in diccionario_usuario_premium
            and diccionario_usuario_premium["Tarjeta de credito"]
        ):
            self.get_tarjeta_credito().diccionario_a_objeto(
                diccionario_usuario_premium["Tarjeta de credito"]
            )

    def objeto_a_diccionario(self) -> dict:
        diccionario: dict = super().objeto_a_diccionario()
        diccionario["Tarjeta de credito"] = (
            self.get_tarjeta_credito().objeto_a_diccionario()
        )
        return diccionario


class UsuarioAnonimo:
    def __init__(self):
        self._tipo_usuario = "ANONIMO"

    def get_nombre_usuario(self):
        return "Usuario anónimo"

    def get_tipo_usuario(self):
        return self._tipo_usuario

    @staticmethod
    def comprobar_acceso_premium():
        return False
