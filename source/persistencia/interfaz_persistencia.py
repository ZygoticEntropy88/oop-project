from abc import ABC, abstractmethod

class IPersistencia(ABC):

    @abstractmethod
    def objeto_a_texto(self) -> str:
        pass

    @abstractmethod
    def objeto_a_diccionario(self) -> dict:
        pass

    @abstractmethod
    def objeto_a_csv(self) -> dict:
        pass

    @abstractmethod
    def texto_a_objeto(self) -> None:
        pass

    @abstractmethod
    def diccionario_a_objeto(self) -> None:
        pass

    @abstractmethod
    def csv_a_objeto(self) -> None:
        pass