# Sistema de Biblioteca con Pilas y Colas

## Descripción
Este ejemplo demuestra el uso de **Pilas (Stack)** y **Colas (Queue)** en Python mediante un sistema de gestión de biblioteca.

- **Pila (LIFO)**: Gestiona libros que llegan al mostrador. El último libro en llegar es el primero en procesarse.
- **Cola (FIFO)**: Gestiona usuarios que esperan ser atendidos. El primero en llegar es el primero en ser atendido.

## Conceptos Demostrados

### 1. **Pila (Stack) - LIFO**
Last In, First Out (Último en entrar, Primero en salir)

**Operaciones principales:**
- `push(dato)`: Agrega elemento al tope
- `pop()`: Remueve y retorna el elemento del tope
- `peek()`: Consulta el tope sin remover
- `esta_vacia()`: Verifica si está vacía
- `mostrar()`: Imprime todos los elementos

**Analogía**: Una pila de platos. Solo puedes tomar el de arriba.

### 2. **Cola (Queue) - FIFO**
First In, First Out (Primero en entrar, Primero en salir)

**Operaciones principales:**
- `enqueue(dato)`: Agrega elemento al final
- `dequeue()`: Remueve y retorna el primer elemento
- `peek()`: Consulta el frente sin remover
- `esta_vacia()`: Verifica si está vacía
- `mostrar()`: Imprime todos los elementos

**Analogía**: Una fila en un banco. El primero en llegar es el primero en ser atendido.

## Estructura del Proyecto

```
Clase 8/
├── nodo.py                 # Clase Nodo básica
├── libro.py                # Clase Libro
├── usuario.py              # Clase Usuario
├── pila_libros.py          # Implementación de Pila
├── cola_usuarios.py        # Implementación de Cola
├── Clase8.py               # Programa principal
└── README.md               # Este archivo
```

## Palabras Clave

| Palabra | Significado |
|---------|-------------|
| `Pila / Stack` | Estructura LIFO (Último en entrar, Primero en salir) |
| `Cola / Queue` | Estructura FIFO (Primero en entrar, Primero en salir) |
| `push` | Agregar elemento al tope de la pila |
| `pop` | Remover elemento del tope de la pila |
| `enqueue` | Agregar elemento al final de la cola |
| `dequeue` | Remover elemento del frente de la cola |
| `peek` | Ver el primer elemento sin removerlo |
| `tope` | Elemento superior de la pila |
| `frente` | Primer elemento de la cola |
| `LIFO` | Last In First Out |
| `FIFO` | First In First Out |

## Casos de Uso

### Pilas (LIFO)
- Historial de navegación (botón "Atrás")
- Pila de llamadas en recursión
- Deshacer/Rehacer en editores
- Procesamiento de expresiones matemáticas

### Colas (FIFO)
- Sistemas de atención al cliente
- Cola de impresión
- Procesamiento de tareas en segundo plano
- Buffer de datos

## Ejemplo de Salida

```
=== BIENVENIDO AL SISTEMA DE BIBLIOTECA ===

--- Cargando libros de ejemplo ---
Libro apilado: Libro[LIB001] - Cien anios de soledad (Gabriel Garcia Marquez)
Libro apilado: Libro[LIB002] - Don Quijote de la Mancha (Miguel de Cervantes)
Libro apilado: Libro[LIB003] - 1984 (George Orwell)

--- Cargando usuarios de ejemplo ---
Usuario encolado: Usuario[U001] - Maria Lopez (Prestamo)
Usuario encolado: Usuario[U002] - Carlos Hernandez (Devolucion)
Usuario encolado: Usuario[U003] - Ana Martinez (Consulta)

--- PILA DE LIBROS (LIFO) ---
TOPE
1. 1984 (George Orwell)
2. Don Quijote de la Mancha (Miguel de Cervantes)
3. Cien anios de soledad (Gabriel Garcia Marquez)

--- COLA DE USUARIOS (FIFO) ---
FRENTE
1. Maria Lopez (Prestamo)
2. Carlos Hernandez (Devolucion)
3. Ana Martinez (Consulta)
FINAL
```

## Diferencias Clave

| Característica | Pila (Stack) | Cola (Queue) |
|----------------|--------------|--------------|
| Orden | LIFO | FIFO |
| Inserción | Por el tope (push) | Por el final (enqueue) |
| Eliminación | Por el tope (pop) | Por el frente (dequeue) |
| Acceso | Solo al tope (peek) | Solo al frente (peek) |
| Uso típico | Deshacer/Volver | Turnos/Orden de llegada |

## Complejidad Temporal

Todas las operaciones principales tienen complejidad **O(1)**:
- push / enqueue: O(1)
- pop / dequeue: O(1)
- peek: O(1)
- esta_vacia: O(1)

## Cómo Ejecutar

```bash
python Clase8.py
```
