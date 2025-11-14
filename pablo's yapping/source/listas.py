from persistencia import IPersistencia
from canciones import Cancion
from fecha import Fecha
#from usuarios import Usuario

class Lista(IPersistencia):

    def __init__(self, nombre : str, descripcion : str,
                 lista_canciones : list['Cancion'],
                 fecha_creacion : Fecha,
                 usuario_creador : 'Usuario'):
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
        diccionario_listas : dict = {
            "Nombre lista" : self.get_nombre(),
            "Descripción" : self.get_descripcion(),
            "Lista de canciones" : self.get_lista_canciones(),
            "Fecha de creación" : self.get_fecha_creacion(),
            "Usuario creador" : self.get_usuario_creador()
        }
        return diccionario_listas

    def diccionario_a_objeto(self, diccionario_listas : dict):
        try:
            if "Descripción" in diccionario_listas and diccionario_listas["Descripción"]:
                self.set_descripcion(diccionario_listas["Descripción"])

            if "Nombre lista" in diccionario_listas and diccionario_listas["Nombre lista"]:
                self.set_nombre(diccionario_listas["Nombre lista"])

            if "Lista de canciones" in diccionario_listas and diccionario_listas["Lista de canciones"]:
                self.set_lista_canciones(diccionario_listas["Lista de canciones"])

            if "Fecha de creación" in diccionario_listas and diccionario_listas["Fecha de creación"]:
                self.set_fecha_creacion(diccionario_listas["Fecha de creación"])

            if "Usuario creador" in diccionario_listas and diccionario_listas["Usuario creador"]:
                self.set_usuario_creador(diccionario_listas["Usuario creador"])

        except Exception as error:
            raise ValueError(f"Valor erróneo en lo que se haya introducido {error}")

class Catalogo(IPersistencia): #Tenemos que guardar los catálogos

    def __init__(self, lista_canciones : list['Cancion']):
        self._lista_canciones = lista_canciones

    def get_lista_canciones(self):
        return self._lista_canciones

    def set_lista_canciones(self, nueva_lista : list['Cancion']):
        self._lista_canciones = nueva_lista

    def filtrar_catalogo(self, artista : str = None, genero : str = None):
        catalogo_filtrado : list['Cancion'] = []

        if artista is not None and genero is not None:
            for cancion in self.get_lista_canciones():
                if cancion.get_artista() == artista and cancion.get_genero() == genero:
                    catalogo_filtrado.append(cancion)

            self.set_lista_canciones(catalogo_filtrado)

        elif artista is not None and genero is None:
            for cancion in self.get_lista_canciones():
                if cancion.get_artista() == artista:
                    catalogo_filtrado.append(cancion)

            self.set_lista_canciones(catalogo_filtrado)

        elif genero is not None and artista is None:
            for cancion in self.get_lista_canciones():
                if cancion.get_genero() == genero:
                    catalogo_filtrado.append(cancion)

            self.set_lista_canciones(catalogo_filtrado)

        else:
            raise ValueError("Los valores introducidos no son válidos")

    def __str__(self):
        self.get_lista_canciones().__str__()

    def objeto_a_csv(self):
        pass

    def csv_a_objeto(self):
        pass

    def texto_a_objeto(self, diccionario_texto : str):
        pass

    def objeto_a_texto(self):
        pass


    def objeto_a_diccionario(self):
        diccionario_catalogo : dict = {}

        for cancion in self.get_lista_canciones():
            diccionario_catalogo.update(cancion.objeto_a_diccionario())

        return diccionario_catalogo


    def diccionario_a_objeto(self, diccionario_catalogo : dict):
        nueva_lista_canciones : list['Cancion'] = []
        for datos_cancion in diccionario_catalogo.items():
            cancion : Cancion = cancion.diccionario_a_objeto(datos_cancion)
            nueva_lista_canciones.append(cancion)

        self.set_lista_canciones(nueva_lista_canciones)

class CatalogoPersonal (Catalogo):
    def __init__(self, lista_canciones : list['Cancion']):
        super().__init__(lista_canciones)

    def anyadir_cancion_a_catalogo(self, cancion : 'Cancion'):
        assert cancion, "Los datos introducidos no son válidos"
        self.get_lista_canciones().append(cancion)