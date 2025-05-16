"""
Estructura de datos que consiste en una secuencia lineal de nodos, donde cada nodo apunta al siguiente

Características:
- Primer nodo se llama cabeza
- Cada nodo tiene un puntero al siguiete nodo
- Último nodo apunta a NULL
"""

class ListaSimpleEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo