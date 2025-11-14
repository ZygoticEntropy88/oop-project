from menus import MenuInicio, MenuPrincipal, MenuReproduccion, MenuCatalogoGenerico, MenuCatalogoPersonal, MenuListasReproduccion


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
			usuario_actual = None,
			menu_actual = None ):

		self._memoria:'Memoria' = memoria
		self._usuario_actual:'Usuario' = None
		self._menu_actual: 'Menu' = MenuInicio()

		self._ejecutandose: bool = True

	def get_estado_aplicacion(self) -> bool:
		return self._ejecutandose

	def imprimir_opciones(self):
		self._menu_actual.imprimir()

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

				if id_menu == 0:
					
					if opcion == 2:
						# REGISTRAR UN NUEVO USUARIO
						nuevo_usuario: 'Usuario' = self._menu_actual.registrar()
						self._memoria.anyadir_usuario(nuevo_usuario)

					elif opcion == 3:
						# LOGIN USUARIO
						pass
					elif opcion == 4:
						# CONTINUAR COMO INVITADO
						self.__cambiar_al_menu_con_id(1)

				elif id_menu == 1:

					if 2 <= opcion <= 5:
						self.__cambiar_al_menu_con_id(opcion)

				elif id_menu == 2:
					pass

				elif id_menu == 3:
					pass

				elif id_menu == 4:
					pass

				elif id_menu == 5:
					pass

		except TypeError as e:
			print(f"La opción debe ser un número entero. {e}")
		return opcion
