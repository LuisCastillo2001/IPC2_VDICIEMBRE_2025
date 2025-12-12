from nodo import Nodo
from libro import Libro

class PilaLibros:
    
    def __init__(self):
        
        self.tope = None # tope = cima = arriba
        self.tamanio = 0
        
    def esta_vacia(self):
        
        return self.tope is None
    
    def push(self,dato):
        
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.tope = nuevo_nodo
            
        else:
            nuevo_nodo.siguiente = self.tope
            self.tope = nuevo_nodo
    
        self.tamanio += 1
        print(f"Libro acoplado {dato}")
    
    
    def pop(self):
        
        if self.esta_vacia():
            print("La lista esta vacia")
            return None
        
    
        dato = self.tope.dato #solo para imprimir
        
        self.tope = self.tope.siguiente
        
        self.tamanio -= 1
        
        
        print(f"Libro procesado : {dato}")
        return dato
    
    
    def peek(self):
        
        if self.esta_vacia():
            return None
        
        return self.tope.dato
    
    
    def mostrar(self):
        
        if self.esta_vacia():
            print("La pila esta vacia")
            return
        
        print("------------Pila de libros------------")
        print("TOPE")
        
        actual = self.tope
        posicion = 1
        
        while actual is not None:
            
            actual.dato.mostrar_informacion()
            actual = actual.siguiente
            
            
    def obtener_tamanio(self):
        
        return self.tamanio
    
    
    


libro1 = Libro("001", "Cien Años de Soledad", "Gabriel García Márquez", "1967")
libro2 = Libro("002", "Don Quijote de la Mancha", "Miguel de Cervantes", "1605")
libro3 = Libro("003", "La Sombra del Viento", "Carlos Ruiz Zafón", "2001")

pila = PilaLibros()

pila.push(libro1)
pila.push(libro2)
pila.push(libro3)



print("Informacion: ")
print(pila.mostrar())

pila.pop()

print(pila.mostrar())



        