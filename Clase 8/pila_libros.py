from nodo import Nodo


class PilaLibros:
    """
    Clase que representa una Pila (LIFO - Last In First Out)
    Los libros que llegan al mostrador se procesan en orden inverso
    """
    
    def __init__(self):
        """Constructor de la pila"""
        self.tope = None
        self.tamanio = 0
    
    def esta_vacia(self):
        """
        Verifica si la pila está vacía
        
        Returns:
            bool: True si está vacía, False en caso contrario
        """
        return self.tope is None
    
    def push(self, dato):
        """
        Agrega un nuevo elemento al tope de la pila
        
        Args:
            dato: Objeto Libro a almacenar
        """
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.tope = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.tope
            self.tope = nuevo_nodo
        
        self.tamanio += 1
        print(f"Libro apilado: {dato}")
    
    def pop(self):
        """
        Desapila y retorna el elemento del tope
        
        Returns:
            Libro desapilado o None si está vacía
        """
        if self.esta_vacia():
            print("La pila esta vacia, no hay libros para procesar")
            return None
        
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        
        print(f"Libro procesado: {dato}")
        return dato
    
    def peek(self):
        """
        Retorna el elemento del tope sin desapilar
        
        Returns:
            Libro en el tope o None si está vacía
        """
        if self.esta_vacia():
            return None
        return self.tope.dato
    
    def mostrar(self):
        """Imprime todos los elementos de la pila"""
        if self.esta_vacia():
            print("La pila esta vacia")
            return
        
        print(f"\n--- Pila de Libros (Total: {self.tamanio}) ---")
        print("TOPE")
        
        actual = self.tope
        posicion = 1
        while actual is not None:
            print(f"{posicion}. ", end="")
            actual.dato.mostrar_informacion()
            actual = actual.siguiente
            posicion += 1
    
    def obtener_tamanio(self):
        """
        Retorna el tamaño de la pila
        
        Returns:
            int: Cantidad de elementos en la pila
        """
        return self.tamanio
