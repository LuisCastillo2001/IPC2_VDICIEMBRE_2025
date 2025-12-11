from nodo import Nodo


class ColaUsuarios:
    """
    Clase que representa una Cola (FIFO - First In First Out)
    Los usuarios se atienden en el orden que llegan
    """
    
    def __init__(self):
        """Constructor de la cola"""
        self.primero = None
        self.tamanio = 0
    
    def esta_vacia(self):
        """
        Verifica si la cola está vacía
        
        Returns:
            bool: True si está vacía, False en caso contrario
        """
        return self.primero is None
    
    def enqueue(self, dato):
        """
        Encola un nuevo elemento al final de la cola
        
        Args:
            dato: Objeto Usuario a almacenar
        """
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            # Recorrer hasta el último nodo
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            
            # Enlazar el nuevo nodo al final
            actual.siguiente = nuevo_nodo
        
        self.tamanio += 1
        print(f"Usuario encolado: {dato}")
    
    def dequeue(self):
        """
        Desencola y retorna el primer elemento
        
        Returns:
            Usuario desencolado o None si está vacía
        """
        if self.esta_vacia():
            print("La cola esta vacia, no hay usuarios para atender")
            return None
        
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self.tamanio -= 1
        
        print(f"Usuario atendido: {dato}")
        return dato
    
    def peek(self):
        """
        Retorna el primer elemento sin desencolar
        
        Returns:
            Usuario al frente o None si está vacía
        """
        if self.esta_vacia():
            return None
        return self.primero.dato
    
    def mostrar(self):
        """Imprime todos los elementos de la cola"""
        if self.esta_vacia():
            print("La cola esta vacia")
            return
        
        print(f"\n--- Cola de Usuarios (Total: {self.tamanio}) ---")
        print("FRENTE")
        
        actual = self.primero
        posicion = 1
        while actual is not None:
            print(f"{posicion}. ", end="")
            actual.dato.mostrar_informacion()
            actual = actual.siguiente
            posicion += 1
        
        print("FINAL")
    
    def obtener_tamanio(self):
        """
        Retorna el tamaño de la cola
        
        Returns:
            int: Cantidad de elementos en la cola
        """
        return self.tamanio
