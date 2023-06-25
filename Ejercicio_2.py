class ColaAtencion:
    def __init__(self):
        self.cola = []
        self.cajas = ["Caja 1", "Caja 2", "Caja 3"]
        self.indice_caja = 0

    def agregar_cliente(self, numero_ticket):
        cliente = {"ticket": numero_ticket, "caja": self.cajas[self.indice_caja]}
        self.cola.append(cliente)
        self.indice_caja = (self.indice_caja + 1) % 3

    def atender_proximo_cliente(self):
        if len(self.cola) == 0:
            print("En este momento no hay clientes esperando la cola.")
            return

        cliente = self.cola.pop(0)
        print("Se atiende al cliente {} en {}.".format(cliente["ticket"], cliente["caja"]))

    def mostrar_cola(self):
        if len(self.cola) == 0:
            print("En este momento no hay clientes esperando en la cola.")
            return

        print("Cola de atención:")
        for cliente in self.cola:
            print("Cliente {}: {}".format(cliente["ticket"], cliente["caja"]))


cola_atencion = ColaAtencion()

cola_atencion.agregar_cliente(1)
cola_atencion.agregar_cliente(2)
cola_atencion.agregar_cliente(3)
cola_atencion.agregar_cliente(4)

cola_atencion.mostrar_cola()
cola_atencion.atender_proximo_cliente()
cola_atencion.atender_proximo_cliente()
cola_atencion.mostrar_cola()
cola_atencion.atender_proximo_cliente()
cola_atencion.mostrar_cola()
