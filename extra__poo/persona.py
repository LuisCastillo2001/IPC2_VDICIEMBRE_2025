class Persona:
    def __init__(self, nombre, edad, profesion="Estudiante"): 
        """
        Constructor de la clase Persona
        
        Args:
            nombre (str): Nombre de la persona
            edad (int): Edad de la persona
            profesion (str): Profesión u ocupación (por defecto: "Estudiante")
        """
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def presentarse(self):
        """Imprime una presentación de la persona"""
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}.")
    
    def cumplir_anios(self):
        """Incrementa la edad en 1 año"""
        self.edad += 1
        print(f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años.")
    
    def cambiar_profesion(self, nueva_profesion):
        """
        Cambia la profesión de la persona
        
        Args:
            nueva_profesion (str): Nueva profesión
        """
        print(f"{self.nombre} cambió de {self.profesion} a {nueva_profesion}.")
        self.profesion = nueva_profesion
    
    def es_mayor_de_edad(self):
        """
        Verifica si la persona es mayor de edad
        
        Returns:
            bool: True si es mayor de edad, False en caso contrario
        """
        return self.edad >= 18


# Programa principal
def main():
    print("=== Ejemplo Simple de POO: Clase Persona ===\n")
    
    # Crear objetos (instancias) de la clase Persona
    persona1 = Persona("Ana García", 17)
    persona2 = Persona("Carlos López", 25, "Ingeniero")
    persona3 = Persona("María Rodríguez", 30, "Doctora")
    
    # Usar métodos de los objetos
    print("--- Presentaciones ---")
    persona1.presentarse()
    persona2.presentarse()
    persona3.presentarse()
    
    print("\n--- Verificar mayoría de edad ---")
    if persona1.es_mayor_de_edad():
        print(f"{persona1.nombre} es mayor de edad.")
    else:
        print(f"{persona1.nombre} es menor de edad.")
    
    print("\n--- Cumpleaños ---")
    persona1.cumplir_anios()
    
    if persona1.es_mayor_de_edad():
        print(f"¡Ahora {persona1.nombre} es mayor de edad!")
    
    print("\n--- Cambio de profesión ---")
    persona1.cambiar_profesion("Universitario")
    persona1.presentarse()
    
    print("\n--- Lista de personas ---")
    personas = [persona1, persona2, persona3]
    for p in personas:
        print(f"{p.nombre} - {p.edad} años - {p.profesion}")


if __name__ == "__main__":
    main()
