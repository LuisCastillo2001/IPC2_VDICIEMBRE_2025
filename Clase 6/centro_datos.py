class CentroDatos:
    """
    Clase que representa un centro de datos con su información completa
    """
    
    def __init__(self, id_centro, nombre, pais, ciudad, cpu, ram, almacenamiento):
        """
        Constructor de la clase CentroDatos
        
        Args:
            id_centro (str): Identificador único del centro
            nombre (str): Nombre del centro de datos
            pais (str): País donde se ubica
            ciudad (str): Ciudad donde se ubica
            cpu (str): Capacidad de CPU
            ram (str): Capacidad de RAM
            almacenamiento (str): Capacidad de almacenamiento
        """
        self.id_centro = id_centro
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
    
    def mostrar_informacion(self):
        """Imprime la información completa del centro de datos"""
        print(f"\nID: {self.id_centro}")
        print(f"Nombre: {self.nombre}")
        print(f"Ubicación: {self.ciudad}, {self.pais}")
        print(f"Capacidad -> CPU: {self.cpu}, RAM: {self.ram}, Almacenamiento: {self.almacenamiento}")
    
    def __str__(self):
        """Representación en string del objeto"""
        return f"Centro[{self.id_centro}] - {self.nombre} ({self.ciudad})"
