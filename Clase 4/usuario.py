class Usuario:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        
        
class Nodo:
    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente
        
class ListaEnlazada:
    def __init__(self):
        self.head = None
        
    def insertar(self, nombre, carrera):
        
        if self.head == None:
            self.head = Nodo(Usuario(nombre, carrera))
            return
        
        nodo_aux = self.head
        
        while nodo_aux.siguiente is not None:
            nodo_aux = nodo_aux.siguiente
        
        
        nodo_aux.siguiente = Nodo(Usuario(nombre, carrera))
        
    def recorrer(self):
        nodo_aux = self.head
        while nodo_aux is not None:
            print(f'Nombre: {nodo_aux.dato.nombre}, Carrera: {nodo_aux.dato.carrera}')
            nodo_aux = nodo_aux.siguiente
        