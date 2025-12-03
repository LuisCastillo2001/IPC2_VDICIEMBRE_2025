# Ejemplo Simple de POO: Clase Persona

## Descripción
Este es un ejemplo básico de Programación Orientada a Objetos (POO) en Python usando una clase `Persona`.
El objetivo es mostrar los conceptos fundamentales de POO de manera simple y clara.

## Conceptos de POO Demostrados

### 1. **Clase**
Una plantilla para crear objetos con atributos y métodos comunes.

```python
class Persona:
    # Definición de la clase
```

### 2. **Atributos**
Variables que almacenan el estado del objeto (características de la persona).
- `nombre`: Nombre de la persona
- `edad`: Edad de la persona
- `profesion`: Ocupación de la persona

### 3. **Métodos**
Funciones que definen el comportamiento del objeto (acciones que puede realizar).
- `presentarse()`: Muestra información de la persona
- `cumplir_anios()`: Incrementa la edad
- `cambiar_profesion()`: Actualiza la profesión
- `es_mayor_de_edad()`: Verifica si es mayor de 18 años

### 4. **Constructor (`__init__`)**
Método especial que se ejecuta al crear un objeto.

```python
def __init__(self, nombre, edad, profesion="Estudiante"):
    self.nombre = nombre
    self.edad = edad
    self.profesion = profesion
```

### 5. **`self`**
Referencia al objeto actual dentro de la clase.

### 6. **Instancias (Objetos)**
Cada objeto creado es una instancia independiente de la clase.

```python
persona1 = Persona("Ana García", 17)
persona2 = Persona("Carlos López", 25, "Ingeniero")
```

## Palabras Clave

| Palabra | Significado |
|---------|-------------|
| `class` | Define una clase |
| `__init__` | Constructor de la clase |
| `self` | Referencia al objeto actual |
| `def` | Define un método |
| Atributo | Variable de la clase que almacena datos |
| Método | Función de la clase que realiza acciones |
| Instancia | Objeto creado a partir de una clase |
| Objeto | Entidad con estado (atributos) y comportamiento (métodos) |



## Ejemplo de Salida

```
=== Ejemplo Simple de POO: Clase Persona ===

--- Presentaciones ---
Hola, mi nombre es Ana García, tengo 17 años y soy Estudiante.
Hola, mi nombre es Carlos López, tengo 25 años y soy Ingeniero.
Hola, mi nombre es María Rodríguez, tengo 30 años y soy Doctora.

--- Verificar mayoría de edad ---
Ana García es menor de edad.

--- Cumpleaños ---
¡Feliz cumpleaños Ana García! Ahora tienes 18 años.
¡Ahora Ana García es mayor de edad!

--- Cambio de profesión ---
Ana García cambió de Estudiante a Universitario.
Hola, mi nombre es Ana García, tengo 18 años y soy Universitario.
```


