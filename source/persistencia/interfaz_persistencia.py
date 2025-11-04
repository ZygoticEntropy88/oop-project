from abc import ABC, abstractmethod

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