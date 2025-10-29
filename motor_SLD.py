# =============================================
#  RESOLUCIÓN SLD - SISTEMA EXPERTO EN GASTRONOMÍA:)
# =============================================
# Este script implementa la resolución SLD (Selective Linear Definite-clause resolution)
# utilizando una base de conocimiento con hechos y reglas expresadas en cláusulas de Horn.

# Importa la base de conocimiento desde un archivo aparte
from base_conocimiento import HECHOS, REGLAS

# FUNCIÓN: UNIFICACIÓN
# Intenta encontrar una sustitución que haga que dos predicados sean equivalentes.
def unificar(x, y, sustituciones=None):
    if sustituciones is None:
        sustituciones = {}

    if x == y:
        return sustituciones
    if isinstance(x, str) and x.startswith("?"):
        return unificar_var(x, y, sustituciones)
    elif isinstance(y, str) and y.startswith("?"):
        return unificar_var(y, x, sustituciones)
    elif isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):

        # En lugar del for, se podría aplicar recursividad
        """Se vería algo así
        def unificar_tuplas(x, y, sustituciones={}):
            if i == len(x): # Caso base
                return sustituciones
            sustituciones = unificar(x[i], y[i], sustituciones)
            if sustituciones is None:
                return None
            return unificar_tuplas(x, y, i + 1, sustituciones) 
            
        return unificar_tuplas(x, y, 0, sustituciones)
            """

        for xi, yi in zip(x, y):
            sustituciones = unificar(xi, yi, sustituciones)
            if sustituciones is None:
                return None
        return sustituciones
    else:
        return None

def unificar_var(var, valor, sustituciones):
    if var in sustituciones:
        return unificar(sustituciones[var], valor, sustituciones)
    elif valor in sustituciones:
        return unificar(var, sustituciones[valor], sustituciones)
    else:
        # Si la variable ya está asignada a otro valor distinto, hay conflicto
        sustituciones[var] = valor
        return sustituciones

# FUNCIÓN: APLICAR SUSTITUCIONES
def aplicar_sustitucion(obj, sustituciones):
    if isinstance(obj, str) and obj.startswith("?"):
        return sustituciones.get(obj, obj)
    elif isinstance(obj, tuple):

        # Aquí hay un for, lo si lo cambiara por recursividad sería algo así:
        """
        def aplicar_recursividad(tupla, sustituciones, i=0):
            if i == len(tupla): # Caso base
                return ()
            return (aplicar_sustitucion(tupla[i], sustituciones),) + aplicar_recursividad(tupla, sustituciones, i + 1)
            
        return aplicar_recursividad(obj, sustituciones)"""

        return tuple(aplicar_sustitucion(x, sustituciones) for x in obj)
    else:
        return obj

# MOTOR SLD
def sld(query, hechos, reglas, profundidad=0, ruta=None):
    if ruta is None:
        ruta = []

    print("  " * profundidad + f"-> Consultando: {query}")

    # Para usar recursividad en lugar de for, podría aplicarse así:
    """
    def verificar_hechos(index=0):
        if index == len(hechos):  # Caso base: sin coincidencia
            return None
        sustituciones = unificar(query, hechos[index])
        if sustituciones is not None:
            print("  " * profundidad + f"Coincidencia con hecho: {hechos[index]}")
            return sustituciones
        return verificar_hechos(index + 1)
    
    return verificar_hechos(0)
    """


    # Caso base: si el query se cumple directamente con los hechos
    for hecho in hechos:
        sustituciones = unificar(query, hecho)
        if sustituciones is not None:
            print("  " * profundidad + f"Coincidencia con hecho: {hecho}")
            return sustituciones

    # Si el predicado es una comparación de tiempo, la resolvemos manualmente
    if query[0] == "tiempo_menor_que":
        receta, limite = query[1], query[2]
        for hecho in hechos:
            if hecho[0] == "tiempo_preparacion" and hecho[1] == receta:
                if hecho[2] < limite:
                    print("  " * profundidad + f"{receta} tiene tiempo {hecho[2]} < {limite}")
                    return {}
        return None
    
    # Para este caso, también aplicando recursividad, quedaría así:
    """
    def buscar_tiempo(index=0):
        if index == len(hechos):  # Caso base: sin coincidencia
            return None
        hecho = hechos[index]
        if hecho[0] == "tiempo_preparacion" and hecho[1] == receta and hecho[2] < limite:
            print(" " * profunidad + f"{receta} tiene tiempo {hecho[2]} < {limite}")
                return {}
        return buscar_tiempo(index + 1)
    """
    # Y se reemplaza el for con: return buscar_tiempo(0) :)



    # Si no hay coincidencia directa, intentamos usar reglas
    for regla in reglas:
        sustituciones = unificar(query, regla["head"])
        if sustituciones is not None:
            print("  " * profundidad + f"Aplicando regla: {regla['head']}")
            nueva_meta = [aplicar_sustitucion(b, sustituciones) for b in regla["body"]]

            todas_satisfechas = True
            for meta in nueva_meta:
                sub = sld(meta, hechos, reglas, profundidad + 1, ruta)
                if sub is None:
                    todas_satisfechas = False
                    break
                sustituciones.update(sub)

            if todas_satisfechas:
                print("  " * profundidad + f"Se cumple: {query}")
                return sustituciones

    print("  " * profundidad + f"No se pudo resolver: {query}")
    return None

# Igual para este caso, se podría usar recursividad así:
"""
def procesar_reglas(index=0):
    if index == len(reglas):  # Caso base: sin coincidencia
        print("  " * profundidad + f"No se pudo resolver: {query}")
        return None
    regla = reglas[index]
    sustituciones = unificar(query, regla["head"])
    if sustituciones is not None:
        print("  " * profundidad + f"Aplicando regla: {regla['head']}")
        nueva_meta = [aplicar_sustitucion(b, sustituciones) for b in regla["body"]]

        todas_satisfechas = True
        for meta in nueva_meta:
            sub = sld(meta, hechos, reglas, profundidad + 1, ruta)
            if sub is None:
                todas_satisfechas = False
                break
            sustituciones.update(sub)

        if todas_satisfechas:
            print("  " * profundidad + f"Se cumple: {query}")
            return sustituciones
    return procesar_reglas(index + 1)
"""
# Se reemplaza el for con: return procesar_reglas(0) 
# Y ya, básicamente así cambio mis for, por recursividad :)

# EJECUCIÓN DE PRUEBA
if __name__ == "__main__":
    # Ejemplo 1: receta muy picante (si incluye chile habanero o pasilla)
    consulta = ("muy_picante", "enchiladas_verdes")
    print("\n=== Prueba 1: Consulta de receta picante ===")
    resultado = sld(consulta, HECHOS, REGLAS)
    print("\nResultado:", resultado)

    # Ejemplo 2: receta ligera (tiempo menor a 40)
    consulta2 = ("ligera", "tostadas_de_tinga")
    print("\n=== Prueba 2: Consulta de receta ligera ===")
    resultado2 = sld(consulta2, HECHOS, REGLAS)
    print("\nResultado:", resultado2)
