from libro import Libro
from usuario import Usuario
from pila_libros import PilaLibros
from cola_usuarios import ColaUsuarios


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*60)
    print("  SISTEMA DE BIBLIOTECA - PILAS Y COLAS")
    print("="*60)
    print("PILAS (Libros en mostrador - LIFO)")
    print("  1. Push - Apilar libro")
    print("  2. Pop - Desapilar libro")
    print("  3. Peek - Ver libro en el tope")
    print("  4. Mostrar pila de libros")
    print("\nCOLAS (Usuarios en espera - FIFO)")
    print("  5. Enqueue - Encolar usuario")
    print("  6. Dequeue - Desencolar usuario")
    print("  7. Peek - Ver siguiente usuario")
    print("  8. Mostrar cola de usuarios")
    print("\n  9. Salir")
    print("="*60)


def agregar_libro(pila):
    """Agrega un nuevo libro a la pila"""
    print("\n--- Apilar nuevo libro ---")
    codigo = input("Codigo del libro: ").strip()
    titulo = input("Titulo: ").strip()
    autor = input("Autor: ").strip()
    anio = input("Anio de publicacion: ").strip()
    
    libro = Libro(codigo, titulo, autor, anio)
    pila.push(libro)


def agregar_usuario(cola):
    """Agrega un nuevo usuario a la cola"""
    print("\n--- Encolar nuevo usuario ---")
    id_usuario = input("ID del usuario: ").strip()
    nombre = input("Nombre completo: ").strip()
    carrera = input("Carrera: ").strip()
    turno = input("Servicio solicitado: ").strip()
    
    usuario = Usuario(id_usuario, nombre, carrera, turno)
    cola.enqueue(usuario)


def procesar_libro(pila):
    """Desapila y procesa un libro"""
    print("\n--- Procesar libro del tope ---")
    libro = pila.pop()
    if libro:
        print("\nLibro procesado correctamente")


def atender_usuario(cola):
    """Desencola y atiende al siguiente usuario"""
    print("\n--- Atender siguiente usuario ---")
    usuario = cola.dequeue()
    if usuario:
        print("\nUsuario atendido correctamente")


def ver_tope_pila(pila):
    """Muestra el libro en el tope sin desapilar"""
    libro = pila.peek()
    if libro:
        print("\n--- Libro en el tope ---")
        libro.mostrar_informacion()
    else:
        print("\nLa pila esta vacia")


def ver_frente_cola(cola):
    """Muestra el usuario al frente sin desencolar"""
    usuario = cola.peek()
    if usuario:
        print("\n--- Siguiente usuario a atender ---")
        usuario.mostrar_informacion()
    else:
        print("\nLa cola esta vacia")


def cargar_datos_iniciales():
    """Carga algunos datos de ejemplo"""
    pila = PilaLibros()
    cola = ColaUsuarios()
    
    # Datos de ejemplo para la pila
    print("\n--- Cargando libros de ejemplo ---")
    pila.push(Libro("LIB001", "Cien anios de soledad", "Gabriel Garcia Marquez", "1967"))
    pila.push(Libro("LIB002", "Don Quijote de la Mancha", "Miguel de Cervantes", "1605"))
    pila.push(Libro("LIB003", "1984", "George Orwell", "1949"))
    
    # Datos de ejemplo para la cola
    print("\n--- Cargando usuarios de ejemplo ---")
    cola.enqueue(Usuario("U001", "Maria Lopez", "Ingenieria en Sistemas", "Prestamo"))
    cola.enqueue(Usuario("U002", "Carlos Hernandez", "Ingenieria Civil", "Devolucion"))
    cola.enqueue(Usuario("U003", "Ana Martinez", "Arquitectura", "Consulta"))
    
    return pila, cola


def main():
    """Función principal del programa"""
    print("\n" + "="*60)
    print("  BIENVENIDO AL SISTEMA DE BIBLIOTECA")
    print("="*60)
    
    # Cargar datos iniciales
    pila_libros, cola_usuarios = cargar_datos_iniciales()
    
    print(f"\nPila de libros inicializada: {pila_libros.tamanio} libros")
    print(f"Cola de usuarios inicializada: {cola_usuarios.tamanio} usuarios")
    
    # Menú principal
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                agregar_libro(pila_libros)
                
            elif opcion == "2":
                procesar_libro(pila_libros)
                
            elif opcion == "3":
                ver_tope_pila(pila_libros)
                
            elif opcion == "4":
                pila_libros.mostrar()
                
            elif opcion == "5":
                agregar_usuario(cola_usuarios)
                
            elif opcion == "6":
                atender_usuario(cola_usuarios)
                
            elif opcion == "7":
                ver_frente_cola(cola_usuarios)
                
            elif opcion == "8":
                cola_usuarios.mostrar()
                
            elif opcion == "9":
                print("\n¡Hasta luego! 📚")
                break
                
            else:
                print("\n⚠ Opción no válida. Intente nuevamente.")
                
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
