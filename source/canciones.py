from persistencia import IPersistencia

class Cancion(IPersistencia):

    def __init__(self, id_cancion : str, nombre : str, genero : str,
                 artista : str, anyo : int):

        assert 0 <= anyo <= 2025, "El año introducido no es válido"
        self._identificador = id_cancion
        self._genero = genero
        self._nombre = nombre
        self._artista = artista
        self._anyo = anyo

    def get_identificador (self):
        return self._identificador

    def get_nombre(self):
        return self._nombre

    def get_artista (self):
        return self._artista

    def get_anyo (self):
        return self._anyo

    def get_genero(self):
        return self._genero

    def set_identificador (self, nuevo_identificador : str):
        self._identificador = nuevo_identificador

    def set_nombre (self, nuevo_nombre : str):
        self._nombre = nuevo_nombre

    def set_artista (self, nuevo_artista : str):
        self._artista = nuevo_artista

    def set_genero (self, nuevo_genero : str):
        self._genero = nuevo_genero

    def set_anyo (self, nuevo_anyo : int):
        self._anyo = nuevo_anyo

    def __str__(self):
        cancion_a_str : str = ""
        cancion_a_str += f"Nombre: {self.get_nombre()} \n"
        cancion_a_str += f"Artista: {self.get_artista()} \n"
        cancion_a_str += f"Año: {self.get_anyo()} \n"
        cancion_a_str += f"Género: {self.get_genero()} \n"
        cancion_a_str += f"Identificador: {self.get_identificador()}"
        return cancion_a_str

    def objeto_a_diccionario (self):
        cancion : dict = {
            "Identificador cancion" : self.get_identificador(),
            "Nombre" : self.get_nombre(),
            "Artista" : self.get_artista(),
            "Género" : self.get_genero(),
            "Anyo" : self.get_anyo()
        }
        return cancion

    def diccionario_a_objeto(self, diccionario_cancion : dict):
        try:
            if "Identificador cancion" in diccionario_cancion and diccionario_cancion["Identificador cancion"]:
                self.set_identificador(diccionario_cancion["Identificador cancion"])

            if "Nombre" in diccionario_cancion and diccionario_cancion["Nombre"]:
                self.set_nombre(diccionario_cancion["Nombre"])

            if "Artista" in diccionario_cancion and diccionario_cancion["Artista"]:
                self.set_artista(diccionario_cancion["Artista"])

            if "Género" in diccionario_cancion and diccionario_cancion["Género"]:
                self.set_genero(diccionario_cancion["Género"])

            if "Anyo" in diccionario_cancion and diccionario_cancion["Anyo"]:
                self.set_anyo(diccionario_cancion["Anyo"])

        except Exception as error:
            raise ValueError(f"Valor erróneo en lo que se haya introducido {error}")

    def texto_a_objeto (self, texto : str):
        pass

    def objeto_a_texto (self):
        pass

    def objeto_a_csv (self):
        pass

    def csv_a_objeto(self):
        pass

