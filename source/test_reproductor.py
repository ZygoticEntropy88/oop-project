from reproductor import Reproductor, EstadoReproductor, ReproduccionError

# Importar lo que necesitemos del modulo reproductor.py


def menu():
    print("---------------------------------------")
    print("Opciones:")
    print("1. Reproducir desde YouTube (stream)")
    print("2. Pausar")
    print("3. Reanudar")
    print("4. Salir")


if __name__ == "__main__":
    reproductor: Reproductor = Reproductor()
    continuar: bool = True
    while continuar:
        menu()
        opcion: str = input("Selecciona una opción: ").strip()
        try:
            if opcion == "1":
                vid: str = input("ID de YouTube: ").strip()
                reproductor.reproducir_desde_youtube(vid)
                print("Reproduciendo (stream)")
            elif opcion == "2":
                if (
                    reproductor.obtener_estado_reproductor()
                    == EstadoReproductor.REPRODUCIENDO
                ):
                    reproductor.pausar()
                    print("> He pausado la reproducción")
                else:
                    print("> Sin cambios - No hay nada sonando en este momento!")
            elif opcion == "3":
                if (
                    reproductor.obtener_estado_reproductor()
                    == EstadoReproductor.PAUSADO
                ):
                    reproductor.reanudar()
                    print("> He reanudado la reproducción")
                else:
                    print("> Sin cambios - No hay nada sonando en este momento!")
            elif opcion == "4":
                continuar = False
            else:
                print("Opción no válida.")
        except ReproduccionError as e:
            print(f"ERROR: {e}")
        except ValueError:
            print("ERROR: Debes introducir un número entero.")
