##se crea clase nodocancion y se inicializa estando vacia 

class nodocancion:
    def __init__ (self,cancion, artista):
        self.cancion = cancion
        self.artista = artista
        self.siguienteCancion = None
        self.anteriorCancion = None

#Lista enlazada

class lista:
    def __init__ (self):
        self.inicioNodo = None 
        self.finalNodo = None 

#clase de la cancion actual donde se imprime la lista de reproduccion y se itera a traves del inicioNodo usando for in
#si el nodo es igual pasa a la siguiente cancion

    def cancionactual(self):
        nodo = self.inicioNodo
        for nodo in not None:
            print("canción:", nodo.cancion)
            print("Artista:", nodo.artista)
        nodo = nodo.siguienteCancion

#similar al anterior mediante for in busca una cancion y si no conside procede a eliminarla mediante el remove
#siempre y cuando no este definida
#si el nodo eliminado esta al inicio se usa nodo.anteriorCancion si es el ultimo nodoSigueinte cancion
#termina el ciclo con break
#con un csv se podria crear una interfaz similar al proyecto donde incluya listas de reproduccion.

def eliminar_cancion(self, cancion):
    for nodo in self.cancion:
        if nodo.cancion == cancion:
            if nodo.anteriorCancion is None:
                self.cancion.remove(nodo)
                if self.cancion:
                    self.cancion[0].anteriorCancion = None
            else:
                nodo.anteriorCancion.siguienteCancion = nodo.siguienteCancion
                if nodo.siguienteCancion is not None:
                    nodo.siguienteCancion.anteriorCancion = nodo.anteriorCancion
                else:
                    ultimo_nodo = self.cancion[-1]
                    ultimo_nodo.anteriorCancion = nodo.anteriorCancion
            break