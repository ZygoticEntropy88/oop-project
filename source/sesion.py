from usuarios.usuario import Usuario
from usuarios.usuario_premium import UsuarioPremium

class Sesion: #Instanciaremos un objeto de esta clase nada más inicializar el main
    def __init__(self, archivo_usuarios : dict, catalogo_generico : str):
        self._csv_usuarios = archivo_usuarios
        self._catalogo_generico = catalogo_generico
        self._usuario_actual : Usuario = self.set_usuario_actual(self.login_usuario())
        
    def get_csv_usuarios(self):
        return self._csv_usuarios

    def get_catalogo_generico (self):
        return self._catalogo_generico

    def set_usuario_actual(self, nuevo_usuario : 'Usuario'):
        self._usuario_actual = nuevo_usuario

    def login_usuario(self) -> 'Usuario': #La clase menú llamará a esta función
        nombre_usuario : str = str(input("Introduzca nombre de usuario"))
        contrasenya : str = str(input("Introduzca contraseña"))
        encontrado : bool = False
        usuario_actual : Usuario = Usuario()
        usuario_actual.diccionario_a_objeto(self.get_csv_usuarios())
        return usuario_actual
