from .usuario import Usuario
from .usuario import Fecha
from persistencia.interfaz_persistencia import IPersistencia
from listas import Lista
from canciones import Cancion

class TarjetaCredito (IPersistencia):
    def __init__(self, numero_de_cuenta : int,
                 CVV : int,
                 fecha_de_caducidad : Fecha,
                 nombre_completo_titular : str,
                 propietario : str = None):

        assert (len(str(numero_de_cuenta)) == 16 and
                len(str(CVV)) == 3), "Los datos introducidos no son válidos"

        self._numero_de_cuenta = numero_de_cuenta
        self._CVV = CVV
        self._fecha_de_caducidad = fecha_de_caducidad
        self._nombre_completo_titular = nombre_completo_titular
        self._propietario = propietario

    def get_numero_cuenta (self):
        return self._numero_de_cuenta

    def get_CVV (self):
        return self._CVV

    def get_fecha_caducidad (self):
        return self._fecha_de_caducidad

    def get_nombre_titular (self):
        return self._nombre_completo_titular

    def get_propietario (self):
        return self._propietario

    def set_numero_cuenta (self, nuevo_numero_cuenta : int):
        self._numero_de_cuenta = nuevo_numero_cuenta

    def set_CVV (self, nuevo_CVV : int):
        self._CVV = nuevo_CVV

    def set_fecha_caducidad (self, nueva_fecha_caducidad : Fecha):
        self._fecha_de_caducidad = nueva_fecha_caducidad

    def set_nombre_titular (self, nuevo_nombre_titular : str):
        self._nombre_completo_titular = nuevo_nombre_titular

    def set_propietario (self, nuevo_propietario : str):
        self._propietario = nuevo_propietario

    def objeto_a_diccionario (self):
        tarjeta = {
            "Numero de cuenta": self.get_numero_cuenta(),
            "CVV": self.get_CVV(),
            "Fecha de caducidad": self.get_fecha_caducidad(),
            "Nombre del titular": self.get_nombre_titular(),
            "Propietario" : self.get_propietario()
        }
        return tarjeta

    def diccionario_a_objeto(self, diccionario_tarjeta: dict):
        try:
            if "Numero de cuenta" in diccionario_tarjeta and diccionario_tarjeta["Numero de cuenta"]:
                self.set_numero_cuenta(diccionario_tarjeta["Numero de cuenta"])

            if "CVV" in diccionario_tarjeta and diccionario_tarjeta["CVV"]:
                self.set_CVV(diccionario_tarjeta["CVV"])

            if "Fecha de caducidad" in diccionario_tarjeta and diccionario_tarjeta["Fecha de caducidad"]:
                self.set_fecha_caducidad(diccionario_tarjeta["Fecha de caducidad"])

            if "Nombre del titular" in diccionario_tarjeta and diccionario_tarjeta["Nombre del titular"]:
                self.set_nombre_titular(diccionario_tarjeta["Nombre del titular"])

            if "Propietario" in diccionario_tarjeta and diccionario_tarjeta["Propietario"]:
                self.set_propietario(diccionario_tarjeta["Propietario"])

        except Exception as error:
            raise ValueError(f"Valor erróneo en lo que se haya introducido {error}")

class UsuarioPremium(Usuario):
    def __init__(self, nombre_usuario : str,
                 fecha_nacimiento : Fecha,
                 correo_electronico : str,
                 contrasenya : str,
                 fecha_registro : Fecha,
                 tarjeta_credito : TarjetaCredito):

        super().__init__(nombre_de_usuario = nombre_usuario,
                       fecha_nacimiento = fecha_nacimiento,
                       correo_electronico = correo_electronico,
                       contrasenya = contrasenya,
                       fecha_registro = fecha_registro)
        self._tarjeta_de_credito = tarjeta_credito

    def get_tarjeta_credito (self):
        return self._tarjeta_de_credito

    def crear_lista_reproduccion(self, lista_canciones : list['Cancion']): #Tengo que permitir que un usuario dado cree una lista de reproduccion
        nombre_lista: str = str(input("Ingrese el nombre de la lista"))
        descripcion_lista: str = str(input("Añade una descripción a la lista"))
        fecha_creacion :'Fecha' = Fecha(10, 11, 2025)
        nueva_lista: 'Lista' = Lista(nombre_lista, descripcion_lista, lista_canciones, fecha_creacion, self)
        return nueva_lista

    def objeto_a_diccionario(self):
        super().objeto_a_diccionario()
        self.get_tarjeta_credito().objeto_a_diccionario()

    def diccionario_a_objeto(self, diccionario_usuario_premium : dict):
        super().diccionario_a_objeto(diccionario_usuario_premium)
        self.get_tarjeta_credito().objeto_a_diccionario()