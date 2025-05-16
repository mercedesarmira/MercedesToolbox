"""
Nodo: es la unidad fundamental en estructuras de datos enlazadas.
Contiene un campo para almacenar un dato y un puntero hacia el siguiente nodo
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None