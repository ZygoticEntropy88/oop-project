from menus import (
    Menu,
    MenuInicio,
    MenuPrincipal,
    MenuReproduccion,
    MenuCatalogoGenerico,
    MenuCatalogoPersonal,
    MenuListasReproduccion,
)
from usuarios import UsuarioAnonimo, Usuario, UsuarioPremium
from memoria import Memoria
from canciones import Cancion
from listas import Lista

HASH_MENUS: dict[int:"Menu"] = {
    0: MenuInicio(),
    1: MenuPrincipal(),
    2: MenuReproduccion(),
    3: MenuCatalogoGenerico(),
    4: MenuCatalogoPersonal(),
    5: MenuListasReproduccion(),
}


class Controlador:

    def __init__(
        self,
        memoria: "Memoria",
        usuario_actual=UsuarioAnonimo(),
        menu_actual=MenuInicio(),
    ):

        self._memoria: "Memoria" = memoria
        self._usuario_actual: "Usuario" = usuario_actual
        self._menu_actual: "Menu" = menu_actual

        self._ejecutandose: bool = True

    def get_estado_aplicacion(self) -> bool:
        return self._ejecutandose

    def get_usuario_actual(self) -> "Usuario":
        return self._usuario_actual

    def get_memoria(self):
        return self._memoria

    def get_menu_actual(self):
        return self._menu_actual

    def comprobar_acceso_premium(self) -> bool:
        """Sirve como flag para restringir el acceso a aquellos menús que solo están disponibles para usuarios premium"""
        if self.get_usuario_actual().get_tipo_usuario() == "Premium":
            return True
        return False

    def set_usuario_actual(self, nuevo_usuario: "Usuario" = None) -> bool:
        if nuevo_usuario and self._memoria.comprobar_credenciales_validas(
            nuevo_usuario
        ):
            print(f"Login correcto: {nuevo_usuario}")
            self._usuario_actual = nuevo_usuario
            return True

        self._usuario_actual = UsuarioAnonimo()
        return False

    def imprimir_opciones(self):
        self._menu_actual.imprimir(self.get_usuario_actual().get_nombre_usuario())

    def __cerrar_sesion_usuario(self):
        self._memoria.guardar_en_disco()
        self.set_usuario_actual()  # Cómo no le paso ninguno, va a establecer el usuario como UsuarioAnonimo

    def __apagar_controlador(self):
        self.__cerrar_sesion_usuario()  # Ya guarda la memoria en disco
        self._ejecutandose = not self._ejecutandose

    def __cambiar_al_menu_con_id(self, id_menu: int):
        self._menu_actual = HASH_MENUS[id_menu]

    def __cambiar_al_menu_anterior(self):
        id_menu: int = self._menu_actual.get_numero_menu()
        if id_menu == 0:
            # Entendemos que volver al menú anterior en el MENU INICIO es equivalente a salir de la aplicación
            self.__apagar_controlador()
        elif id_menu == 1:
            # Entendemos que el usuario quiere cerrar sesión para quizá, hacer login con otra cuenta.
            self.__cerrar_sesion_usuario()
            self.__cambiar_al_menu_con_id(0)
        else:
            self.__cambiar_al_menu_con_id(1)

    def ejecutar(self):
        try:
            opcion = int(input("Introduzca la opción que desea ejecutar --> "))
            if opcion == 0:
                self.__apagar_controlador()
            elif opcion == 1:
                self.__cambiar_al_menu_anterior()
            else:
                # La opción escogida no es ni volver al menú anterior, ni salir de la aplicación: luego es una opción específica
                # del menú actual.
                id_menu: int = self._menu_actual.get_numero_menu()

                # ============================ MENU INICIO ============================
                if id_menu == 0:
                    if opcion == 2:
                        # REGISTRAR UN NUEVO USUARIO
                        nuevo_usuario: "Usuario" = self.get_menu_actual().registrar()
                        self._memoria.anyadir_usuario(nuevo_usuario)
                    elif opcion == 3:
                        # LOGIN DE UN USUARIO PREVIAMENTE REGISTRADO
                        nuevo_usuario: "Usuario" = self._menu_actual.login()
                        nuevo_usuario_cargado: "Usuario" = (
                            self._memoria.cargar_usuario_por_nombre_y_contrasenya(
                                nombre=nuevo_usuario.get_nombre_usuario(),
                                contrasenya=nuevo_usuario.get_contrasenya(),
                            )
                        )
                        if nuevo_usuario_cargado:
                            self._usuario_actual = nuevo_usuario_cargado
                            self.__cambiar_al_menu_con_id(1)
                            self._memoria.guardar_en_disco()

                        else:
                            print("No se ha podido cargar el usuario.")
                    elif opcion == 4:
                        # CONTINUAR COMO INVITADO
                        self.__cerrar_sesion_usuario()
                        self.__cambiar_al_menu_con_id(1)

                # ============================ MENU PRINCIPAL ============================
                elif id_menu == 1:

                    # DESPLAZARSE AL MENÚ CORRESPONDIENTE
                    if 2 <= opcion <= 5:
                        self.__cambiar_al_menu_con_id(opcion)

                # ============================ MENU REPRODUCTOR ============================
                elif id_menu == 2:
                    # REPRODUCIR POR ID
                    if opcion == 2:
                        id_cancion: str = self._menu_actual.reproducir_por_id()
                        if self.get_memoria().comprobar_cancion_en_catalogo(id_cancion):
                            cancion_actual = (
                                self.get_memoria()
                                .get_catalogo_generico()
                                .devolver_cancion_por_id(id_cancion)
                            )
                            print(
                                f"Reproduciendo actualmente : {cancion_actual.__str__()}"
                            )

                        elif self.get_usuario_actual().tipo_usuario() == "PREMIUM" and self.get_memoria().comprobar_cancion_en_catalogo_premium(
                                id_cancion, self.get_usuario_actual().get_nombre()
                        ):
                            cancion_actual = (
                                self.get_memoria()
                                .get_catalogo_generico()
                                .devolver_cancion_por_id(id_cancion)
                            )
                            print(
                                f"Reproduciendo actualmente : {cancion_actual.__str__()}"
                            )

                        else:
                            print("Cancion desconocida")

                    elif opcion == 3:
                        self.get_menu_actual().pausar_cancion()
                    # RENAUDAR REPRODUCCIÓN
                    elif opcion == 4:
                        self._menu_actual.reanudar_cancion()

                # ========================= MENÚ CATÁLOGO GENÉRICO =========================
                elif id_menu == 3:

                    if opcion == 2:
                        self._menu_actual.listar_canciones(
                            self._memoria.get_catalogo_generico()
                        )

                # ========================= MENÚ CATÁLOGO PERSONAL =========================
                elif id_menu == 4:
                    if not self._usuario_actual.comprobar_acceso_premium():
                        print(
                            "Lo sentimos el catálogo personal está solo disponible para usuarios premium."
                        )
                        self.__cambiar_al_menu_anterior()
                    else:

                        if opcion == 2:
                            self._menu_actual.listar_catalogo_personal(
                                self._usuario_actual.get_catalogo_personal()
                            )

                        elif opcion == 3:
                            nueva_cancion = self._menu_actual.anyadir_cancion()
                            self._usuario_actual.anyadir_cancion_a_catalogo(
                                nueva_cancion
                            )

                        elif opcion == 4:
                            cancion_a_eliminar = self._menu_actual.eliminar_cancion()
                            self._usuario_actual.eliminar_cancion_de_catalogo(
                                cancion_a_eliminar
                            )

                # ========================= MENÚ LISTAS REPRODUCCIÓN =========================
                elif id_menu == 5:
                    nombre_usuario_actual:str = self.get_usuario_actual().get_nombre_usuario() 

                    if self.get_memoria().comprobar_usuario_registrado(nombre_usuario_actual):

                        # MOSTRAR TODAS LAS LISTAS
                        if opcion == 2:
                            self.get_menu_actual().mostrar_todas_las_listas(self.get_usuario_actual().get_listas_reproduccion())

                        # MOSTRAR CANCIONES EN LISTA
                        elif opcion == 3:
                            self.get_menu_actual().mostrar_canciones_en_lista(
                                self.get_usuario_actual().get_listas_reproduccion()
                            )

                        # CREAR LISTA
                        elif opcion == 4:

                            nombre_lista, descripcion_lista, fecha, ids_canciones = self.get_menu_actual().crear_lista()
                            canciones_validas  = self.get_memoria().get_catalogo_generico().comprobar_lista_canciones_por_id(ids_canciones)

                            # Si el usuario es premium, también añado las que estén en el catálogo personal
                            if self.get_usuario_actual().comprobar_acceso_premium():
                                canciones_validas += self.get_usuario_actual().get_catalogo_personal().comprobar_lista_canciones_por_id(ids_canciones)

                            nueva_lista: 'Lista' =  Lista(
                                nombre_lista,
                                descripcion_lista,
                                canciones_validas,
                                fecha_creacion=fecha,
                                usuario_creador=self.get_usuario_actual().get_nombre_usuario(),
                            )

                            self.get_usuario_actual().get_listas_reproduccion().append(nueva_lista)

                        # ELIMINAR LISTA
                        elif opcion == 5:
                            self.get_menu_actual().eliminar_lista(self.get_usuario_actual())

                        # AÑADIR CANCIÓN A LISTA
                        elif opcion == 6:
                            id_cancion, nombre_lista = self.get_menu_actual().anyadir_cancion_a_lista()
                            posicion_lista_buscada, lista_buscada = self.get_usuario_actual().devolver_lista_por_nombre(nombre_lista)
                            if lista_buscada:
                                cancion = self.get_memoria().get_catalogo_generico().devolver_cancion_por_id(id_cancion)
                                if self.get_usuario_actual().comprobar_acceso_premium() and not cancion:
                                    cancion = self.get_usuario_actual().get_catalogo_personal().devolver_cancion_por_id(id_cancion)
                                if cancion:
                                    self.get_usuario_actual().get_listas_reproduccion()[posicion_lista_buscada].anyadir_cancion(cancion)
                                else:
                                    print("No se puede añadir la cancion {id_cancion} a la lista. Esta canción no está disponible en ningún catálogo.")
                            else:
                                print(f"No se pudo añadir la canción {id_cancion} a la lista {nombre_lista}.")

                    else:
                        print("Usuario no registrado")
                        self.__cambiar_al_menu_anterior()


        #except TypeError as e:
         #4
        #print(f"La opción escogida debe ser un número entero. {e}")
        except Exception as e:
            print(f"Error: {e}")