import pyttsx3




def aceptada():
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 180)
    engine.setProperty('voice', 'spanish')
    engine.say("PALABRA ACEPTADA")
    engine.runAndWait()

def hola(palabra,busco,apilo):
    print(palabra)
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 180)
    engine.setProperty('voice', 'spanish')
    if apilo=="x":
        apilo="vacío"
    if busco=="#":
        busco="numeral"
    if apilo=="#a":
        apilo="numeral y a"
    if palabra=="x":
        palabra="vacio"
    
    oracion = "Estoy buscando una "+palabra+" busco un caracter "+ busco + " en la cabeza de la pila "+ " y voy a apilar "+apilo

    engine.say(oracion)
    engine.runAndWait()
def transicion(transicion):
    print("------------------------------")
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 180)
    engine.setProperty('voice', 'spanish')
    oracion = "Estoy buscando una "+leo+" busco un caracter "+ busco + " en la cabeza de la pila "+ " y voy a apilar "+apilo

    engine.say(oracion)
    engine.runAndWait()

def rechaza():
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 180)
    engine.setProperty('voice', 'spanish')
    engine.say("PALABRA RECHAZADA")
    engine.runAndWait()