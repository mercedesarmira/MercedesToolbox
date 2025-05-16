# Busqueda lineal

def busqueda_lineal(lista, dato):
    """
    Aquí escribimos el docstring de esta función
    """
    for i, elemento in enumerate(lista):
        if elemento == dato:
            return i
    return None
