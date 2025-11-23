from memoria import Memoria
from controlador import Controlador
from persistencia import ErrorGravePersistencia

if __name__ == "__main__":
    print(
        "\n ################################ U-MUSIC ################################\n"
    )
    try:
        memoria: Memoria = Memoria()
        print(memoria)
    except ErrorGravePersistencia as e:
        print(f"ERROR: {e}")
    else:
        controlador: Controlador = Controlador(memoria)

        while controlador.get_estado_aplicacion():
            controlador.imprimir_opciones()
            controlador.ejecutar()