from persistencia import IPersistencia
from canciones import Cancion
from usuarios.usuario import Fecha
from usuarios.usuario import Usuario


class Lista(IPersistencia):

    def __init__(self, nombre : str, descripcion : str,
                 lista_canciones : list['Cancion'],
                 fecha_creacion : Fecha,
                 usuario_creador : Usuario):
        self._nombre = nombre
        self._descripcion = descripcion
        self._lista_canciones = lista_canciones
        self._fecha_creacion = fecha_creacion
        self._usuario_creador = usuario_creador

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def get_lista_canciones(self):
        return self._lista_canciones

    def get_fecha_creacion(self):
        return self.fecha_creacion

    def get_usuario_creador(self):
        return self._usuario_creador

    def __str__(self):
        lista_a_str : str = ""
        lista_a_str += f"{self.get_nombre()} \n"
        lista_a_str += f"{self.get_descripcion()} \n"
        for cancion in self.get_lista_canciones():
            lista_a_str += cancion.__str__()
        lista_a_str += self.get_usuario_creador().get_nombre_usuario()
        print(lista_a_str)

    def mostar_canciones(self):
        pass





class Catalogo(Lista):
    pass