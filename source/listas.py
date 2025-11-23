from persistencia import IPersistencia
from canciones import Cancion
from fecha import Fecha

#from usuarios import Usuario


class Lista(IPersistencia):

    def __init__(
        self,
        nombre: str = None,
        descripcion: str = None,
        lista_canciones: list["Cancion"] = None,
        fecha_creacion: Fecha = None,
        usuario_creador: "Usuario" = None,
    ):
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

    def set_nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre

    def set_descripcion(self, nueva_descripcion: str):
        self._descripcion = nueva_descripcion

    def set_lista_canciones(self, nueva_lista: list["Cancion"]):
        self._lista_canciones = nueva_lista

    def set_fecha_creacion(self, nueva_fecha: "Fecha"):
        self._fecha_creacion = nueva_fecha

    def set_usuario_creador(self, nuevo_usuario: "Usuario"):
        self._usuario_creador = nuevo_usuario

    def __str__(self):
        lista_a_str: str = "LISTA | "
        lista_a_str += f"{self.get_nombre()} ; "
        lista_a_str += f"{self.get_descripcion()} ; "
        lista_a_str += f"{self.get_usuario_creador()} ; \n"

        if self.get_lista_canciones():
            for cancion in self.get_lista_canciones():
                lista_a_str += f"\t\t\t\t {cancion}\n"
        else:
            lista_a_str += "\t\t\t\tLista vacía\n"
        return lista_a_str

    def mostrar_canciones(self):
        for cancion in self.get_lista_canciones():
            print(cancion.__str__())

    def anyadir_cancion(self, cancion: "Cancion"):
        self.get_lista_canciones().append(cancion)

    def eliminar_cancion(self, id_cancion: "Cancion"):
        if self.comprobar_cancion_en_lista_por_id(id_cancion):
            posicion_cancion, cancion = self.cargar_cancion_por_id(id_cancion)
            self.get_lista_canciones().pop(posicion_cancion)
        else:
            print(f"No se puede eliminar la canción. La canción {id_cancion}  no está en la lista.")

    def comprobar_cancion_en_lista_por_id(self, id_cancion):
        encontrada = False
        posicion = 0
        while not encontrada and posicion < len(self.get_lista_canciones()):
            if self.get_lista_canciones()[posicion].get_identificador() == id_cancion:
                encontrada = True
            else:
                posicion += 1
        return encontrada

    def cargar_cancion_por_id(self, id_cancion):
        if self.comprobar_cancion_en_lista_por_id(id_cancion):
            encontrada = False
            posicion = 0
            while not encontrada and posicion < len(self.get_lista_canciones()):
                if self.get_lista_canciones()[posicion].get_identificador() == id_cancion:
                    encontrada = True
                else:
                    posicion += 1
            return posicion, self.get_lista_canciones()[posicion] 
        else:
            return posicion, None
    def objeto_a_csv(self):
        pass

    def csv_a_objeto(self):
        pass

    def objeto_a_diccionario(self):
        diccionario_listas: dict = {
            "Nombre lista": self.get_nombre(),
            "Descripcion": self.get_descripcion(),
            "Fecha creacion": self.get_fecha_creacion().objeto_a_diccionario(),
            "Usuario creador": self.get_usuario_creador(),
        }
        if self.get_lista_canciones():
            diccionario_listas["Lista canciones"] = [cancion.objeto_a_diccionario() for cancion in self.get_lista_canciones()]
        return diccionario_listas

    def diccionario_a_objeto(self, diccionario_listas: dict):
        try:
            if ("Nombre lista" in diccionario_listas and diccionario_listas["Nombre lista"]):
                self.set_nombre(diccionario_listas["Nombre lista"])

            if ("Descripcion" in diccionario_listas and diccionario_listas["Descripcion"]):
                self.set_descripcion(diccionario_listas["Descripcion"])

            if ("Lista canciones" in diccionario_listas and diccionario_listas["Lista canciones"]):
                lista_canciones: list[Cancion] = list()
                for cancion_info in diccionario_listas["Lista canciones"]:
                    cancion = Cancion()
                    cancion.diccionario_a_objeto(cancion_info)
                    lista_canciones.append(cancion)
                self.set_lista_canciones(lista_canciones)

            if ("Fecha creacion" in diccionario_listas and diccionario_listas["Fecha creacion"]):
                fecha_creacion = Fecha()
                fecha_creacion.diccionario_a_objeto(
                    diccionario_listas["Fecha creacion"]
                )
                self.set_fecha_creacion(fecha_creacion)

            if ("Usuario creador" in diccionario_listas and diccionario_listas["Usuario creador"]):
                self.set_usuario_creador(diccionario_listas["Usuario creador"])

        except Exception as error:
            raise ValueError(f"Valor erróneo en lo que se haya introducido {error}")














class Catalogo(IPersistencia):  # Tenemos que guardar los catálogos

    def __init__(self, lista_canciones: list["Cancion"]):
        self._lista_canciones = lista_canciones

    def __str__(self):
        msg = "\n"
        for i, cancion in enumerate(self.get_lista_canciones()):
            msg += f"\t\t\t[{i}]: {cancion} \n"
        return msg

    def get_lista_canciones(self):
        return self._lista_canciones

    def set_lista_canciones(self, nueva_lista: list["Cancion"]):
        self._lista_canciones = nueva_lista

    def filtrar_catalogo(self, artista: str = None, genero: str = None):
        catalogo_filtrado: list["Cancion"] = []

        if artista is not None and genero is not None:
            for cancion in self.get_lista_canciones():
                if (
                    cancion.get_artista().lower() == artista
                    and cancion.get_genero().lower() == genero
                ):
                    catalogo_filtrado.append(cancion)

        elif artista is not None and genero is None:
            for cancion in self.get_lista_canciones():
                if cancion.get_artista().lower() == artista:
                    catalogo_filtrado.append(cancion)

        elif genero is not None and artista is None:
            for cancion in self.get_lista_canciones():
                if cancion.get_genero().lower() == genero:
                    catalogo_filtrado.append(cancion)

        elif genero is None and artista is None:
            catalogo_filtrado = self.get_lista_canciones()

        else:
            raise ValueError("Los valores introducidos no son válidos")

        return catalogo_filtrado

    def devolver_canciones_en_catalogo_por_consola(self):
        lista_canciones : list['Cancion'] = []
        seguir_anyadiendo : bool = True
        while seguir_anyadiendo:
            continuar : str = input("¿Desea seguir añadiendo canciones? ")
            if continuar == "si":
                id_cancion : str = input("Introduzca el id de la canción -> ")
                if self.devolver_cancion_por_id(id_cancion) is not None:
                    lista_canciones.append(self.devolver_cancion_por_id(id_cancion))
                else:
                    print("Id introducido no válido")
            elif continuar == "no":
                seguir_anyadiendo = False
            else:
                print("Introduce si o no")
        return lista_canciones

    def devolver_cancion_por_id(self, id: str) -> "Cancion":
        contador: int = 0
        cancion_encontrada: bool = False
        cancion: "Cancion" = Cancion()
        while contador < len(self.get_lista_canciones()) and not cancion_encontrada:
            if self.get_lista_canciones()[contador].get_identificador() == id:
                cancion = self.get_lista_canciones()[contador]
                cancion_encontrada = True
            contador += 1
        return cancion if cancion_encontrada else None

    def comprobar_lista_canciones_por_id(self, lista_ids:list['str']) -> list['Cancion']:
        """Dada una lista de ids, devuelve la lista de canciones cuyos ids están en el catálogo"""
        lista_canciones_validas:list['Cancion'] = list()
        for id_cancion in lista_ids:
            cancion = self.devolver_cancion_por_id(id_cancion) # Puede ser None
            if cancion:
                lista_canciones_validas.append(cancion)
        return lista_canciones_validas

    def listar_canciones(self, filtrar_por_genero=None, filtrar_por_artista=None):
        for i, cancion in enumerate(
            self.filtrar_catalogo(
                genero=filtrar_por_genero, artista=filtrar_por_artista
            )
        ):
            print(f"\t\t\t[{i}]: {cancion}")

    def eliminar_cancion(self, id_cancion: "Cancion"):
        if self.devolver_cancion_por_id(id_cancion):

            encontrada = False
            posicion = 0
            while not encontrada and posicion < len(self.get_lista_canciones()):

                if self.get_lista_canciones()[posicion].get_identificador() == id_cancion:
                    self.get_lista_canciones().pop(posicion)
                    encontrada = True
                else:
                    posicion += 1
        else:
            print(f"No se puede eliminar la canción. La canción {id_cancion}  no está en la lista.")


    def objeto_a_csv(self):
        pass

    def csv_a_objeto(self):
        pass

    def texto_a_objeto(self, diccionario_texto: str):
        pass

    def objeto_a_texto(self):
        pass

    def objeto_a_diccionario(self):

        diccionario_catalogo: list = list()
        for cancion in self.get_lista_canciones():
            diccionario_catalogo.append(cancion.objeto_a_diccionario())
        return diccionario_catalogo

    def diccionario_a_objeto(self, diccionario_catalogo: dict):
        nueva_lista_canciones: list["Cancion"] = []
        for datos_cancion in diccionario_catalogo:
            cancion = Cancion()
            cancion: Cancion = cancion.diccionario_a_objeto(datos_cancion)
            nueva_lista_canciones.append(cancion)




class CatalogoPersonal(Catalogo):
    def __init__(self, lista_canciones: list["Cancion"]):
        super().__init__(lista_canciones)

    def anyadir_cancion_a_catalogo(self, cancion: "Cancion"):
        self.get_lista_canciones().append(cancion)

    def comprobar_lista_canciones_por_id(self, lista_ids:list['str']) -> list['Cancion']:
        """Dada una lista de ids, devuelve la lista de canciones cuyos ids están en el catálogo"""
        lista_canciones_validas:list['Cancion'] = list()
        for id_cancion in lista_ids:
            cancion = self.devolver_cancion_por_id(id_cancion) # Puede ser None
            if cancion:
                lista_canciones_validas.append(cancion)
        return lista_canciones_validas

    def eliminar_cancion_de_catalogo(self, cancion: "Cancion"):
        encontrada = False
        posicion = 0
        while not encontrada and posicion < len(self.get_lista_canciones()):
            print(f" pos : {posicion}")
            if (
                self.get_lista_canciones()[posicion].get_identificador()
                == cancion.get_identificador()
            ):
                encontrada = True
                self.get_lista_canciones().pop(posicion)
            posicion += 1
