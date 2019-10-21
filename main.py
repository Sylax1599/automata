from holamundo import nodos
#from vista_principal import *
from estado import *
from transicion import *
from time import sleep
class Automata:
    def __init__(self):
        self.estado_aceptacion = "q2"
        self.estados = []
        self.trancisiones = []

    def iniciar_estados(self):
        #pinta(label,"aaaa")
        for estado in nodos["estados"]:
            self.estados.append(Estado(estado))
        return "hoaaa"
        
    def get_estados(self):
        return self.estados
    
    def iniciar_tranciones(self):
        for transiciones in nodos["transiciones"]:
            for estado in self.estados:
                if transiciones['inicio'] == estado.getEstado():
                    auxEstadoInicial = estado
                    caracter = transiciones['cadena']
                    buscar = transiciones['buscar']
                    insertar = transiciones['insertar']
                    
                if transiciones['fin'] == estado.getEstado():
                    auxEstuadoFinal = estado
            nueva_transicion = Transicion(auxEstadoInicial, auxEstuadoFinal, caracter, buscar, insertar)
            auxEstadoInicial.setTransicion(nueva_transicion)
        
    
    def get_tranciones(self):
        return self.transiciones

    def validar_palabra(self):
        
        self.estado = "q1"
        self.transicion = "3"

        sleep(2)

        self.estado = "q2"self.suma = 2+2
        self.transicion = "4"
        return self.suma
    def cargar_automata(self):
        self.iniciar_estados()
        self.iniciar_tranciones()
            
automata = Automata()
automata.cargar_automata()
