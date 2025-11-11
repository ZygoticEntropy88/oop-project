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
        return self._fecha_creacion

    def get_usuario_creador(self):
        return self._usuario_creador

    def set_nombre(self, nuevo_nombre : str):
        self._nombre = nuevo_nombre

    def set_descripcion(self, nueva_descripcion : str):
        self._descripcion = nueva_descripcion

    def set_lista_canciones(self, nueva_lista : list['Cancion']):
        self._lista_canciones = nueva_lista

    def set_fecha_creacion(self, nueva_fecha : 'Fecha'):
        self._fecha_creacion = nueva_fecha

    def set_usuario_creador(self, nuevo_usuario : 'Usuario'):
        self._usuario_creador = nuevo_usuario

    def __str__(self):
        lista_a_str : str = ""
        lista_a_str += f"{self.get_nombre()} \n"
        lista_a_str += f"{self.get_descripcion()} \n"
        for cancion in self.get_lista_canciones():
            lista_a_str += cancion.__str__()
        lista_a_str += self.get_usuario_creador().get_nombre_usuario()
        print(lista_a_str)

    def mostrar_canciones(self):
        for cancion in self.get_lista_canciones():
            print(cancion.__str__())

    def anyadir_cancion(self, cancion : 'Cancion'):

        self.get_lista_canciones().append(cancion)

    def eliminar_cancion (self, cancion : 'Cancion'):
        self.get_lista_canciones().remove(cancion)

    def objeto_a_csv(self):
        pass

    def csv_a_objeto(self):
        pass

    def texto_a_objeto(self, diccionario_texto : str):
        pass

    def objeto_a_texto(self):
        pass
    def objeto_a_diccionario(self):
        pass
    def diccionario_a_objeto(self, diccionario_listas : dict):
        pass





class Catalogo:

    def __init__(self, lista_canciones : list['Cancion']):
        self._lista_canciones = lista_canciones

    def get_lista_canciones(self):
        return self._lista_canciones

    def set_lista_canciones(self, nueva_lista : list['Cancion']):
        self._lista_canciones = nueva_lista

    def filtrar_lista(self, artista : str = None, genero : str = None):
        lista_filtrada : list['Cancion'] = []

        if artista is not None and genero is not None:
            for cancion in self.get_lista_canciones():
                if cancion.get_artista() == artista and cancion.get_genero() == genero:
                    lista_filtrada.append(cancion)

            self.set_lista_canciones(lista_filtrada)

        elif artista is not None and genero is None:
            for cancion in self.get_lista_canciones():
                if cancion.get_artista() == artista:
                    lista_filtrada.append(cancion)

            self.set_lista_canciones(lista_filtrada)

        elif genero is not None and artista is None:
            for cancion in self.get_lista_canciones():
                if cancion.get_genero() == genero:
                    lista_filtrada.append(cancion)

            self.set_lista_canciones(lista_filtrada)

        else:
            raise ValueError("Los valores introducidos no son válidos")

class CatalogoPersonal ('Catalogo'):
    def anyadir_cancion(self, ):