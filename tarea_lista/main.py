from pasajero import Pasajero
from mi_lista import ListaPasajerosManual
from lista_python import ListaPasajerosPython
from ejercicios import menu_ejercicios
lista1 = ListaPasajerosManual(capacidad=10)
lista2 = ListaPasajerosPython()

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes ingresar un número entero")


def leer_pasajero():
    numero = leer_entero("Número: ")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    edad = leer_entero("Edad: ")
    fecha_vuelo = input("Fecha de vuelo: ")
    destino = input("Destino: ")
    asiento = input("Asiento: ")

    return Pasajero(numero, nombre, cedula, edad, fecha_vuelo, destino, asiento)
def cargar_datos_prueba(lista):
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana", "0912345678", 28))
    lista.añadir(Pasajero("Luis", "0987654321", 35))
    lista.añadir(Pasajero("Beto", "0934567890", 16))
    lista.añadir(Pasajero("Elena", "0901234567", 41))
    print("Datos de prueba cargados")


def mostrar_menu_lista(titulo):
    print("\n==========", titulo, "==========")
    print("1. Añadir pasajero")
    print("2. Listar pasajeros")
    print("3. Insertar en una posición")
    print("4. Buscar por cédula")
    print("5. Buscar binaria")
    print("6. Modificar pasajero")
    print("7. Eliminar por posición")
    print("8. Eliminar por cédula")
    print("9. Ordenar ascendente")
    print("10. Ordenar descendente")
    print("11. Reversar")
    print("12. Copiar lista")
    print("13. Longitud")
    print("14. Filtrar mayores de edad")
    print("15. Nombres en mayúsculas")
    print("C. Cargar datos de prueba")
    print("0. Volver")


# MENÚ COMPARTIDO PARA AMBAS LISTAS

def menu_lista(lista, titulo):
    while True:
        mostrar_menu_lista(titulo)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista.añadir(pasajero):
                print("Pasajero añadido")

        elif op == "2":
            lista.listar()

        elif op == "3":
            posicion = leer_entero("Posición: ")
            pasajero = leer_pasajero()
            if lista.insertar(posicion, pasajero):
                print("Pasajero insertado")

        elif op == "4":
            cedula = input("Cédula: ").strip()
            posicion = lista.buscar(cedula)

            if posicion == -1:
                print("Pasajero no encontrado")
            else:
                if titulo == "LISTA 1":
                    print(lista.datos[posicion])
                else:
                    print(lista.pasajeros[posicion])

        elif op == "5":
            print("Primero debes ordenar con la opción 9")
            cedula = input("Cédula: ").strip()
            posicion = lista.buscar_binaria(cedula)

            if posicion == -1:
                print("Pasajero no encontrado")
            else:
                if titulo == "LISTA 1":
                    print(lista.datos[posicion])
                else:
                    print(lista.pasajeros[posicion])

        elif op == "6":
            cedula = input("Cédula: ").strip()
            nombre = input("Nuevo nombre: ").strip()
            edad = leer_entero("Nueva edad: ")

            if lista.modificar(cedula, nombre, edad):
                print("Pasajero modificado")

        elif op == "7":
            posicion = leer_entero("Posición: ")
            eliminado = lista.eliminar_por_posicion(posicion)

            if eliminado is not None:
                print("Eliminado:", eliminado)

        elif op == "8":
            cedula = input("Cédula: ").strip()

            if lista.eliminar_por_valor(cedula):
                print("Pasajero eliminado")
            else:
                print("Pasajero no encontrado")

        elif op == "9":
            lista.ordenar_asc()
            print("Lista ordenada ascendentemente")
            lista.listar()

        elif op == "10":
            lista.ordenar_desc()
            print("Lista ordenada descendentemente")
            lista.listar()

        elif op == "11":
            lista.reversar()
            print("Lista invertida")
            lista.listar()

        elif op == "12":
            copia = lista.copiar()
            copia.reversar()

            print("\n--- COPIA REVERSADA ---")
            copia.listar()

            print("\n--- ORIGINAL ---")
            lista.listar()

        elif op == "13":
            print("Hay", lista.longitud(), "pasajeros")

        elif op == "14":
            mayores = lista.filtrar_mayores_de_edad()
            print("Pasajeros mayores de edad:")
            mayores.listar()

        elif op == "15":
            nombres = lista.nombres_en_mayusculas()
            print(nombres)

        elif op == "C":
            cargar_datos_prueba(lista)

        elif op == "0":
            break

        else:
            print("Opción no válida")


def menu_lista1():
    menu_lista(lista1, "LISTA 1")


def menu_lista2():
    menu_lista(lista2, "LISTA 2")


# MENÚ PRINCIPAL

def main():
    while True:
        print("\n===== SISTEMA DE PASAJEROS =====")
        print("1. Lista 1 (manual)")
        print("2. Lista 2 (Python)")
        print("3. Listar ejercicios")
        print("4. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            menu_lista1()

        elif opcion == "2":
            menu_lista2()

        elif opcion == "3":
            menu_ejercicios()

        elif opcion == "4":
            print("Hasta pronto")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
