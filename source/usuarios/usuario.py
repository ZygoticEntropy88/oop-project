from source.persistencia import IPersistencia

class Fecha:
    def __init__(self, dia : int, mes : int, anyo : int):
        assert (0 < dia <= 31
                and 0 < mes <= 12
                and 0 < anyo <= 2025), "La fecha introducida no es válida"

        self._dia = dia
        self._mes = mes
        self._anyo = anyo

    def get_dia(self):
        return self._dia

    def get_mes(self):
        return self._mes

    def get_anyo(self):
        return self._anyo

    def fecha_to_list(self) -> list[int]:
        fecha : list[int] = [self.get_dia(),
                             self.get_mes(),
                             self.get_anyo()]
        return fecha


class Usuario(IPersistencia):
    def __init__(self, nombre_de_usuario : str,
                 fecha_nacimiento : Fecha,
                 correo_electronico : str,
                 contrasenya : str,
                 fecha_registro : Fecha):

        self._nombre_de_usuario = nombre_de_usuario
        self._fecha_de_nacimiento = fecha_nacimiento
        self._correo_electronico = correo_electronico
        self._contrasenya = contrasenya
        self.fecha_de_registro = fecha_registro