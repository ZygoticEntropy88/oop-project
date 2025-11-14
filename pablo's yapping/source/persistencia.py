import json
import csv
from abc import ABC, abstractmethod
import os



class GestorPersistencia:


    @staticmethod
    def guardar_json(self, contenido:dict, ruta:str) -> bool:
        """Dada la ruta de un archivo .json, guarda el contenido que recibe por parámetros en esa ruta."""
        try:
            with open(ruta, "w") as f:
                json.dump(contenido, f)

        except Exception as e:
            print(f"No se ha podido guardar en el JSON: {ruta}, error {e}")
            return False
        return True

    @staticmethod
    def guardar_csv(self, contenido:dict, ruta:str) -> bool:
        """Dada la ruta de un archivo .csv, guarda el contenido que recibe por parámetros en esa ruta.
        Para que el método funcione, el contenido debe ser un diccionario de la forma:
            {'nombre de la cabecera': 'valor de la cabecera',}
        """
        try:
            with open(ruta, "w") as f:
                cabecera = contenido.keys()
                escritor = csv.DictWriter(f, fieldnames=cabecera)
                # Si la cabecera fuera diferente, la machacaría
                escritor.writeheader()
                escritor.writerow(contenido)

        except Exception as e:
            print(f"No se ha podido escribir en el CSV: {ruta}, error {e}")
            return False
        return True

    @staticmethod
    def guardar_txt(self, contenido:str, ruta:str) -> bool:
        """Dada la ruta de un archivo .txt, guarda el contenido que recibe por parámetros en esa ruta."""
        try:
            with  open(ruta), "w" as f:
                f.write(contenido)
        except Exception as e:
            print(f"No se ha podido guardar en el TXT: {ruta}, error {e}")
            return False
        return True

    # ===== MÉTODOS CARGAR: Cargan el contenido directamente en un objeto =======
    # === MÉTODOS LEER: Devuelven el contenido como información sin procesar ====

    @staticmethod
    def leer_json(ruta: str) -> dict:
        with open(ruta, "r") as f:
            contenido = json.load(f)
        return contenido

    def cargar_json(self, ruta:str, objeto:object) -> bool:
        """Dada la ruta de un archivo .json, y un objeto objeto que debe heredar de IPersistencia, carga su contenido
        en el archivo .txt. Devuelve True si ha conseguido cargar el contenido satisfactoriamente y false si no puede."""
        try:
            contenido = self.leer_json(ruta)
        except Exception as e:
            print(f"No se ha podido cargar el JSON: {ruta}, error {e}")
            return False
        else:
            objeto.diccionario_a_objeto(contenido)
            return True

    @staticmethod
    def leer_csv(ruta:str) -> list[dict]:
        with open(ruta, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            # Convierto el iterador "lector" en una lista de diccionarios de la forma {'cabecera': 'valor'}
            contenido = list(lector) # [{"cabecera 1: "valor fila 1", "cabecera 2": "valor cabecera 2"}, {}, {},{}]
        return contenido

    def cargar_csv(self, ruta:str, objeto:object) -> bool:
        """Dada la ruta de un archivo .csv, y un objeto objeto que debe heredar de IPersistencia, carga su contenido
        en el archivo .txt. Devuelve True si ha conseguido cargar el contenido satisfactoriamente y false si no puede."""
        try:
            contenido = self.leer_csv(ruta)
        except Exception as e:
            print(f"No se ha podido cargar el CSV: {ruta}, error {e}")
            return False
        else:
            objeto.csv_a_objeto(contenido)
            return True

    @staticmethod
    def leer_txt(ruta: str) -> str:
        with open(ruta) as f:
            contenido = f.read()
        return contenido

    def cargar_txt(self, ruta:str, objeto:object) -> bool:
        """Dada la ruta de un archivo .txt, y un objeto objeto que debe heredar de IPersistencia, carga su contenido
        en el archivo .txt. Devuelve True si ha conseguido cargar el contenido satisfactoriamente y false si no puede."""
        try:
            contenido = self.leer_txt(ruta)
        except Exception as e:
            print(f"No se ha cargado el texto en el TXT: {ruta}")
            return False
        else:
            objeto.texto_a_objeto(contenido)
            return True





class IPersistencia(ABC):

    @abstractmethod
    def objeto_a_texto(self) -> str:
        """Dado un objeto (aquel que implementa la Interfaz de Persistencia), este método ha de sintetizar los atributos
        del objeto en una cadena de texto."""
        pass

    @abstractmethod
    def objeto_a_diccionario(self) -> dict:
        """Dado un objeto (aquel que implementa la Interfaz de Persistencia), este método ha de sintetizar los atributos
        del objeto y devolver un diccionario de la forma {'nombre del atributo' : 'valor del atributo'}"""
        pass

    @abstractmethod
    def objeto_a_csv(self) -> dict:
        """Dado un objeto (aquel que implementa la Interfaz de Persistencia), este método ha de sintetizar los atributos
        del objeto y devolver un diccionario de la forma {'cabecera' : ' valor del atributo asociado a esa cabecera'}"""
        pass

    @abstractmethod
    def texto_a_objeto(self, texto:str) -> None:
        """Dado un texto, el objeto que implemente este método debe extraer del texto los valores necesarios para
        establecerlos en su propia instancia."""
        pass

    @abstractmethod
    def diccionario_a_objeto(self, diccionario:dict) -> None:
        """Dado un diccionario, el objeto que implemente este método debe extraer del diccionario los valores necesarios
        para establecerlos en su propia instancia. """
        pass

    @abstractmethod
    def csv_a_objeto(self) -> None:
        """Dado un csv (que realmente no será más que un diccionario de la forma {'cabecera': 'valor de la cabecera'})
        este método debe extraer del diccionario los valores necesarios para establecerlos en su propia instancia"""
        pass

class Memoria:
    def __init__(self, ruta="db/"):

        self.__gp = GestorPersistencia()

        self._usuarios = self.__gp.leer_csv(f"{ruta}usuarios.csv")

        self._catalogo_generico = self.__gp.leer_csv(f"{ruta}catalogo_generico.csv")
        
        self._listas_reproduccion = {}
        for directorio_usuario in os.listdir(f"{ruta}listas_reproduccion/"):
            self._listas_reproduccion[directorio_usuario] = []
            for nombre_archivo in os.listdir(f"{ruta}listas_reproduccion/{directorio_usuario}"):
                if "." in nombre_archivo:  
                    lista = self.__gp.leer_csv(f"{ruta}listas_reproduccion/{directorio_usuario}/{nombre_archivo}")
                    self._listas_reproduccion[directorio_usuario].append(lista)

        self._catalogos_personales = {}
        for nombre_archivo in os.listdir(f"{ruta}catalogos_personales/"):
            if "." in nombre_archivo:  
                catalogo = self.__gp.leer_csv(f"{ruta}catalogos_personales/{nombre_archivo}")
                self._catalogos_personales[nombre_archivo].append(catalogo)

    def __str__(self):
        msg = "===================================MEMORIA=========================================\n"
        msg += f"\t ·USUARIOS: {self._usuarios}\n\n"

        msg += f"\t ·CATÁLOGO GENÉRICO = [\n"
        for cancion_info in self._catalogo_generico:
            msg += f"\t\t{cancion_info}\n"
        msg += "\t  ]\n"


        msg += f"\t ·LISTAS REPRODUCCIÓN =  \n"
        for usuario, listas_usuario in self._listas_reproduccion.values():
            msg += "\tt {usuario} : {listas_usuario}"

        msg += f"\t ·CATÁLOGOS PERSONALES: {self._catalogos_personales}\n\n"
        return msg

    def guardar_en_disco():
        """Este método se ejecuta antes de salir de la aplicación, y guarda toda la memoria en el disco duro"""
        print(f"GUARDANDO LA INFORMACIÓN {self._usuarios}")
        self.__gp.guardar_csv(self._usuarios, f"{ruta}usuarios.csv")

    def anyadir_usuario(self, usuario:'Usuario'):
        self.__gp.guardar_csv(usuario.objeto_a_diccionario())