import json
import csv
from abc import ABC, abstractmethod

class ErrorGravePersistencia(Exception):
    def __init__(self, mensaje = "No se ha podido cargar la base de datos."):
        super().__init__(mensaje)

class GestorPersistencia:
    # ===== MÉTODOS CARGAR: Cargan el contenido directamente en un objeto =======
    # === MÉTODOS LEER: Devuelven el contenido como información sin procesar ====


    # =============================== MÉTODOS PARA JSON =================================================
    @staticmethod
    def guardar_json(contenido: dict, ruta: str) -> bool:
        """Dada la ruta de un archivo .json, guarda el contenido que recibe por parámetros en esa ruta."""
        try:
            with open(ruta, "w") as f:
                json.dump(contenido, f)

        except Exception as e:
            print(f"No se ha podido guardar en el JSON: {ruta}, error {e}")
            raise ErrorGravePersistencia
        return True

    @staticmethod
    def leer_json(ruta: str) -> dict:
        with open(ruta, "r") as f:
            contenido = json.load(f)
        return contenido

    def cargar_json(self, ruta: str, objeto: object) -> bool:
        """Dada la ruta de un archivo .json, y un objeto objeto que debe heredar de IPersistencia, carga su contenido
        en el archivo .txt. Devuelve True si ha conseguido cargar el contenido satisfactoriamente y false si no puede.
        """
        try:
            contenido = self.leer_json(ruta)
        except Exception as e:
            print(f"No se ha podido cargar el JSON: {ruta}, error {e}")
            return False
        else:
            objeto.diccionario_a_objeto(contenido)
            return True

    # =============================== MÉTODOS PARA CSV =================================================
    @staticmethod
    def guardar_csv(contenido: dict, ruta: str) -> bool:
        """Dada la ruta de un archivo .csv, guarda el contenido que recibe por parámetros en esa ruta.
        Para que el método funcione, el contenido debe ser un diccionario de la forma:
            {'nombre de la cabecera': 'valor de la cabecera',}
        """
        try:
            with open(ruta, "a", newline="") as f:
                escritor = csv.DictWriter(f, fieldnames=contenido.keys())
                escritor.writerow(contenido)
        except Exception as e:
            print(f"No se ha podido escribir en el CSV: {ruta}, error {e}")
            raise ErrorGravePersistencia
        return True

    @staticmethod
    def escribir_keys_csv(contenido: dict, ruta: str) -> bool:
        try:
            with open(ruta, "w", newline="") as f:
                escritor = csv.writer(f)
                escritor.writerow(contenido.keys())  # todas en una sola fila
        except Exception as e:
            print(f"No se ha podido escribir en el CSV las cabeceras: {ruta}, error {e}")
            raise ErrorGravePersistencia
        return True

    @staticmethod
    def resetear_csv_manteniendo_cabeceras(ruta: str) -> bool:
        try:
            with open(ruta, "r", newline="") as f:
                reader = csv.reader(f)
                cabecera = next(reader)
            with open(ruta, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(cabecera)
        except Exception as e:
            print("No se ha podido resetear el csv, error {e}")
            raise ErrorGravePersistencia
        return True

    @staticmethod
    def leer_csv(ruta: str) -> list[dict]:
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            # Convierto el iterador "lector" en una lista de diccionarios de la forma {'cabecera': 'valor'}
            contenido = list(
                lector
            )  # [{"cabecera 1: "valor fila 1", "cabecera 2": "valor cabecera 2"}, {}, {},{}]
        return contenido

    def cargar_csv(self, ruta: str, objeto: object) -> bool:
        """Dada la ruta de un archivo .csv, y un objeto objeto que debe heredar de IPersistencia, carga su contenido
        en el archivo .txt. Devuelve True si ha conseguido cargar el contenido satisfactoriamente y false si no puede.
        """
        try:
            contenido = self.leer_csv(ruta)
        except Exception as e:
            print(f"No se ha podido cargar el CSV: {ruta}, error {e}")
            return False
        else:
            objeto.csv_a_objeto(contenido)
            return True

class IPersistencia(ABC):

    @abstractmethod
    def objeto_a_diccionario(self) -> dict:
        """Dado un objeto (aquel que implementa la Interfaz de Persistencia), este método ha de sintetizar los atributos
        del objeto y devolver un diccionario de la forma {'nombre del atributo' : 'valor del atributo'}
        """
        pass

    @abstractmethod
    def objeto_a_csv(self) -> dict:
        """Dado un objeto (aquel que implementa la Interfaz de Persistencia), este método ha de sintetizar los atributos
        del objeto y devolver un diccionario de la forma {'cabecera' : ' valor del atributo asociado a esa cabecera'}
        """
        pass

    @abstractmethod
    def diccionario_a_objeto(self, diccionario: dict) -> None:
        """Dado un diccionario, el objeto que implemente este método debe extraer del diccionario los valores necesarios
        para establecerlos en su propia instancia."""
        pass

    @abstractmethod
    def csv_a_objeto(self) -> None:
        """Dado un csv (que realmente no será más que un diccionario de la forma {'cabecera': 'valor de la cabecera'})
        este método debe extraer del diccionario los valores necesarios para establecerlos en su propia instancia
        """
        pass