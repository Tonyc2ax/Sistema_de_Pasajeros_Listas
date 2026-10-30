from pasajero import Pasajero

class ListaPasajerosManual:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):
        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return False

        if self.buscar(pasajero.cedula) != -1:
            print("La cédula ya existe")
            return False

        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("Lista vacía")
            return

        for i in range(self.cantidad):
            print(f"[{i}] {self.datos[i]}")

    def longitud(self):
        return self.cantidad

    def insertar(self, posicion, pasajero):
        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return False

        if posicion < 0 or posicion > self.cantidad:
            print("Posición no válida")
            return False

        if self.buscar(pasajero.cedula) != -1:
            print("La cédula ya existe")
            return False

        i = self.cantidad

        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i = i - 1

        self.datos[posicion] = pasajero
        self.cantidad = self.cantidad + 1
        return True
    def buscar(self, cedula):
        for i in range(self.cantidad):
            if self.datos[i].cedula == cedula:
                return i

        return -1
    def buscar_binaria(self, cedula):
        izquierda = 0
        derecha = self.cantidad - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2

            if self.datos[medio].cedula == cedula:
                return medio

            elif self.datos[medio].cedula < cedula:
                izquierda = medio + 1

            else:
                derecha = medio - 1

        return -1

    def modificar(self, cedula, nuevo_nombre, nueva_edad):
        posicion = self.buscar(cedula)

        if posicion == -1:
            print("Pasajero no encontrado")
            return False

        self.datos[posicion].nombre = nuevo_nombre
        self.datos[posicion].edad = nueva_edad
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("Posición no válida")
            return None

        valor = self.datos[posicion]

        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1

        return valor
    def eliminar_por_valor(self, cedula):
        posicion = self.buscar(cedula)

        if posicion == -1:
            print("Pasajero no encontrado")
            return False

        self.eliminar_por_posicion(posicion)
        return True

    def ordenar_asc(self):
        n = self.cantidad

        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].cedula > self.datos[i + 1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux
    def ordenar_desc(self):
        n = self.cantidad

        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].cedula < self.datos[i + 1].cedula:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    def reversar(self):
        izquierda = 0
        derecha = self.cantidad - 1

        while izquierda < derecha:
            aux = self.datos[izquierda]
            self.datos[izquierda] = self.datos[derecha]
            self.datos[derecha] = aux

            izquierda = izquierda + 1
            derecha = derecha - 1

    def copiar(self):
        nueva = ListaPasajerosManual(self.capacidad)

        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])

        return nueva
    def filtrar_mayores_de_edad(self):
        resultado = ListaPasajerosManual(self.capacidad)

        for i in range(self.cantidad):
            if self.datos[i].es_mayor_de_edad():
                resultado.añadir(self.datos[i])

        return resultado
    def nombres_en_mayusculas(self):
        resultado = [None] * self.cantidad

        for i in range(self.cantidad):
            resultado[i] = self.datos[i].nombre.upper()

        return resultado
