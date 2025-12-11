class Nodo:
    """
    Clase que representa un nodo en una estructura de datos lineal
    """
    
    def __init__(self, dato):
        """
        Constructor del nodo
        
        Args:
            dato: Información que almacena el nodo (puede ser cualquier objeto)
        """
        self.dato = dato
        self.siguiente = None
