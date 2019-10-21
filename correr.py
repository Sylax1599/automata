
import holamundo
from estado import *
from pila import *
from transicion import *
from tkinter import *
import time
from hablar import aceptada,rechaza,transicion,hola

#Mira fb
#ahh ya

root=Tk()
root.title("AUTOMATA")
root.resizable(0,0)
root.iconbitmap("icono.ico")
root.geometry("950x450")
root.config(bg="#44656B")
#---------- FIN RAIZ ---------
valor=StringVar()

#------- EL FRAME --------

canvas = Canvas(root,width=200, height=100, bg='white')
canvas.pack()
canvas.config(bg="#BCD1D5")
canvas.config(width="800", height="450")

# conectar 1 con el mismo
cordenadas5=100,170,150,220
canvas.create_oval(cordenadas5,width=3)
canvas.create_line(140,195,148,215, width=2)
canvas.create_line(148,208,160,200, width=2)

# conectar 2 con el mismo
cordenadas5=250,170,300,220
canvas.create_oval(cordenadas5,width=3)
canvas.create_line(290,195,298,215, width=2)
canvas.create_line(298,208,310,200, width=2)

#estado 1
cordenadas=100,200,150,250
canvas.create_oval(cordenadas,width=5, fill='white')
circulo1=Label(canvas,text="q0")
circulo1.config(bg="#FFFFFF")
circulo1.config(font=("Comic Sans MS",13))
circulo1.place(x=111,y=210)
#estado 2
cordenadas2=250,200,300,250
canvas.create_oval(cordenadas2,width=5, fill='white')
circulo2=Label(canvas,text="q1")
circulo2.config(bg="#FFFFFF")
circulo2.config(font=("Comic Sans MS",13))
circulo2.place(x=261,y=210)
#estado 3
cordenadas3=400,200,450,250
cordenadas4=390,190,460,260
canvas.create_oval(cordenadas3,width=5, fill='white')
canvas.create_oval(cordenadas4,width=5)
circulo3=Label(canvas,text="q2")
circulo3.config(bg="#FFFFFF")
circulo3.config(font=("Comic Sans MS",13))
circulo3.place(x=411,y=210)

#la flechita del inicio 
canvas.create_line(50,225,100,225, width=2)
canvas.create_line(90,220,100,225, width=2)
canvas.create_line(90,230,100,225, width=2)
#conectar 1 y 2
canvas.create_line(148,225,253,225, width=2)
canvas.create_line(240,220,250,225, width=2)
canvas.create_line(240,230,250,225, width=2)
#conectar 2 y 3
canvas.create_line(300,225,390,225, width=2)
canvas.create_line(380,220,390,225, width=2)
canvas.create_line(380,230,390,225, width=2)

#-------------------- PILA
#posicion 0
Label(canvas,text="  ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=260)
canvas.create_rectangle(655, 50, 705, 100, width=4, fill='#44656B')
#posicion 1
Label(canvas,text="  ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=210)
canvas.create_rectangle(655, 100, 705, 150, width=4, fill='#44656B')
#posicion 2
Label(canvas,text="  ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=160)
canvas.create_rectangle(655, 150, 705, 200, width=4, fill='#44656B')
#posicion 3
Label(canvas,text="  ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=110)
canvas.create_rectangle(655, 200, 705, 250, width=4, fill='#44656B')
#posicion 4
Label(canvas,text="  ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=110-50)
canvas.create_rectangle(655, 250, 705, 300, width=4, fill='#44656B')


#-------- LABELS ------------
miLabel=Label(canvas,text="AUTOMATA DE PILA",fg="#383838")
miLabel.config(bg="#BCD1D5")
miLabel.config(font=("Comic Sans MS",18))
miLabel.place(x=250,y=20)

miLabel2=Label(canvas,text="Ingrese la expresion: ",fg="#383838")
miLabel2.config(bg="#BCD1D5")
miLabel2.config(font=("Comic Sans MS",12))
miLabel2.place(x=60,y=100)

labelPila=Label(canvas, text="PILA",fg="#383838")
labelPila.config(bg="#BCD1D5")
labelPila.config(font=("Comic Sans MS",18))
labelPila.place(x=650,y=320)

#-----------------------------
cuadroTexto=Entry(canvas,textvariable=valor)
cuadroTexto.config(width=20)
cuadroTexto.place(x=230,y=105)




def aceptado():
    cadena=valor.get()
    cadena+="x"
    estado=cargarAutomata(cadena)
    if estado:
        estadoAceptado=Label(canvas,text="PALABRA ACEPTADA!",fg="#383838")
        estadoAceptado.config(bg="#BCD1D5")
        estadoAceptado.config(font=("Comic Sans MS",22))
        estadoAceptado.place(x=210,y=290)
        aceptada()
    else:
        estadoRechazado=Label(canvas,text="PALABRA RECHAZADA!",fg="#383838")
        estadoRechazado.config(bg="#BCD1D5")
        estadoRechazado.config(font=("Comic Sans MS",22))
        estadoRechazado.place(x=210,y=290)
        rechaza()
        
    

#--------- BOTONES -----------------

botonlento=Button(canvas,text="MODO LENTO",fg="#F7F7F7",command=aceptado)
botonlento.config(font=("Comic Sans MS",10))
botonlento.config(bg="#474747",width=12, height=1)
botonlento.place(x=250,y=350)
botonlento.config(relief='groove')
"""
botonrapido=Button(canvas,text="MODO RAPIDO",fg="#F7F7F7")
botonrapido.config(font=("Comic Sans MS",10))
botonrapido.config(bg="#474747",width=12, height=1)
botonrapido.place(x=380,y=350)
"""

def cargarAutomata(cadena):
    # TERMINA EN X PORQUE ES EL VALOR VACIO, EL VALOR VACIO ESTÁ EN UNA TRANSICION EN HOLAMUNDO MIRA
    estados = []
    print(len(cadena))
    
    for estado in holamundo.nodos['estados']:
        estados.append(Estado(estado))   
    for transicion in holamundo.nodos['transiciones']:
        auxEstadoInicial = None
        auxEstuadoFinal = None
        caracter = None
        buscar = None
        insertar = None
        for estado in estados:
            if estado.getEstado() == 'q2':
                aceptacion = estado
            if transicion['inicio'] == estado.getEstado():
                auxEstadoInicial = estado
                caracter = transicion['cadena']
                buscar = transicion['buscar']
                insertar = transicion['insertar']
                #final = transicion['final']

            if transicion['fin'] == estado.getEstado():
                auxEstuadoFinal = estado

        t = Transicion(auxEstadoInicial, auxEstuadoFinal, caracter, buscar, insertar)
        auxEstadoInicial.setTransicion(t)
        #print(auxEstadoInicial.getTransiciones())


    band=False
    prueba2=Label(canvas,text="",fg="#383838",bg="#BCD1D5")
    while True:
        p = Pila('#')
        actual = estados[0]
        Label(canvas,text="#",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=260)


        for caracter in range(len(cadena)):
                time.sleep(2)
                print("el caracter en resivion es: ",cadena[caracter])
                """root.update()
                prueba=Label(canvas,text="HOLA",fg="#383838")
                prueba.place(x=40,y=67)"""
                contador = 0
                for estado in estados:    
                    
                    for x in estado.getTransiciones():

                        if cadena[caracter] == x.getCaracter() and x.getBuscar() == p.getTope() and estado.getEstado() == actual.getEstado():
                            print("------------------------------------------------------------------------Mi estado es:", estado.getEstado())
                            #prueba2=Label(canvas,text=""+x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar(),fg="#383838",bg="#BCD1D5")
                            #prueba2.place(x=400,y=140)
                            #print("zzzzzzzzzzzzzzzzzzzz",x.getFin().getEstado())
                            if x.getFin().getEstado()=="q1" and (x.getCaracter()=="c" and x.getBuscar()=="#" and x.getInsertar()=="#") or (x.getCaracter()=="c" and x.getBuscar()=="b"  and x.getInsertar()=="b") or (x.getCaracter()=="c" and x.getBuscar()=="a" and x.getInsertar()=="a"):
                                #print("Estoy en q22222222222222222222222222222222222222")
                                
                                
                                #prueba2=Label(canvas,text=""+x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar(),fg="#383838",bg="#BCD1D5")
                                prueba2.config(text=x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar())
                                prueba2.place(x=180,y=200)
                                

                            
                            if x.getFin().getEstado()=="q2" and (x.getCaracter()=="x" and x.getBuscar()=="#" and x.getInsertar()=="#"):
                                #prueba2=Label(canvas,text="              ",fg="#383838",bg="#BCD1D5")
                                #prueba2.place(x=250,y=140)
                                #prueba2=Label(canvas,text=""+x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar(),fg="#383838",bg="#BCD1D5")
                                prueba2.config(text=x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar())
                                prueba2.place(x=350,y=200)
                            
                            if estado.getEstado()=="q0":
                                prueba=Label(canvas,text="ESTOY EN EL Q0",fg="#383838")
                                cordenadas=100,200,150,250
                                canvas.create_oval(cordenadas,width=5, fill='grey')
                                circulo1=Label(canvas,text="q0")
                                circulo1.config(bg="grey")
                                circulo1.config(font=("Comic Sans MS",13))
                                circulo1.place(x=111,y=210)
                                root.update()
                                time.sleep(2)
                                cordenadas=100,200,150,250
                                canvas.create_oval(cordenadas,width=5, fill='#FFFFFF')
                                circulo1=Label(canvas,text="q0")
                                circulo1.config(bg="#FFFFFF")
                                circulo1.config(font=("Comic Sans MS",13))
                                circulo1.place(x=111,y=210)
                                #prueba2=Label(canvas,text="            ",fg="#383838",bg="#BCD1D5")
                                #prueba2.place(x=100,y=140)
                                
                                #prueba2=Label(canvas,text=""+x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar(),fg="#383838",bg="#BCD1D5")
                                
                                if x.getFin().getEstado() == "q1":
                                    pass
                                else:
                                    prueba2.config(text=x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar())

                                    prueba2.place(x=100,y=140)
                                

                                #transicion(["a","b","c"])
                                
                                root.update()
                                hola(x.getCaracter(),x.getBuscar(),x.getInsertar())
                            if estado.getEstado()=="q1":
                                cordenadas=100,200,150,250
                                canvas.create_oval(cordenadas,width=5, fill='grey')
                                circulo1=Label(canvas,text="q0")
                                circulo1.config(bg="grey")
                                circulo1.config(font=("Comic Sans MS",13))
                                circulo1.place(x=111,y=210)
                                prueba=Label(canvas,text="ESTOY EN EL Q1",fg="#383838")
                                prueba.place(x=40,y=67)
                                cordenadas2=250,200,300,250
                                canvas.create_oval(cordenadas2,width=5, fill='grey')
                                circulo2=Label(canvas,text="q1")
                                circulo2.config(bg="grey")
                                circulo2.config(font=("Comic Sans MS",13))
                                circulo2.place(x=261,y=210)
                                root.update()
                                time.sleep(2)
                                cordenadas2=250,200,300,250
                                canvas.create_oval(cordenadas2,width=5, fill='white')
                                circulo2=Label(canvas,text="q1")
                                circulo2.config(bg="#FFFFFF")
                                
                                circulo2.config(font=("Comic Sans MS",13))
                                circulo2.place(x=261,y=210)
                                
                                
                                #prueba2=Label(canvas,text="            ",fg="#383838",bg="#BCD1D5")
                                #prueba2.place(x=100,y=140)
                                #prueba2=Label(canvas,text="             ",fg="#383838",bg="#BCD1D5")
                                #prueba2.place(x=180,y=200)
                                #prueba2=Label(canvas,text=""+x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar(),fg="#383838",bg="#BCD1D5")
                                if x.getFin().getEstado() == "q2":
                                    pass
                                else:
                                    prueba2.config(text=x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar())
                                    prueba2.place(x=250,y=140)
                                
                                
                                #hola(x.getCaracter(),x.getBuscar(),x.getInsertar())
                                root.update()
                                hola(x.getCaracter(),x.getBuscar(),x.getInsertar())
                            '''
                            if estado.getEstado()=="q2":
                                prueba2=Label(canvas,text=""+x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar(),fg="#383838",bg="#BCD1D5")
                                prueba2.place(x=400,y=140)
                            '''
                            if band:
                                #print("llegue a desapilar")
                                if p.getLen()==4:
                                    Label(canvas,text="  ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=60)
                                    root.update()
                                if p.getLen()==3:
                                    Label(canvas,text="  ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=110)
                                    root.update()
                                if p.getLen()==2:
                                    Label(canvas,text="  ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=160)
                                    root.update()
                                if p.getLen()==1:
                                    Label(canvas,text="  ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=210)
                                    root.update()
                            print("El tamaño de la pila es", p.getLen()) 
                            p.removeDate()
                            print(actual.getEstado())
                            for insert in x.getInsertar():
                                if insert != 'x':

                                    if p.getLen()==1:
                                        Label(canvas,text=insert,font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=210)
                                        root.update()
                                    if p.getLen()==2:
                                        Label(canvas,text=insert,font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=160)
                                        root.update()
                                    if p.getLen()==3:
                                        Label(canvas,text=insert,font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=110)
                                        root.update()
                                    if p.getLen()==4:
                                        Label(canvas,text=insert,font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=60)
                                        root.update()
                                    if p.getLen()==5:
                                        Label(canvas,text=insert,font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=10)
                                        root.update()
                                    
                                    print("Esta insertando",insert)
                                    p.pushDate(insert)
                                    #p.viewPila()
                                    print("El tamaño de la pila es", p.getLen())  
                                    band=True
                            p.viewPila()
                            actual = x.getFin()
        
        if actual.getEstado()=="q2":
            time.sleep(2)
            cordenadas=100,200,150,250
            canvas.create_oval(cordenadas,width=5, fill='grey')
            circulo1=Label(canvas,text="q0")
            circulo1.config(bg="grey")
            circulo1.config(font=("Comic Sans MS",13))
            circulo1.place(x=111,y=210)
            prueba=Label(canvas,text="ESTOY EN EL Q1",fg="#383838")
            prueba.place(x=40,y=67)
            cordenadas2=250,200,300,250
            canvas.create_oval(cordenadas2,width=5, fill='grey')
            circulo2=Label(canvas,text="q1")
            circulo2.config(bg="grey")
            circulo2.config(font=("Comic Sans MS",13))
            circulo2.place(x=261,y=210)
            cordenadas3=400,200,450,250
            canvas.create_oval(cordenadas3,width=5, fill='grey')
            circulo3=Label(canvas,text="q2") 
            circulo3.config(bg="grey")
            circulo3.config(font=("Comic Sans MS",13))
            circulo3.place(x=411,y=210)
            prueba=Label(canvas,text="ESTOY EN EL Q2",fg="#383838")
            prueba.place(x=40,y=67)
            root.update()
        if actual.getEstado() == aceptacion.getEstado():
                print("La palabra [ "+ cadena[:len(cadena)-1] +" ] fue aceptada")
                return True
               
        else:
                print("La palabra [ "+ cadena[:len(cadena)-1] +" ] no fue aceptada")
                return False
                



root.mainloop()