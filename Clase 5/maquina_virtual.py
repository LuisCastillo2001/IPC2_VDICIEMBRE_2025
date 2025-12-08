class MaquinaVirtual:
    """
    Clase que representa una máquina virtual con sus recursos y configuración
    """
    
    def __init__(self, id_vm, centro_asignado, sistema_operativo, cpu, ram, almacenamiento, ip):
        """
        Constructor de la clase MaquinaVirtual
        
        Args:
            id_vm (str): Identificador único de la VM
            centro_asignado (str): ID del centro de datos asignado
            sistema_operativo (str): Sistema operativo de la VM
            cpu (str): Recursos de CPU asignados
            ram (str): Recursos de RAM asignados
            almacenamiento (str): Almacenamiento asignado
            ip (str): Dirección IP de la VM
        """
        self.id_vm = id_vm
        self.centro_asignado = centro_asignado
        self.sistema_operativo = sistema_operativo
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.ip = ip
    
    def mostrar_informacion(self):
        """Imprime la información completa de la máquina virtual"""
        print(f"\nID VM: {self.id_vm}")
        print(f"Centro asignado: {self.centro_asignado}")
        print(f"Sistema operativo: {self.sistema_operativo}")
        print(f"Recursos -> CPU: {self.cpu}, RAM: {self.ram}, Almacenamiento: {self.almacenamiento}")
        print(f"IP: {self.ip}")
    
    def __str__(self):
        """Representación en string del objeto"""
        return f"VM[{self.id_vm}] - {self.sistema_operativo} @ {self.ip}"
