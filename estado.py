class Estado:
    def __init__(self, estado):
        self.estado = estado
        self.transiciones = []
    
    def getEstado(self):
        return self.estado

    def setTransicion(self, transicion):
        self.transiciones.append(transicion)
    
    def getTransiciones(self):
        return self.transiciones