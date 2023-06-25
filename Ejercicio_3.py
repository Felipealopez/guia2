import math

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_dato(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def calcular_media(self):
        if not self.cabeza:
            return None

        suma = 0
        contador = 0
        actual = self.cabeza

        while actual:
            suma += actual.dato
            contador += 1
            actual = actual.siguiente

        return suma / contador

    def calcular_desviacion_estandar(self):
        if not self.cabeza:
            return None

        media = self.calcular_media()
        suma_cuadrados = 0
        contador = 0
        actual = self.cabeza

        while actual:
            suma_cuadrados += (actual.dato - media) ** 2
            contador += 1
            actual = actual.siguiente

        varianza = suma_cuadrados / contador
        desviacion_estandar = math.sqrt(varianza)
        return desviacion_estandar

    def imprimir_lista(self):
        if not self.cabeza:
            print("La lista se encuentra vacía.")
            return

        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def verificar_lista_vacia(self):
        return not self.cabeza

lista = ListaEnlazada()

lista.agregar_dato(8)
lista.agregar_dato(80)
lista.agregar_dato(800)
lista.agregar_dato(8000)

lista.imprimir_lista()

media = lista.calcular_media()
print("El resultado de la media es:", media)

desviacion_estandar = lista.calcular_desviacion_estandar()
print("El resultado de la desviación estandar es:", desviacion_estandar)

esta_vacia = lista.verificar_lista_vacia()
print("¿La lista está vacía?", esta_vacia)
