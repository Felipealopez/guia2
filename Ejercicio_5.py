class Empleado:
    def __init__(self, nombre, cargo):
        self.nombreEmpleado = nombre
        self.cargo = cargo
        self.Subordinados = []

class Empresa:
    def __init__(self):
        self.raiz = None

    def nuevoEmpleado(self, nombreEmpleado, cargo, Jefecito=None):
        empleado = Empleado(nombreEmpleado, cargo)
        if Jefecito:
            Jefecito.Subordinados.append(empleado)
        else:
            self.raiz = empleado

    def unEmpleadomenos(self, nombre):
        empleado = self.PosibleEmpleado(nombre)
        if empleado:
            jefecito = self.nuevoJefecito(empleado)
            jefecito.Subordinados.extend(empleado.Subordinados)
            jefecito.Subordinados.remove(empleado)

    def Jerarquia(self):
        self.verEmpleados(self.raiz, 0)

    def PosibleEmpleado(self, nombre):
        return self.PosibleEmpleado(nombre, self.raiz)

    def nuevoJefecito(self, empleado):
        return self.nuevoJefecito(empleado, self.raiz)

    def verEmpleado(self, empleado, nivel):
        if empleado:
            print("  " * nivel + f"{empleado.nombre} - {empleado.cargo}")
            self.verEmpleado(empleado.Subordinados[0], nivel + 1) if empleado.Subordinados else None

    def buscarEmpleado(self, nombre, empleado):
        if empleado:
            if empleado.nombre == nombre:
                return empleado
            return self.buscarEmpleado(nombre, empleado.Subordinados[0]) if empleado.Subordinados else None
        return None

    def buscarJefecito(self, empleado, jefecito):
        if jefecito:
            if empleado in jefecito.Subordinados:
                return jefecito
            return self.buscarJefecito(empleado, jefecito.Subordinados[0]) if jefecito.Subordinados else None
        return None

empresa = Empresa()

empresa.nuevoEmpleado("CEO", "Director Ejecutivo")
empresa.nuevoEmpleado("Gerente", "Gerente General", empresa.raiz)
empresa.nuevoEmpleado("Empleado1", "Empleado", empresa.raiz.Subordinados[0])
empresa.nuevoEmpleado("Empleado2", "Empleado", empresa.raiz.Subordinados[0])
empresa.nuevoEmpleado("Empleado3", "Empleado", empresa.raiz.Subordinados[0])
empresa.nuevoEmpleado("Empleado4", "Empleado", empresa.raiz.Subordinados[0])
