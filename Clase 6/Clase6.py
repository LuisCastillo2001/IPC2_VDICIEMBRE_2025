import xml.etree.ElementTree as ET
from centro_datos import CentroDatos
from maquina_virtual import MaquinaVirtual
from lista_doble_centros import ListaDobleCentros
from lista_doble_vms import ListaDobleVMs


def cargar_centros_datos(configuracion):
    """
    Carga los centros de datos del XML y los almacena en una lista doblemente enlazada
    
    Args:
        configuracion: Elemento XML con la configuración
        
    Returns:
        ListaDobleCentros: Lista con los centros de datos
    """
    lista_centros = ListaDobleCentros()
    
    for centro in configuracion.find("centrosDatos").findall("centro"):
        id_centro = centro.get("id")
        nombre = centro.get("nombre")
        
        ubicacion = centro.find("ubicacion")
        pais = ubicacion.find("pais").text
        ciudad = ubicacion.find("ciudad").text
        
        capacidad = centro.find("capacidad")
        cpu = capacidad.find("cpu").text
        ram = capacidad.find("ram").text
        almacenamiento = capacidad.find("almacenamiento").text
        
        # Crear objeto CentroDatos y agregarlo a la lista
        centro_obj = CentroDatos(id_centro, nombre, pais, ciudad, cpu, ram, almacenamiento)
        lista_centros.agregar(centro_obj)
    
    return lista_centros


def cargar_maquinas_virtuales(configuracion):
    """
    Carga las máquinas virtuales del XML y las almacena en una lista doblemente enlazada
    
    Args:
        configuracion: Elemento XML con la configuración
        
    Returns:
        ListaDobleVMs: Lista con las máquinas virtuales
    """
    lista_vms = ListaDobleVMs()
    
    for vm in configuracion.find("maquinasVirtuales").findall("vm"):
        id_vm = vm.get("id")
        centro = vm.get("centroAsignado")
        so = vm.find("sistemaOperativo").text
        
        recursos = vm.find("recursos")
        cpu = recursos.find("cpu").text
        ram = recursos.find("ram").text
        almacenamiento = recursos.find("almacenamiento").text
        
        ip = vm.find("ip").text
        
        # Crear objeto MaquinaVirtual y agregarlo a la lista
        vm_obj = MaquinaVirtual(id_vm, centro, so, cpu, ram, almacenamiento, ip)
        lista_vms.agregar(vm_obj)
    
    return lista_vms


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*60)
    print("  SISTEMA DE GESTIÓN - LISTAS DOBLEMENTE ENLAZADAS")
    print("="*60)
    print("1. Mostrar centros de datos")
    print("2. Mostrar máquinas virtuales")
    print("3. Buscar centro de datos por ID")
    print("4. Buscar máquina virtual por ID")
    print("5. Eliminar centro de datos por ID")
    print("6. Eliminar máquina virtual por ID")
    print("7. Graficar lista de centros de datos")
    print("8. Graficar lista de máquinas virtuales")
    print("9. Salir")
    print("="*60)


def buscar_centro(lista_centros):
    """Busca y muestra un centro de datos por su ID"""
    id_buscar = input("\nIngrese el ID del centro de datos a buscar: ").strip()
    centro = lista_centros.buscar_por_id(id_buscar)
    
    if centro:
        print("\n--- Centro de datos encontrado ---")
        centro.mostrar_informacion()
    else:
        print(f"\nNo se encontró ningún centro con ID: {id_buscar}")


def buscar_vm(lista_vms):
    """Busca y muestra una máquina virtual por su ID"""
    id_buscar = input("\nIngrese el ID de la máquina virtual a buscar: ").strip()
    vm = lista_vms.buscar_por_id(id_buscar)
    
    if vm:
        print("\n--- Máquina virtual encontrada ---")
        vm.mostrar_informacion()
    else:
        print(f"\nNo se encontró ninguna VM con ID: {id_buscar}")


def eliminar_centro(lista_centros):
    """Elimina un centro de datos por su ID"""
    id_eliminar = input("\nIngrese el ID del centro de datos a eliminar: ").strip()
    lista_centros.eliminar_por_id(id_eliminar)


def eliminar_vm(lista_vms):
    """Elimina una máquina virtual por su ID"""
    id_eliminar = input("\nIngrese el ID de la máquina virtual a eliminar: ").strip()
    lista_vms.eliminar_por_id(id_eliminar)


def main():
    """Función principal del programa"""
    # Cargar el archivo XML
    try:
        tree = ET.parse("Clase 6\\entrada.xml")
        root = tree.getroot()
        configuracion = root.find("configuracion")
        
        # Cargar datos en listas doblemente enlazadas
        lista_centros = cargar_centros_datos(configuracion)
        lista_vms = cargar_maquinas_virtuales(configuracion)
        
        print("\n¡Datos cargados exitosamente!")
        print(f"Centros de datos: {lista_centros.obtener_tamanio()}")
        print(f"Máquinas virtuales: {lista_vms.obtener_tamanio()}")
        
    except FileNotFoundError:
        print("\nError: No se encontró el archivo 'entrada.xml'")
        return
    except Exception as e:
        print(f"\nError al cargar el archivo: {e}")
        return
    
    # Menú principal
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                print("\n" + "="*60)
                print("         CENTROS DE DATOS")
                print("="*60)
                print(f"Total: {lista_centros.obtener_tamanio()}")
                lista_centros.mostrar()
                
            elif opcion == "2":
                print("\n" + "="*60)
                print("         MÁQUINAS VIRTUALES")
                print("="*60)
                print(f"Total: {lista_vms.obtener_tamanio()}")
                lista_vms.mostrar()
                
            elif opcion == "3":
                buscar_centro(lista_centros)
                
            elif opcion == "4":
                buscar_vm(lista_vms)
                
            elif opcion == "5":
                eliminar_centro(lista_centros)
                
            elif opcion == "6":
                eliminar_vm(lista_vms)
                
            elif opcion == "7":
                lista_centros.graficar("lista_centros")
                
            elif opcion == "8":
                lista_vms.graficar("lista_vms")
                
            elif opcion == "9":
                print("\n¡Hasta luego!")
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
