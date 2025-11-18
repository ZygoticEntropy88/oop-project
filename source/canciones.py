from persistencia import IPersistencia

class Cancion(IPersistencia):

    def __init__(self,
                id_cancion : str = None,
                nombre : str = None,
                genero : str = None,
                artista : str = None,
                anyo : int = 2025):

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
        cancion_a_str : str = "CANCIÓN | "
        cancion_a_str += f"Nombre: {self.get_nombre()} ; "
        cancion_a_str += f"Artista: {self.get_artista()} ;"
        cancion_a_str += f"Año: {self.get_anyo()} ;"
        cancion_a_str += f"Genero: {self.get_genero()} ;"
        cancion_a_str += f"Identificador: {self.get_identificador()}\n"
        return cancion_a_str

    def solicitar_usuario_por_consola(self, motivo_consulta="", eliminar = False):
        cancion_id:str = input(f"Introduzca el ID de youtube de la canción {motivo_consulta}: ")
        self.set_identificador(cancion_id)

        if not eliminar:
            if input("Le gustaría guardar más datos de la canción? (s/n)").lower().strip() == 's':
                cancion_nombre = input("Introduzca el título de la canción (Presione enter para dejar en blanco): ")
                if cancion_nombre != "":
                    self.set_nombre(cancion_nombre)
                cancion_artista = input("Introduzca el artista de la canción (Presione enter para dejar en blanco): ")
                if cancion_artista != "":
                    self.set_artista(cancion_artista)
                cancion_genero = input("Introduzca el género de la canción (Presione enter para dejar en blanco): ")
                if cancion_genero != "":
                    self.set_genero(cancion_genero)
                cancion_anyo = input("Introduzca el año de la canción (Presione enter para dejar en blanco)")
                if cancion_anyo != "":
                    self.set_anyo(cancion_anyo)


    def objeto_a_diccionario (self):
        cancion : dict = {
            "Nombre" : self.get_nombre(),
            "Artista" : self.get_artista(),
            "Genero" : self.get_genero(),
            "Anyo" : self.get_anyo(),
            "Identificador cancion" : self.get_identificador(),
        }
        return cancion


    def diccionario_a_objeto(self, diccionario_cancion : dict):
        try:

            if "Nombre" in diccionario_cancion and diccionario_cancion["Nombre"]:
                self.set_nombre(diccionario_cancion["Nombre"])

            if "Artista" in diccionario_cancion and diccionario_cancion["Artista"]:
                self.set_artista(diccionario_cancion["Artista"])

            if "Genero" in diccionario_cancion and diccionario_cancion["Genero"]:
                self.set_genero(diccionario_cancion["Genero"])

            if "Anyo" in diccionario_cancion and diccionario_cancion["Anyo"]:
                self.set_anyo(int(diccionario_cancion["Anyo"]))

            if "Identificador cancion" in diccionario_cancion and diccionario_cancion["Identificador cancion"]:
                self.set_identificador(diccionario_cancion["Identificador cancion"])

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