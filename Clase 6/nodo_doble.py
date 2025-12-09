class NodoDoble:
    """
    Clase que representa un nodo en una lista doblemente enlazada
    """
    
    def __init__(self, dato):
        """
        Constructor del nodo doble
        
        Args:
            dato: Información que almacena el nodo (puede ser cualquier objeto)
        """
        self.dato = dato
        self.siguiente = None
        self.anterior = None
