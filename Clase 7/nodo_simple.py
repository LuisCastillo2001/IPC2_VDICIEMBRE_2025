class NodoSimple:
    """
    Clase que representa un nodo en una lista simplemente enlazada circular
    """
    
    def __init__(self, dato):
        """
        Constructor del nodo simple
        
        Args:
            dato: Información que almacena el nodo (puede ser cualquier objeto)
        """
        self.dato = dato
        self.siguiente = None
