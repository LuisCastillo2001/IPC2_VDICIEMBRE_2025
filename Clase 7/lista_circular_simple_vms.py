from nodo_simple import NodoSimple


class ListaCircularSimpleVMs:
    """
    Clase que representa una lista simplemente enlazada circular para Máquinas Virtuales
    """
    
    def __init__(self):
        """Constructor de la lista circular simple"""
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
        Agrega un nuevo elemento al final de la lista circular
        
        Args:
            dato: Objeto MaquinaVirtual a almacenar
        """
        nuevo_nodo = NodoSimple(dato)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero  # Apunta a sí mismo
        else:
            # Recorrer hasta el último nodo (el que apunta al primero)
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            
            # Enlazar el nuevo nodo al final y cerrar el círculo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        
        self.tamanio += 1
    
    def agregar_al_inicio(self, dato):
        """
        Agrega un nuevo elemento al inicio de la lista circular
        
        Args:
            dato: Objeto MaquinaVirtual a almacenar
        """
        nuevo_nodo = NodoSimple(dato)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
        else:
            # Encontrar el último nodo
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            
            # Insertar al inicio
            nuevo_nodo.siguiente = self.primero
            actual.siguiente = nuevo_nodo
            self.primero = nuevo_nodo
        
        self.tamanio += 1
    
    def mostrar(self):
        """Imprime todos los elementos de la lista circular"""
        if self.esta_vacia():
            print("La lista está vacía")
            return

        actual = self.primero
        while True:
            actual.dato.mostrar_informacion()
            actual = actual.siguiente
            if actual == self.primero:
                break

    def buscar_por_id(self, id_buscado):
        """
        Busca una máquina virtual por su ID
        
        Args:
            id_buscado (str): ID a buscar
            
        Returns:
            MaquinaVirtual encontrada o None si no existe
        """
        if self.esta_vacia():
            return None

        actual = self.primero
        while True:
            if actual.dato.id_vm == id_buscado:
                return actual.dato
            actual = actual.siguiente
            if actual == self.primero:
                break
        return None
    
    def eliminar_por_id(self, id_buscado):
        """
        Elimina una máquina virtual de la lista circular por su ID

        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        if self.esta_vacia():
            print("La lista está vacía, no hay nada que eliminar.")
            return False

        # Caso 1: Único elemento
        if self.tamanio == 1:
            if self.primero.dato.id_vm == id_buscado:
                print(f"Máquina virtual eliminada: {self.primero.dato}")
                self.primero = None
                self.tamanio = 0
                return True
            print(f"No se encontró ninguna VM con ID: {id_buscado}")
            return False

        # Caso 2: El primero (pero hay más)
        if self.primero.dato.id_vm == id_buscado:
            # Encontrar el último para mantener circularidad
            ultimo = self.primero
            while ultimo.siguiente != self.primero:
                ultimo = ultimo.siguiente
            print(f"Máquina virtual eliminada: {self.primero.dato}")
            self.primero = self.primero.siguiente
            ultimo.siguiente = self.primero
            self.tamanio -= 1
            return True

        # Caso 3: Medio o final 
        #  
        actual = self.primero
        while True:
            if actual.siguiente.dato.id_vm == id_buscado:
                print(f"Máquina virtual eliminada: {actual.siguiente.dato}")
                actual.siguiente = actual.siguiente.siguiente
                self.tamanio -= 1
                return True
            actual = actual.siguiente
            if actual == self.primero:
                break

        print(f"No se encontró ninguna VM con ID: {id_buscado}")
        return False
    
    def obtener_tamanio(self):
        """
        Retorna el tamaño de la lista
        
        Returns:
            int: Cantidad de elementos en la lista
        """
        return self.tamanio
