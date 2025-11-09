from menus import MenuInicio, MenuPrincipal, MenuReproduccion, MenuCatalogoGenerico, MenuCatalogoPersonal, MenuListasReproduccion
from enum import Enum

menus:dict['Menu'] = {
    0:MenuInicio,
    1:MenuPrincipal,
    2:MenuReproduccion,
    3:MenuCatalogoGenerico,
    4:MenuCatalogoPersonal,
    5:MenuListasReproduccion
}

if __name__ == '__main__':
    numero_menu :int = 0
    ejecutar = True

    menus[numero_menu].imprimir()
    opcion = input(">> ")
    numero_menu = menus[numero_menu].ejecutar(opcion)