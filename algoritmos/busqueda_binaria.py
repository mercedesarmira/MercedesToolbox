# Búsqueda binaria

def busqueda_binaria(lista_ordenada, dato):
    """
    aquí escribimos el docstring
    """

    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio] == dato:
            return medio
        elif lista_ordenada[medio] < dato:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None
