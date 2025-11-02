from menu import Menu

class MenuReproduccion(Menu):
    id = 2
    opciones = [
        "Reproducir canción por ID",
        "Pausar reproducción de la canción",
        "Renaudar reproducción"
    ]

    @classmethod
    def ejecutar(cls, opcion:int):
        pass

    @classmethod
    def reproducir_por_id(cls):
        pass

    @classmethod
    def pausar_cancion(cls):
        pass

    @classmethod
    def renaudar_cancion(cls):
        pass