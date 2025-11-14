from persistencia import IPersistencia
from fecha import Fecha

from listas import Lista, Catalogo
from canciones import Cancion


class Usuario(IPersistencia):
    def __init__(self, 
                nombre_de_usuario : str = "user",
                fecha_nacimiento : Fecha = Fecha(),
                correo_electronico : str = "",
                contrasenya : str = "12345678",
                fecha_registro : Fecha = Fecha(),
                catalogo_generico : 'Catalogo' = None):

        self._nombre_de_usuario:str = nombre_de_usuario
        self._fecha_de_nacimiento:Fecha = fecha_nacimiento
        self._correo_electronico:str = correo_electronico
        self._contrasenya:str = contrasenya
        self._fecha_de_registro:Fecha = fecha_registro
        self._catalogo_generico = catalogo_generico

    def get_nombre_usuario (self):
        return self._nombre_de_usuario

    def get_fecha_nacimiento(self):
        return self._fecha_de_nacimiento

    def get_correo_electronico (self):
        return self._correo_electronico

    def get_contrasenya (self):
        return self._contrasenya

    def get_fecha_registro (self):
        return self._fecha_de_registro

    def get_catalogo_generico(self):
        return self._catalogo_generico

    def set_nombre_usuario (self, nuevo_nombre : str):
        self._nombre_de_usuario = nuevo_nombre

    def set_apellidos (self, nuevos_apellidos : str):
        self._apellidos = nuevos_apellidos

    def set_email (self, nuevo_email : str):
        self._email = nuevo_email

    def set_fecha_nacimiento(self, nueva_fecha : Fecha):
        self._fecha_de_nacimiento = nueva_fecha

    def set_correo_electronico (self, nuevo_correo : str):
        self._correo_electronico = nuevo_correo

    def set_contrasenya (self, nueva_contrasenya : str):
        self._contrasenya = nueva_contrasenya

    def set_fecha_registro (self, nueva_fecha_registro : Fecha):
        self._fecha_de_registro = nueva_fecha_registro

    def set_catalogo_generico(self, nuevo_catalogo_generico : 'Catalogo'):
        self._catalogo_generico = nuevo_catalogo_generico

    def crear_nuevo_usuario_por_consola(self):
        nombre:str = input("Ingresa tu nombre: ")
        apellidos:str = input("Ingresa tu apellido: ")
        email:str = input("Ingresa tu email: ")
        fecha_nacimiento = Fecha()
        fecha_registro = Fecha()
        fecha_nacimiento.solicitar_usuario("(fecha de nacimiento)")
        fecha_registro.solicitar_usuario("(fecha de registro)")
        contrasenya:str = input("Establece una contraseña: ")

        self.set_nombre_usuario(nombre)
        self.set_apellidos(apellidos)
        self.set_email(email)
        self.set_fecha_nacimiento(fecha_nacimiento)
        self.set_fecha_registro(fecha_registro)
        self.set_contrasenya(contrasenya)



    def crear_lista_reproduccion(self, lista_canciones : list['Cancion']):
        nombre_lista: str = str(input("Ingrese el nombre de la lista"))
        descripcion_lista: str = str(input("Añade una descripción a la lista"))
        fecha_creacion :'Fecha' = Fecha(10, 11, 2025)
        nueva_lista: 'Lista' = Lista(nombre_lista, descripcion_lista, lista_canciones, fecha_creacion, self)
        return nueva_lista

    # ===================================================================================
    #                  IMPLEMENTACIONES DE LA INTERFAZ DE PERSISTENCIA
    # ===================================================================================
    def objeto_a_texto (self):
        usuario_texto : str = ""
        usuario_texto += f"Nombre:  {self.get_nombre_usuario()} \n"
        usuario_texto += f"Fecha Nacimiento:  {self.get_fecha_nacimiento()} \n"
        usuario_texto += f"Correo Electrónico:  {self.get_correo_electronico()} \n"
        usuario_texto += f"Contraseña:  {self.get_contrasenya()} \n"
        usuario_texto += f"Fecha Registro:  {self.get_fecha_registro()} \n"
        return usuario_texto

    def objeto_a_diccionario (self):
        usuario = {
            "Nombre" : self.get_nombre_usuario(),
            "Fecha Nacimiento" : self.get_fecha_nacimiento(),
            "Correo Electrónico" : self.get_correo_electronico(),
            "Contraseña" : self.get_contrasenya(),
            "Fecha Registro" : self.get_fecha_registro()
        }
        return usuario

    def objeto_a_csv(self):
        pass

    def texto_a_objeto (self, texto : str):
        pass

    def diccionario_a_objeto (self, diccionario_usuario : dict):
        try:
            if "Nombre" in diccionario_usuario and diccionario_usuario["Nombre"]:
                self.set_nombre_usuario(diccionario_usuario["Nombre"])

            if "Fecha de Nacimiento" in diccionario_usuario and diccionario_usuario["Fecha de Nacimiento"]:
                self.set_fecha_nacimiento(diccionario_usuario["Fecha de Nacimiento"])

            if "Correo Electrónico" in diccionario_usuario and diccionario_usuario["Correo Electrónico"]:
                self.set_correo_electronico(diccionario_usuario["Correo Electrónico"])

            if "Contraseña" in diccionario_usuario and diccionario_usuario["Contraseña"]:
                self.set_contrasenya(diccionario_usuario["Contraseña"])

            if "Fecha Registro" in diccionario_usuario and diccionario_usuario["Fecha Registro"]:
                self.set_fecha_registro(diccionario_usuario["Fecha Registro"])

        except Exception as error:
            raise ValueError(f"Valor erróneo en lo que se haya introducido {error}")

    def csv_a_objeto (self):
        pass


class TarjetaCredito (IPersistencia):
    def __init__(self, numero_de_cuenta : int,
                 CVV : int,
                 fecha_de_caducidad : Fecha,
                 nombre_completo_titular : str,
                 propietario : str = None):

        assert (len(str(numero_de_cuenta)) == 16 and
                len(str(CVV)) == 3), "Los datos introducidos no son válidos"

        self._numero_de_cuenta = numero_de_cuenta
        self._CVV = CVV
        self._fecha_de_caducidad = fecha_de_caducidad
        self._nombre_completo_titular = nombre_completo_titular
        self._propietario = propietario

    def get_numero_cuenta (self):
        return self._numero_de_cuenta

    def get_CVV (self):
        return self._CVV

    def get_fecha_caducidad (self):
        return self._fecha_de_caducidad

    def get_nombre_titular (self):
        return self._nombre_completo_titular

    def get_propietario (self):
        return self._propietario

    def set_numero_cuenta (self, nuevo_numero_cuenta : int):
        self._numero_de_cuenta = nuevo_numero_cuenta

    def set_CVV (self, nuevo_CVV : int):
        self._CVV = nuevo_CVV

    def set_fecha_caducidad (self, nueva_fecha_caducidad : Fecha):
        self._fecha_de_caducidad = nueva_fecha_caducidad

    def set_nombre_titular (self, nuevo_nombre_titular : str):
        self._nombre_completo_titular = nuevo_nombre_titular

    def set_propietario (self, nuevo_propietario : str):
        self._propietario = nuevo_propietario

    # ===================================================================================
    #                  IMPLEMENTACIONES DE LA INTERFAZ DE PERSISTENCIA
    # ===================================================================================
    def objeto_a_diccionario (self):
        tarjeta = {
            "Numero de cuenta": self.get_numero_cuenta(),
            "CVV": self.get_CVV(),
            "Fecha de caducidad": self.get_fecha_caducidad(),
            "Nombre del titular": self.get_nombre_titular(),
            "Propietario" : self.get_propietario()
        }
        return tarjeta

    def diccionario_a_objeto(self, diccionario_tarjeta: dict):
        try:
            if "Numero de cuenta" in diccionario_tarjeta and diccionario_tarjeta["Numero de cuenta"]:
                self.set_numero_cuenta(diccionario_tarjeta["Numero de cuenta"])

            if "CVV" in diccionario_tarjeta and diccionario_tarjeta["CVV"]:
                self.set_CVV(diccionario_tarjeta["CVV"])

            if "Fecha de caducidad" in diccionario_tarjeta and diccionario_tarjeta["Fecha de caducidad"]:
                self.set_fecha_caducidad(diccionario_tarjeta["Fecha de caducidad"])

            if "Nombre del titular" in diccionario_tarjeta and diccionario_tarjeta["Nombre del titular"]:
                self.set_nombre_titular(diccionario_tarjeta["Nombre del titular"])

            if "Propietario" in diccionario_tarjeta and diccionario_tarjeta["Propietario"]:
                self.set_propietario(diccionario_tarjeta["Propietario"])

        except Exception as error:
            raise ValueError(f"Valor erróneo en lo que se haya introducido {error}")

    def objeto_a_csv(self):
        pass

    def objeto_a_texto(self):
        pass

    def csv_a_objeto(self):
        pass

    def texto_a_objeto(self, texto : str):
        pass


class UsuarioPremium(Usuario):
    def __init__(self, nombre_usuario : str,
                 fecha_nacimiento : Fecha,
                 correo_electronico : str,
                 contrasenya : str,
                 fecha_registro : Fecha,
                 tarjeta_credito : TarjetaCredito,
                 catalogo_generico : 'Catalogo',
                 catalogo_personal : 'CatalogoPersonal'):

        super().__init__(nombre_de_usuario = nombre_usuario,
                       fecha_nacimiento = fecha_nacimiento,
                       correo_electronico = correo_electronico,
                       contrasenya = contrasenya,
                       fecha_registro = fecha_registro,
                       catalogo_generico = catalogo_generico)

        self._tarjeta_de_credito = tarjeta_credito
        self._catalogo_personal = catalogo_personal

    def get_tarjeta_credito (self):
        return self._tarjeta_de_credito

    def get_catalogo_personal(self):
        return self._catalogo_personal

    def objeto_a_diccionario(self):
        diccionario_base : dict = super().objeto_a_diccionario()
        diccionario_base["Tarjeta de crédito"] = self.get_tarjeta_credito().objeto_a_diccionario()
        return diccionario_base

    def crear_lista_reproduccion(self, lista_canciones: list['Cancion']):
        contador : int = 0
        pertenece_a_catalogo_personal : bool = True
        while contador < len(lista_canciones) and pertenece_a_catalogo_personal: #Compruebo que todas las canciones que implemento están en el catálogo personal
            if lista_canciones[contador] not in self.get_catalogo_personal():
                pertenece_a_catalogo_personal = False
        contador +=1
        if pertenece_a_catalogo_personal:
            nombre_lista: str = str(input("Ingrese el nombre de la lista"))
            descripcion_lista: str = str(input("Añade una descripción a la lista"))
            fecha_creacion: 'Fecha' = Fecha(10, 11, 2025)
            nueva_lista: 'Lista' = Lista(nombre_lista, descripcion_lista, lista_canciones, fecha_creacion, self)
            return nueva_lista
        else:
            return -1


    def diccionario_a_objeto(self, diccionario_usuario_premium : dict):
        super().diccionario_a_objeto(diccionario_usuario_premium)
        if "Tarjeta de crédito" in diccionario_usuario_premium:
            self.get_tarjeta_credito().diccionario_a_objeto(diccionario_usuario_premium["Tarjeta de crédito"])

class UsuarioAnonimo(Usuario):
    pass