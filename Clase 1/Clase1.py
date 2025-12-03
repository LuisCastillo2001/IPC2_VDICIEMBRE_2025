

# -----------------------
# FUNCIONES DE VALIDACIÓN
# -----------------------

def leer_entero_positivo(mensaje):
    """Lee un entero positivo validado."""
    valor = input(mensaje)

    while not valor.isdigit():  # validación simple
        print("Error: Debes ingresar un número entero positivo.")
        valor = input(mensaje)

    return int(valor)


def leer_opcion_si_no(mensaje):
    """Lee un 's' o 'n' validado."""
    opcion = input(mensaje).lower()

    while opcion != "s" and opcion != "n":
        print("Error: Solo se acepta 's' o 'n'.")
        opcion = input(mensaje).lower()

    return opcion


# -----------------------
# FUNCIONES LÓGICAS
# -----------------------

def calcular_anio_nacimiento(edad, anio_actual):
    """Devuelve el año de nacimiento estimado."""
    return anio_actual - edad


def clasificar_edad(edad):
    """Retorna un texto que describe la etapa de vida."""
    if edad < 18:
        return "Menor de edad"
    elif edad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"


def es_par(numero):
    """Retorna True si el número es par."""
    return numero % 2 == 0


# -----------------------
# PROGRAMA PRINCIPAL
# -----------------------

print("=== SISTEMA DE INFORMACIÓN PERSONAL ===\n")

# Input del usuario
nombre = input("Ingresa tu nombre: ")

# Validación usando una función
edad = leer_entero_positivo("Ingresa tu edad: ")

# Casteo a str (para cumplir con la presentación)
nombre = str(nombre)

# Operaciones aritméticas
anio_actual = 2025
nacimiento = calcular_anio_nacimiento(edad, anio_actual)

print("\nResumen inicial:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Año estimado de nacimiento:", nacimiento)

# Clasificación por edad
categoria = clasificar_edad(edad)
print("Clasificación:", categoria)

# Input validado sí/no
tiene_identificacion = leer_opcion_si_no("¿Tienes DPI? (s/n): ")

# Expresiones lógicas
if tiene_identificacion == "s" and edad >= 18:
    print("Acceso permitido")
else:
    print("Acceso denegado")

# Ciclo while
print("\nCuenta regresiva:")
contador = 3
while contador > 0:
    print("Faltan:", contador)
    contador -= 1

# Ciclo for
print("\nRepetición usando for:")
for i in range(1, 4):
    print("Iteración", i)

# Comprobación par/impar
print("\nVerificando tu edad...")
if es_par(edad):
    print("Tu edad es PAR")
else:
    print("Tu edad es IMPAR")

print("\n=== FIN DEL PROGRAMA ===")
