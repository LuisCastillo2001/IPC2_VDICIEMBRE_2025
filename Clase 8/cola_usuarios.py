from nodo import Nodo
from usuario import Usuario
import time

class ColaUsuarios:
    
    
    def __init__(self):
        
        self.primero = None
        self.tamanio = 0
        
    
    def esta_vacia(self):
        
        return self.primero is None
    
    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.primero = nuevo_nodo
            
        else:
            
            actual = self.primero
            
            while actual.siguiente is not None:
                actual = actual.siguiente
                
           # Enlazar el nuevo nodo al final
           
            actual.siguiente = nuevo_nodo  
            
        self.tamanio += 1
        
        # print("Usuario encolado : {dato}")
        
        
    def dequeue(self):
        
        if self.esta_vacia():
            print("La cola esta vacia, no hay usuarios para atender")
            return None
    
        
        dato = self.primero.dato # solo para hacer el print
        
        self.primero = self.primero.siguiente 
        self.tamanio -=1
        
        print("Usuario atendido")
        return dato
    
    
    def peek(self):
        
        if self.esta_vacia():
            return None
        
        return self.primero.dato 
    
    def mostrar(self):
        
        if self.esta_vacia():
            print("La cola esta vacia")
            
            return
        
        print("Cola de usuarios")
        
        actual = self.primero
        
        posicion = 1
        
        while actual is not None:
            actual.dato.mostrar_informacion()
            actual = actual.siguiente
            
        
        
    def obtener_tamanio(self):
        return self.tamanio
    
    def metodo_atender_grupos(self, n):
        
        contador = 0
        
        while contador < n:
            self.dequeue()
            contador += 1
            
        
            
    
    
    
    


usuario1 = Usuario("ID001", "Luis", "Ingeniería", "Atención")
usuario2 = Usuario("ID002", "Ana", "Industrial", "Atencion")
usuario3 = Usuario("ID003", "Juan", "Medicina", "Atencion")


cola = ColaUsuarios()



cola.enqueue(usuario1)
cola.enqueue(usuario2)
cola.enqueue(usuario3)

cola.metodo_atender_grupos(3)

cola.mostrar()



                