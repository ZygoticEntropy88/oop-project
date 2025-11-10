from .usuario import Usuario
from usuario import Fecha
from listas import Lista
from canciones import Cancion

class UsuarioRegular(Usuario):

    def crear_lista_reproduccion(self, lista_canciones : list['Cancion']): #Tengo que permitir que un usuario dado cree una lista de reproduccion
        nombre_lista: str = str(input("Ingrese el nombre de la lista"))
        descripcion_lista: str = str(input("Añade una descripción a la lista"))
        fecha_creacion :'Fecha' = Fecha(10, 11, 2025)
        nueva_lista: 'Lista' = Lista(nombre_lista, descripcion_lista, lista_canciones, fecha_creacion, self)
        return nueva_lista

    pass