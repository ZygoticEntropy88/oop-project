from menus import Menu, MenuInicio, MenuPrincipal, MenuReproduccion, MenuCatalogoGenerico, MenuCatalogoPersonal, MenuListasReproduccion
from usuarios import UsuarioAnonimo, Usuario, UsuarioPremium
from memoria import Memoria

HASH_MENUS: dict[int: 'Menu'] = {
	0: MenuInicio(),
	1: MenuPrincipal(),
	2: MenuReproduccion(),
	3: MenuCatalogoGenerico(),
	4: MenuCatalogoPersonal(),
	5: MenuListasReproduccion()
}

class Controlador:

	def __init__(self, 
			memoria:'Memoria',
			usuario_actual = UsuarioAnonimo(),
			menu_actual = MenuInicio()):

		self._memoria:'Memoria' = memoria
		self._usuario_actual:'Usuario' = usuario_actual
		self._menu_actual: 'Menu' = menu_actual

		self._ejecutandose: bool = True

	def get_estado_aplicacion(self) -> bool:
		return self._ejecutandose

	def get_usuario_actual(self) -> 'Usuario':
		return self._usuario_actual

	def comprobar_acceso_premium(self) -> bool:
		"""Sirve como flag para restringir el acceso a aquellos menús que solo están disponibles para usuarios premium"""
		if self.get_usuario_actual().get_tipo_usuario() == "Premium":
			return True
		return False

	def set_usuario_actual(self, nuevo_usuario:'Usuario' = None) -> bool:
		if nuevo_usuario and self._memoria.comprobar_credenciales_validas(nuevo_usuario):
			print(f"Login correcto: {nuevo_usuario}")
			self._usuario_actual = nuevo_usuario
			return True
		
		self._usuario_actual = UsuarioAnonimo()
		return False

	def imprimir_opciones(self):
		self._menu_actual.imprimir()

	def __cerrar_sesion_usuario(self):
		self.set_usuario_actual() # Cómo no le paso ninguno, va a establecer el usuario como UsuarioAnonimo

	def __apagar_controlador(self):
		self._ejecutandose = not self._ejecutandose
		# ANTES DE SALIR TENEMOS QUE GUARDAR LA MEMORIA EN DISCO
		self._memoria.guardar_en_disco()

	def __cambiar_al_menu_con_id(self, id_menu:int):
		self._menu_actual = HASH_MENUS[id_menu]

	def __cambiar_al_menu_anterior(self):
		id_menu:int = self._menu_actual.get_numero_menu()
		if  id_menu == 0:
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
				id_menu:int = self._menu_actual.get_numero_menu()

				# ============================ MENU INICIO ============================
				if id_menu == 0:
					if opcion == 2:
						# REGISTRAR UN NUEVO USUARIO
						nuevo_usuario: 'Usuario' = self._menu_actual.registrar()
						self._memoria.anyadir_usuario(nuevo_usuario)
					elif opcion == 3:
						# LOGIN DE UN USUARIO PREVIAMENTE REGISTRADO
						nuevo_usuario: 'Usuario' = self._menu_actual.login()
						nuevo_usuario_cargado: 'Usuario' = self._memoria.cargar_usuario_por_nombre_y_contrasenya(
							nombre = nuevo_usuario.get_nombre_usuario(),
							contrasenya = nuevo_usuario.get_contrasenya()
						)
						if nuevo_usuario_cargado:
							self._usuario_actual = nuevo_usuario_cargado
							self.__cambiar_al_menu_con_id(1)
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


				# TODO: IMPORTANTE SOLICIONAR ERRORES CON MENU REPRODUCTOR --> MODULO NO FUNCIONA
				# ============================ MENU REPRODUCTOR ============================
				elif id_menu == 2:
					# REPRODUCIR POR ID
					if opcion == 2:
						id_cancion = self._menu_actual.reproducir_por_id()
                        #self.get_memoria().comprobarcancionporid(id_cancion).imprimir
					# PAUSAR REPRODUCCION
					elif opcion == 3:
						self._menu_actual.pausar_cancion()
					# RENAUDAR REPRODUCCIÓN
					elif opcion == 4:
						self._menu_actual.reanudar_cancion()


				# ========================= MENÚ CATÁLOGO GENÉRICO =========================
				elif id_menu == 3:
					
					if opcion == 2:
						self._menu_actual.listar_canciones(self._memoria.get_catalogo_generico())


				# ========================= MENÚ CATÁLOGO PERSONAL =========================
				elif id_menu == 4:
					if not self.usuario_actual.comprobar_acceso_premium():
						print("Lo sentimos el catálogo personal está solo disponible para usuarios premium")
					else:
						

						if opcion == 2:
							self.menu_actual.listar_canciones()

						elif opcion == 3:
							nueva_cancion = self.menu_actual.anyadir_cancion_a_catalogo()
							self.usuario_actual.anyadir_cancion_a_catalogo(nueva_cancion)

						elif opcion == 4:
							cancion_a_eliminar = self.menu_actual.eliminar_cancion_de_catalogo()
							self.usuario_actual.eliminar_cancion_de_catalogo(cancion_a_eliminar)

				# ========================= MENÚ LISTAS REPRODUCCIÓN =========================
				elif id_menu == 5:
					pass

		except TypeError as e:
			print(f"La opción escogida debe ser un número entero. {e}")
		except Exception as e:
			print(f"Error: {e}")
		return opcion
