class Usuario:
    """
    Clase que representa un usuario de la biblioteca
    """
    
    def __init__(self, id_usuario, nombre, carrera, turno):
        """
        Constructor de la clase Usuario
        
        Args:
            id_usuario (str): Identificador único del usuario
            nombre (str): Nombre completo del usuario
            carrera (str): Carrera que estudia
            turno (str): Tipo de servicio solicitado
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.carrera = carrera
        self.turno = turno
    
    def mostrar_informacion(self):
        """Imprime la información completa del usuario"""
        print(f"\nID: {self.id_usuario}")
        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print(f"Servicio: {self.turno}")
    
    def __str__(self):
        """Representación en string del objeto"""
        return f"Usuario[{self.id_usuario}] - {self.nombre} ({self.turno})"
