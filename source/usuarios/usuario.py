from persistencia.interfaz_persistencia import IPersistencia
import csv
from listas import Lista
from listas import Catalogo
from canciones import Cancion
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
                 fecha_registro : Fecha,
                 catalogo_generico : 'Catalogo' ):

        self._nombre_de_usuario = nombre_de_usuario
        self._fecha_de_nacimiento = fecha_nacimiento
        self._correo_electronico = correo_electronico
        self._contrasenya = contrasenya
        self._fecha_de_registro = fecha_registro
        self._catalogo_generico = catalogo_generico

    def get_nombre_usuario (self):
        return self._nombre_de_usuario

    def get_fecha_nacimiento(self):
        return self._fecha_de_nacimiento

    def get_correo_electronico (self):
        return self._correo_electronico

    def get_contrasenya (self):
        return self._contrasenya

    def get_fecha_registro (self):
        return self._fecha_de_registro

    def get_catalogo_generico(self):
        return self._catalogo_generico

    def set_nombre_usuario (self, nuevo_nombre : str):
        self._nombre_de_usuario = nuevo_nombre

    def set_fecha_nacimiento(self, nueva_fecha : Fecha):
        self._fecha_de_nacimiento = nueva_fecha

    def set_correo_electronico (self, nuevo_correo : str):
        self._correo_electronico = nuevo_correo

    def set_contrasenya (self, nueva_contrasenya : str):
        self._contrasenya = nueva_contrasenya

    def set_fecha_registro (self, nueva_fecha_registro : Fecha):
        self._fecha_de_registro = nueva_fecha_registro

    def set_catalogo_generico(self, nuevo_catalogo_generico : 'Catalogo'):
        self._catalogo_generico = nuevo_catalogo_generico

    def crear_lista_reproduccion(self, lista_canciones : list['Cancion']): #Tengo que permitir que un usuario dado cree una lista de reproduccion
        nombre_lista: str = str(input("Ingrese el nombre de la lista"))
        descripcion_lista: str = str(input("Añade una descripción a la lista"))
        fecha_creacion :'Fecha' = Fecha(10, 11, 2025)
        nueva_lista: 'Lista' = Lista(nombre_lista, descripcion_lista, lista_canciones, fecha_creacion, self)
        return nueva_lista

    def objeto_a_texto (self):
        usuario_texto : str = ""
        usuario_texto += f"Nombre:  {self.get_nombre_usuario()} \n"
        usuario_texto += f"Fecha Nacimiento:  {self.get_fecha_nacimiento()} \n"
        usuario_texto += f"Correo Electrónico:  {self.get_correo_electronico()} \n"
        usuario_texto += f"Contraseña:  {self.get_contrasenya()} \n"
        usuario_texto += f"Fecha Registro:  {self.get_fecha_registro()} \n"
        return usuario_texto

    def objeto_a_diccionario (self):
        usuario = {
            "Nombre" : self.get_nombre_usuario(),
            "Fecha Nacimiento" : self.get_fecha_nacimiento(),
            "Correo Electrónico" : self.get_correo_electronico(),
            "Contraseña" : self.get_contrasenya(),
            "Fecha Registro" : self.get_fecha_registro()
        }
        return usuario

    def objeto_a_csv(self):
        pass

    def texto_a_objeto (self, texto : str):
        pass

    def diccionario_a_objeto (self, diccionario_usuario : dict):
        try:
            if "Nombre" in diccionario_usuario and diccionario_usuario["Nombre"]:
                self.set_nombre_usuario(diccionario_usuario["Nombre"])

            if "Fecha de Nacimiento" in diccionario_usuario and diccionario_usuario["Fecha de Nacimiento"]:
                self.set_fecha_nacimiento(diccionario_usuario["Fecha de Nacimiento"])

            if "Correo Electrónico" in diccionario_usuario and diccionario_usuario["Correo Electrónico"]:
                self.set_correo_electronico(diccionario_usuario["Correo Electrónico"])

            if "Contraseña" in diccionario_usuario and diccionario_usuario["Contraseña"]:
                self.set_contrasenya(diccionario_usuario["Contraseña"])

            if "Fecha Registro" in diccionario_usuario and diccionario_usuario["Fecha Registro"]:
                self.set_fecha_registro(diccionario_usuario["Fecha Registro"])

        except Exception as error:
            raise ValueError(f"Valor erróneo en lo que se haya introducido {error}")

    def csv_a_objeto (self):
        pass