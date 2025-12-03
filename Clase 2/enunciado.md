# Sistema de Estacionamiento y Consumo de Combustible - Ejemplo POO en Python

## Descripción
Se desarrollará un sistema para gestionar distintos vehículos dentro de un estacionamiento.
Cada vehículo registra su placa, tipo, tiempo de estacionamiento y nivel de combustible.
Dependiendo del tipo de vehículo, su pago por minuto y consumo de combustible serán distintos.

## Pilares de POO utilizados
- **Abstracción** → Clase abstracta `Vehiculo`
- **Herencia** → Clases hijas `Carro`, `Moto`, `Camion`
- **Encapsulación** → `__combustible`, `__placa` protegidos con `@property`
- **Polimorfismo** → Cada clase implementa su versión de `calcular_pago()` y `mover()`

## Palabras clave y significado
| Palabra | Significado |
|--------|-------------|
| `class` | Define una clase en Python |
| `__init__` | Constructor (se ejecuta al crear el objeto) |
| `self` | Referencia al propio objeto dentro de la clase |
| `super()` | Llama métodos y atributos de la clase padre |
| `ABC` | Permite crear clases abstractas |
| `@abstractmethod` | Método que debe ser implementado por subclases |
| `@property` | Permite acceso controlado a atributos privados |
| `__atributo` | Indica atributo privado (encapsulación) |
| Polimorfismo | Método con mismo nombre, distinto comportamiento |
| Instancia | Un objeto creado a partir de una clase |

---
