from .usuario import Usuario
from .usuario import Fecha

class TarjetaCredito:
    def __init__(self, numero_de_cuenta : int,
                 CVV : int,
                 fecha_de_caducidad : Fecha,
                 nombre_completo_titular : str,
                 propietario : UsuarioPremium = None ):

        assert (len(str(numero_de_cuenta)) == 16 and
                len(str(CVV)) == 3), "Los datos introducidos no son válidos"

        self._numero_de_cuenta = numero_de_cuenta
        self._CVV = CVV
        self._fecha_de_caducidad = fecha_de_caducidad
        self.nombre_completo_titular = nombre_completo_titular
        self._propietario = propietario

    def get_numero_cuenta (self):
        return self._numero_de_cuenta

    def get_CVV (self):
        return self._CVV

    def get_fecha_caducidad (self):
        return self._fecha_caducidad

    def get_nombre_titular (self):
        return self._nombre_completo_titular


class UsuarioPremium(Usuario):
    def __init__(self, nombre_usuario : str,
                 fecha_nacimiento : Fecha,
                 correo_electronico : str,
                 contrasenya : str,
                 fecha_registro : Fecha,
                 tarjeta_credito : TarjetaCredito
    ):
        super.__init__(nombre_usuario = nombre_usuario,
                       fecha_nacimiento = fecha_nacimiento,
                       correo_electronico = correo_electronico,
                       