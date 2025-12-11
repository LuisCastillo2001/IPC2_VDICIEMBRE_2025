class Libro:
    """
    Clase que representa un libro con su información básica
    """
    
    def __init__(self, codigo, titulo, autor, anio):
        """
        Constructor de la clase Libro
        
        Args:
            codigo (str): Código único del libro
            titulo (str): Título del libro
            autor (str): Autor del libro
            anio (str): Año de publicación
        """
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    
    def mostrar_informacion(self):
        """Imprime la información completa del libro"""
        print(f"\nCódigo: {self.codigo}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")
    
    def __str__(self):
        """Representación en string del objeto"""
        return f"Libro[{self.codigo}] - {self.titulo} ({self.autor})"
