import json
import csv

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

    @staticmethod
    def cargar_json(self, ruta:str, objeto:object) -> bool:
        """Dada la ruta de un archivo .json, y un objeto objeto que debe heredar de IPersistencia, carga su contenido
        en el archivo .txt. Devuelve True si ha conseguido cargar el contenido satisfactoriamente y false si no puede."""
        try:
            with open(ruta, "r") as f:
                contenido = json.load(f)
        except Exception as e:
            print(f"No se ha podido cargar el JSON: {ruta}, error {e}")
            return False
        else:
            objeto.diccionario_a_objeto(contenido)
            return True

    @staticmethod
    def cargar_csv(self, ruta:str, objeto:object) -> bool:
        """Dada la ruta de un archivo .csv, y un objeto objeto que debe heredar de IPersistencia, carga su contenido
        en el archivo .txt. Devuelve True si ha conseguido cargar el contenido satisfactoriamente y false si no puede."""
        try:
            with open(ruta, newline='', encoding='utf-8') as f:
                lector = csv.DictReader(f)
                # Convierto el iterador "lector" en una lista de diccionarios de la forma {'cabecera': 'valor'}
                contenido = list(lector)
        except Exception as e:
            print(f"No se ha podido cargar el CSV: {ruta}, error {e}")
            return False
        else:
            objeto.csv_a_objeto(contenido)
            return True

    @staticmethod
    def cargar_txt(self, ruta:str, objeto:object) -> bool:
        """Dada la ruta de un archivo .txt, y un objeto objeto que debe heredar de IPersistencia, carga su contenido
        en el archivo .txt. Devuelve True si ha conseguido cargar el contenido satisfactoriamente y false si no puede."""
        try:
            with open(ruta) as f:
                contenido = f.read()
        except Exception as e:
            print(f"No se ha cargado el texto en el TXT: {ruta}")
            return False
        else:
            objeto.texto_a_objeto(contenido)
            return True