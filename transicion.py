class Transicion:
    def __init__(self, inicio = "", fin = "", caracter = "", buscar = "", insertar = ""):
        self.inicio = inicio
        self.fin = fin
        self.caracter = caracter
        self.buscar = buscar
        self.insertar = insertar
    
    def getInicio(self):
        return self.inicio
    
    def getFin(self):
        return self.fin

    def getCaracter(self):
        return self.caracter

    def getBuscar(self):
        return self.buscar

    def getInsertar(self):
        return self.insertar

    def setFin(self, fin):
        self.fin = fin