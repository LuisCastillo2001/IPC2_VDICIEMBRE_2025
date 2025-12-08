class Nodo:
    """
    Clase que representa un nodo en una lista enlazada simple
    """
    
    def __init__(self, dato):
        """
        Constructor del nodo
        
        Args:
            dato: Información que almacena el nodo (puede ser cualquier objeto)
        """
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """
    Clase que representa una lista enlazada simple
    """
    
    def __init__(self):
        """Constructor de la lista enlazada"""
        self.primero = None
        self.tamanio = 0
    
    def esta_vacia(self):
        """
        Verifica si la lista está vacía
        
        Returns:
            bool: True si está vacía, False en caso contrario
        """
        return self.primero is None
    
    def agregar(self, dato):
        """
        Agrega un nuevo elemento al final de la lista
        
        Args:
            dato: Información a almacenar en el nuevo nodo
        """
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        
        self.tamanio += 1
    
    def mostrar(self):
        """Imprime todos los elementos de la lista"""
        if self.esta_vacia():
            print("La lista está vacía")
            return
        
        actual = self.primero
        while actual is not None:
            if hasattr(actual.dato, 'mostrar_informacion'):
                actual.dato.mostrar_informacion()
            else:
                print(actual.dato)
            actual = actual.siguiente
    
    def buscar_por_id(self, id_buscado, atributo_id='id_centro'):
        """
        Busca un elemento por su ID
        
        Args:
            id_buscado (str): ID a buscar
            atributo_id (str): Nombre del atributo que contiene el ID
            
        Returns:
            El dato encontrado o None si no existe
        """
        actual = self.primero
        while actual is not None:
            if hasattr(actual.dato, atributo_id):
                if getattr(actual.dato, atributo_id) == id_buscado:
                    return actual.dato
            actual = actual.siguiente
        return None
    
    def obtener_tamanio(self):
        """
        Retorna el tamaño de la lista
        
        Returns:
            int: Cantidad de elementos en la lista
        """
        return self.tamanio
    
    def eliminar_por_id(self, id_buscado, atributo_id='id_centro'):
        """
        Elimina un elemento de la lista por su ID
        
        Args:
            id_buscado (str): ID del elemento a eliminar
            atributo_id (str): Nombre del atributo que contiene el ID
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        if self.esta_vacia():
            print("La lista está vacía, no hay nada que eliminar.")
            return False
        
        # Caso 1: El elemento a eliminar es el primero
        if hasattr(self.primero.dato, atributo_id):
            if getattr(self.primero.dato, atributo_id) == id_buscado:
                elemento_eliminado = self.primero.dato
                self.primero = self.primero.siguiente
                self.tamanio -= 1
                print(f"Elemento eliminado: {elemento_eliminado}")
                return True
        
        # Caso 2: El elemento está en medio o al final
        actual = self.primero
        while actual.siguiente is not None:
            if hasattr(actual.siguiente.dato, atributo_id):
                if getattr(actual.siguiente.dato, atributo_id) == id_buscado:
                    elemento_eliminado = actual.siguiente.dato
                    actual.siguiente = actual.siguiente.siguiente
                    self.tamanio -= 1
                    print(f"Elemento eliminado: {elemento_eliminado}")
                    return True
            actual = actual.siguiente
        
        print(f"No se encontró ningún elemento con ID: {id_buscado}")
        return False
