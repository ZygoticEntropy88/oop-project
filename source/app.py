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
    id = 0
    ejecutar = True

    while ejecutar:
        print(menus[id])
        opcion = input(">> ")
        id = menus[id].ejecutar(opcion)