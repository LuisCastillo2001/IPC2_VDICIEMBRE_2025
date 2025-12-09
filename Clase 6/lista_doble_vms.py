from nodo_doble import NodoDoble
import os


class ListaDobleVMs:
    """
    Clase que representa una lista doblemente enlazada para Máquinas Virtuales
    """
    
    def __init__(self):
        """Constructor de la lista doblemente enlazada"""
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
            dato: Objeto MaquinaVirtual a almacenar
        """
        nuevo_nodo = NodoDoble(dato)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            # Recorrer hasta el último nodo
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            
            # Enlazar el nuevo nodo al final
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
        
        self.tamanio += 1
    
    def agregar_al_inicio(self, dato):
        """
        Agrega un nuevo elemento al inicio de la lista
        
        Args:
            dato: Objeto MaquinaVirtual a almacenar
        """
        nuevo_nodo = NodoDoble(dato)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
        
        self.tamanio += 1
    
    def mostrar(self):
        """Imprime todos los elementos de la lista de inicio a fin"""
        if self.esta_vacia():
            print("La lista está vacía")
            return
        
        actual = self.primero
        while actual is not None:
            actual.dato.mostrar_informacion()
            actual = actual.siguiente
    
    def buscar_por_id(self, id_buscado):
        """
        Busca una máquina virtual por su ID
        
        Args:
            id_buscado (str): ID a buscar
            
        Returns:
            MaquinaVirtual encontrada o None si no existe
        """
        actual = self.primero
        while actual is not None:
            if actual.dato.id_vm == id_buscado:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def eliminar_por_id(self, id_buscado):
        """
        Elimina una máquina virtual de la lista por su ID
        
        Args:
            id_buscado (str): ID del elemento a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        if self.esta_vacia():
            print("La lista está vacía, no hay nada que eliminar.")
            return False
        
        actual = self.primero
        
        while actual is not None:
            if actual.dato.id_vm == id_buscado:
                # Caso 1: Es el único elemento
                if actual.anterior is None and actual.siguiente is None:
                    self.primero = None
                
                # Caso 2: Es el primer elemento (pero hay más)
                elif actual.anterior is None:
                    self.primero = actual.siguiente
                    self.primero.anterior = None
                
                # Caso 3: Es el último elemento
                elif actual.siguiente is None:
                    actual.anterior.siguiente = None
                
                # Caso 4: Está en medio
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                
                self.tamanio -= 1
                print(f"Máquina virtual eliminada: {actual.dato}")
                return True
            
            actual = actual.siguiente
        
        print(f"No se encontró ninguna VM con ID: {id_buscado}")
        return False
    
    def obtener_tamanio(self):
        """
        Retorna el tamaño de la lista
        
        Returns:
            int: Cantidad de elementos en la lista
        """
        return self.tamanio
    
    def graficar(self, nombre_archivo="lista_vms"):
        """
        Genera un archivo DOT para visualizar la lista con Graphviz y crea el PNG
        
        Args:
            nombre_archivo (str): Nombre del archivo sin extensión
        """
        if self.esta_vacia():
            print("No se puede graficar una lista vacía")
            return
        
        dot_content = 'digraph ListaDobleVMs {\n'
        dot_content += '    rankdir=LR;\n'
        dot_content += '    node [shape=record];\n\n'
        
        # Generar nodos
        actual = self.primero
        contador = 0
        
        while actual is not None:
            label = f"{actual.dato.id_vm}|{actual.dato.sistema_operativo}|{actual.dato.ip}"
            dot_content += f'    nodo{contador} [label="{label}"];\n'
            actual = actual.siguiente
            contador += 1
        
        dot_content += '\n'
        
        # Generar conexiones bidireccionales
        for i in range(contador - 1):
            dot_content += f'    nodo{i} -> nodo{i+1} [dir=both];\n'
        
        dot_content += '}\n'
        
        # Guardar archivo DOT
        ruta_dot = f'Clase 6\\{nombre_archivo}.dot'
        with open(ruta_dot, 'w', encoding='utf-8') as archivo:
            archivo.write(dot_content)
        
        print(f"\n✓ Archivo '{nombre_archivo}.dot' generado exitosamente")
        
        # Generar PNG automáticamente
        ruta_png = f'Clase 6\\{nombre_archivo}.png'
        resultado = os.system(f'dot -Tpng "{ruta_dot}" -o "{ruta_png}"')
        
        if resultado == 0:
            print(f"Imagen '{nombre_archivo}.png' generada exitosamente")
        else:
            print(f"No se pudo generar el PNG. Asegúrate de tener Graphviz instalado.")
            print(f"  Ejecuta manualmente: dot -Tpng \"{ruta_dot}\" -o \"{ruta_png}\"")
