import json
import os
from collections import Counter

def auditar():
    ruta = "data/libros.json"
    auditoria = "data/reportes/reporte_auditoria_estados.json"
    try:
        with open(ruta, "r", encoding='utf-8') as archivo:
            libros = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print('No hay libros en el inventario para generar reporte.')
        return

    if not libros:
        print('El inventario está vacío.')
        return
    mismatches = []
    types = []

    for libro in libros:
        estado = libro.get('Estado')
        prestado_a = libro.get('Prestado a')
        if estado not in ['Disponible', 'Prestado']:
            mismatches.append({**libro, 'Inconsistencia' : 'ESTADO_INVALIDO'})
            types.append('ESTADO_INVALIDO')
        elif estado == 'Disponible' and prestado_a:
            mismatches.append({**libro, 'Inconsistencia' : 'DISPONIBLE_CON_USUARIO'})
            types.append('DISPONIBLE_CON_USUARIO')
        elif estado == 'Prestado' and not prestado_a:
            mismatches.append({**libro, 'Inconsistencia' : 'PRESTADO_SIN_USUARIO'})
            types.append('PRESTADO_SIN_USUARIO')

    print('=' * 50)
    print('REPORTE DE ERRORES DE LIBROS')
    print('=' * 50)

    resumen = {
        'Revisados' : len(libros),
        'Con errores' : len(mismatches),
        'Conteo por tipo' : dict(Counter(types))
    }

    reporte = {
        'Libros con problemas' : mismatches,
        'Resumen' : resumen
    }

    for tipo, cant in resumen['Conteo por tipo'].items():
        print(f'{tipo}: {cant}')
    
    rev = resumen['Revisados']
    errors = resumen['Con errores']
    print(f'Libros revisados: {rev}\n Libros con errores: {errors}')

    os.makedirs('data/reportes', exist_ok=True)
    filename = auditoria
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(reporte, f, indent=4, ensure_ascii=False)
    print(f'Reporte guardado en {filename}')