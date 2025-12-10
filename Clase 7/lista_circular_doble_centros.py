from nodo_doble import NodoDoble


class ListaCircularDobleCentros:
    """
    Clase que representa una lista doblemente enlazada circular para Centros de Datos
    """
    
    def __init__(self):
        """Constructor de la lista circular doble"""
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
        Agrega un nuevo elemento al final de la lista circular doble
        
        Args:
            dato: Objeto CentroDatos a almacenar
        """
        nuevo_nodo = NodoDoble(dato)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        else:
            # Recorrer hasta el último nodo (el anterior al primero)
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            
            # Insertar al final y mantener la circularidad
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
        
        self.tamanio += 1
    
    def agregar_al_inicio(self, dato):
        """
        Agrega un nuevo elemento al inicio de la lista circular doble
        
        Args:
            dato: Objeto CentroDatos a almacenar
        """
        nuevo_nodo = NodoDoble(dato)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        else:
            ultimo = self.primero.anterior
            
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = ultimo
            self.primero.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo
            self.primero = nuevo_nodo
        
        self.tamanio += 1
    
    def mostrar(self):
        """Imprime todos los elementos de la lista circular doble"""
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
        Busca un centro de datos por su ID
        
        Args:
            id_buscado (str): ID a buscar
            
        Returns:
            CentroDatos encontrado o None si no existe
        """
        if self.esta_vacia():
            return None

        actual = self.primero
        while True:
            if actual.dato.id_centro == id_buscado:
                return actual.dato
            actual = actual.siguiente
            if actual == self.primero:
                break
        return None

    def eliminar_por_id(self, id_buscado):
        """
        Elimina un centro de datos de la lista circular doble por su ID
        
        Args:
            id_buscado (str): ID del elemento a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        if self.esta_vacia():
            print("La lista está vacía, no hay nada que eliminar.")
            return False

        actual = self.primero
        while True:
            if actual.dato.id_centro == id_buscado:
                # Caso 1: Es el único elemento
                if self.tamanio == 1:
                    self.primero = None

                # Caso 2: Es el primer elemento (pero hay más)
                elif actual == self.primero:
                    ultimo = self.primero.anterior
                    self.primero = actual.siguiente
                    self.primero.anterior = ultimo
                    ultimo.siguiente = self.primero

                # Caso 3: Es el último elemento (anterior al primero)
                elif actual == self.primero.anterior:
                    nuevo_ultimo = actual.anterior
                    nuevo_ultimo.siguiente = self.primero
                    self.primero.anterior = nuevo_ultimo

                # Caso 4: Está en medio
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior

                self.tamanio -= 1
                print(f"Centro de datos eliminado: {actual.dato}")
                return True

            actual = actual.siguiente
            if actual == self.primero:
                break

        print(f"No se encontró ningún centro con ID: {id_buscado}")
        return False
    
    def obtener_tamanio(self):
        """
        Retorna el tamaño de la lista
        
        Returns:
            int: Cantidad de elementos en la lista
        """
        return self.tamanio
