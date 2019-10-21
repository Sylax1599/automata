class Pila:
    def __init__(self, inicial):
        self.pila = []
        self.pila.append(inicial)
    
    def pushDate(self,dato):
        self.pila.append(dato)
    
    def removeDate(self):
        self.pila.pop()
    
    def viewPila(self):
        print(self.pila)

    def getLen(self):
        return len(self.pila)

    def isEmpty(self):
        if(len(self.pila) > 0):
            #print (str(len(self.pila)))
            return True
        return False
    
    def getTope(self):
        return self.pila[len(self.pila)-1]