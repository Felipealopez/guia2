class Supermercado:
    def __init__(self):
        self.productos_recibidos = []
        self.productos_despachar = []

    def agregar_producto(self, producto):
        self.productos_recibidos.append(producto)
        print("El producto se ha agregado exitosamente.")

    def despachar_producto(self):
        if self.productos_despachar:
            producto = self.productos_despachar.pop(0)
            print("El producto ha sido despachado:", producto)
        else:
            print("No existen productos disponibles por el momento.")

    def pila_vacia(self):
        if not self.productos_recibidos:
            print("La pila de productos recibidos se encuentra vacía.")
        else:
            print("La pila de productos recibidos no se encuentra vacía.")

    def cola_vacia(self):
        if not self.productos_despachar:
            print("La cola de productos para despachar se encuentra vacía.")
        else:
            print("La cola de productos para despachar no se encuentra vacía.")

    def imprimir_productos_recibidos(self):
        print("La lista de productos recibidos es:")
        for producto in reversed(self.productos_recibidos):
            print(producto)

    def imprimir_productos_despachar(self):
        print("La lista de productos para despachar es:")
        for producto in self.productos_despachar:
            print(producto)

    def mostrar_total_cantidad(self):
        total_productos = len(self.productos_recibidos) + len(self.productos_despachar)
        print("La cantidad total de productos en el almacén es:", total_productos)

supermercado = Supermercado()

supermercado.agregar_producto("Galletas")
supermercado.agregar_producto("Manzanas")
supermercado.agregar_producto("Suflitos")
supermercado.agregar_producto("Jugo")
supermercado.agregar_producto("Miel")
supermercado.agregar_producto("Platanos")

supermercado.despachar_producto()
supermercado.despachar_producto()

supermercado.imprimir_productos_recibidos()

supermercado.cola_vacia()

supermercado.mostrar_total_cantidad()
