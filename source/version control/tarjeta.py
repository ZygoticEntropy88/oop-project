from fecha import Fecha
from persistencia import IPersistencia

class TarjetaNoValida(Exception):
    pass
class TarjetaCaducada(Exception):
    pass

class TarjetaCredito (IPersistencia):
    def __init__(self, numero_de_cuenta : int = "",
                 cvv : int = 123,
                 fecha_de_caducidad : Fecha = Fecha(),
                 nombre_completo_titular : str = "nombre",
                 propietario : str = None):

        self._numero_de_cuenta = numero_de_cuenta
        self._cvv = cvv
        self._fecha_de_caducidad = fecha_de_caducidad
        self._propietario = propietario

    def get_fecha_registro(self):
        return self._fecha_de_registro
        
    def get_numero_cuenta (self):
        return self._numero_de_cuenta

    def get_cvv (self):
        return self._cvv

    def get_fecha_caducidad (self):
        return self._fecha_de_caducidad

    def get_propietario (self):
        return self._propietario

    def set_numero_cuenta (self, nuevo_numero_cuenta : int):
        self._numero_de_cuenta = nuevo_numero_cuenta

    def set_cvv (self, nuevo_cvv : int):
        self._cvv = nuevo_cvv

    def set_fecha_registro(self, nueva_fecha_registro: Fecha):
        self._fecha_de_registro = nueva_fecha_registro

    def set_fecha_caducidad (self, nueva_fecha_caducidad : Fecha):
        self._fecha_de_caducidad = nueva_fecha_caducidad

    def set_nombre_titular (self, nuevo_nombre_titular : str):
        self._nombre_completo_titular = nuevo_nombre_titular

    def set_propietario (self, nuevo_propietario : str):
        self._propietario = nuevo_propietario

    def crear_tarjeta_por_consola(self):
        iban = input("Introduce el IBAN de su tarjeta: ")
        cvv = input("Introduce el CVV de su tarjeta: ")
        propietario = input("Introduce el nombre completo del propietario de la tarjeta: ")
        fecha_registro = Fecha()
        fecha_caducidad = Fecha(es_de_caducidad = True)
        fecha_registro.solicitar_usuario("Fecha de registro de la tarjeta")
        fecha_caducidad.solicitar_usuario("Fecha de caducidad de la tarjeta")

        # TODO COMPROBACIONES DE ERRORES
        self.set_numero_cuenta(iban)
        self.set_cvv(cvv)
        self.set_propietario(propietario)
        self.set_fecha_registro(fecha_registro)
        self.set_fecha_caducidad(fecha_caducidad)


    # ===================================================================================
    #                  IMPLEMENTACIONES DE LA INTERFAZ DE PERSISTENCIA
    # ===================================================================================
    def objeto_a_diccionario (self):
        tarjeta = {
            "Numero de cuenta": self.get_numero_cuenta(),
            "cvv": self.get_cvv(),
            "Fecha registro": self.get_fecha_registro(),
            "Fecha caducidad": self.get_fecha_caducidad(),
            "Propietario" : self.get_propietario()
        }
        return tarjeta

    def diccionario_a_objeto(self, diccionario_tarjeta: dict):
        try:
            if "Numero de cuenta" in diccionario_tarjeta and diccionario_tarjeta["Numero de cuenta"]:
                self.set_numero_cuenta(diccionario_tarjeta["Numero de cuenta"])

            if "cvv" in diccionario_tarjeta and diccionario_tarjeta["cvv"]:
                self.set_cvv(diccionario_tarjeta["cvv"])

            if "Fecha de registro" in diccionario_tarjeta and diccionario_tarjeta["Fecha de registro"]:
                self.set_fecha_registro(diccionario_tarjeta["Fecha de registro"])

            if "Fecha de caducidad" in diccionario_tarjeta and diccionario_tarjeta["Fecha de caducidad"]:
                self.set_fecha_caducidad(diccionario_tarjeta["Fecha de caducidad"])

            if "Nombre del titular" in diccionario_tarjeta and diccionario_tarjeta["Nombre del titular"]:
                self.set_nombre_titular(diccionario_tarjeta["Nombre del titular"])

            if "Propietario" in diccionario_tarjeta and diccionario_tarjeta["Propietario"]:
                self.set_propietario(diccionario_tarjeta["Propietario"])

        except Exception as error:
            raise ValueError(f"Valor erróneo en lo que se haya introducido {error}")

    def objeto_a_csv(self):
        pass

    def objeto_a_texto(self):
        pass

    def csv_a_objeto(self):
        pass

    def texto_a_objeto(self, texto : str):
        pass