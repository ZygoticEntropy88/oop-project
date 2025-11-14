from enum import Enum 

class Meses(Enum):
    ENERO = 1
    FEBRERO = 2
    MARZO = 3
    ABRIL = 4
    MAYO = 5
    JUNIO = 6
    JULIO = 7
    AGOSTO = 8
    SEPTIEMBRE = 9
    OCTUBRE = 10
    NOVIEMBRE = 11
    DICIEMBRE = 12

class FechaNoValida(Exception):
    def __init__(self, mensaje=None):
        super().__init__(mensaje)

class FormatoFechaNoValido(Exception): 
    pass

class Fecha:
    def __init__(self, dia:int = 1, mes:Meses = Meses(1), anyo:int = 2025):
        self._dia:int = dia
        self._mes:Meses = mes
        self._anyo:int = anyo

    def __str__(self):
        return f"Fecha: {self._dia} de {self._mes.name} del año {self._anyo}"

    def get_dia(self):
        return self._dia

    def get_mes(self):
        return self._mes

    def get_anyo(self):
        return self._anyo

    def set_dia(self, dia:int):
        if 1 <= dia <= 31:
            self._dia = dia
        else:
            raise FechaNoValida("El día debe estar entre 1 y 31")

    def set_mes(self, mes:int):
        if 1 <= mes <= 12:
            self._mes = Meses(mes)
        else:
            raise FechaNoValida("El número del mes debe estar entre 1 y 12")

    def set_anyo(self, anyo:int):
        if 1900 <= anyo <= 2026:
            self._anyo = anyo
        else:
            raise FechaNoValida("El año debe estar entre 1900 y 2026")

    def solicitar_usuario(self, motivo_consulta:str = None):
        fecha_introducida = input(f"Introduzca la fecha {f"({motivo_consulta}" if motivo_consulta else ""}: dd/mm/aaaa: ")

        try:
            # Tratamiento de los datos (casting)
            dia_introducido:int = int(fecha_introducida[:1]) if fecha_introducida[0] != '0' else int(fecha_introducida[1])
            mes_introducido:int = int(fecha_introducida[3:4]) if fecha_introducida[3] != '0' else int(fecha_introducida[4])
            anyo_introducido:int = int(fecha_introducida[6:])

        except Exception as e:
            raise FormatoFechaNoValido

        self.set_dia(dia_introducido)
        self.set_mes(mes_introducido)
        self.set_anyo(anyo_introducido)

if __name__ == "__main__":
    # Pequeña prueba para ver que la clase funciona correctamente, ejecutar como "python fecha.py"
    fecha = Fecha()
    fecha.solicitar_usuario()
    print(fecha)