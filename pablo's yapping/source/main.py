from persistencia import Memoria
from controlador import Controlador

if __name__ == "__main__":
	print("\n ################################ U-MUSIC ################################\n")
	memoria:Memoria = Memoria()
	print(memoria)


	controlador:Controlador = Controlador(memoria)

	while controlador.get_estado_aplicacion():
		controlador.imprimir_opciones()
		controlador.ejecutar()