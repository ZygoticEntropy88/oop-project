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
        self.lista_canciones = lista_canciones
        self._fecha_creacion = fecha_creacion
        self._usuario_creador = usuario_creador

    
class Catalogo(Lista):
    pass