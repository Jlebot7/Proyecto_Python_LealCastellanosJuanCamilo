
from gestion_libros import *
from buscar_libros import *
from prestamos import *
from reportes import *
import os

def mostrar_menu():
    print('=' * 50)
    print('GESTOR DE INVENTARIO PARA UNA BIBLIOTECA VIRTUAL')
    print('=' * 50)
    print('1. Registrar un nuevo libro')
    print('2. Ver el inventario de libros')
    print('3. Buscar un libro')
    print('4. Prestar un libro')
    print('5. Devolver un libro')
    print('6. Generar un reporte del inventario')
    print('7. Salir')
    print('=' * 50)

while True:
    mostrar_menu()
    try:
        opcion = int(input('Seleccione una opción: '))
    except ValueError:
        print('Opción inválida. Intente de nuevo.')
        input('Presione ENTER para continuar...')
        continue

    if opcion == 1:
        reg_libros()
        input('Presione ENTER para volver al menú...')
    elif opcion == 2:
        listar_libros()
        input('Presione ENTER para volver al menú...')
    elif opcion == 3:
        buscar_libros()
        input('Presione ENTER para volver al menú...')
    elif opcion == 4:
        prestar_libro()
        input('Presione ENTER para volver al menú...')
    elif opcion == 5:
        devolver_libro()
        input('Presione ENTER para volver al menú...')
    elif opcion == 6:
        generar_reporte()
    elif opcion == 7:
        print('Hasta luego!')
        break
    else:
        print('Opcion no valida, reintente.')

