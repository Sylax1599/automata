
from cargar import nodos 
from estado import *
from pila import *
from transicion import *
from tkinter import *
import time
from hablar import *


root=Tk()
root.title("AUTOMATA")
root.resizable(0,0)
root.iconbitmap("icono.ico")
root.geometry("950x450")
root.config(bg="#44656B")


#---------- FIN RAIZ ---------
valor=StringVar()
#------- EL FRAME --------
canvas = Canvas(root,bg="#BCD1D5",width="800", height="450")
canvas.pack()
#----- FIN DEL FRAME 

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
circulo1=Label(canvas,text="q0",bg="#FFFFFF",font=("Comic Sans MS",13))
circulo1.place(x=111,y=210)
#estado 2
cordenadas2=250,200,300,250
canvas.create_oval(cordenadas2,width=5, fill='white')
circulo2=Label(canvas,text="q1",bg="#FFFFFF",font=("Comic Sans MS",13))
circulo2.place(x=261,y=210)
#estado 3
cordenadas3=400,200,450,250
cordenadas4=390,190,460,260
canvas.create_oval(cordenadas3,width=5, fill='white')
canvas.create_oval(cordenadas4,width=5)
circulo3=Label(canvas,text="q2",bg="#FFFFFF",font=("Comic Sans MS",13))
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
miLabel=Label(canvas,text="AUTOMATA DE PILA",fg="#383838",bg="#BCD1D5",font=("Comic Sans MS",18))
miLabel.place(x=250,y=20)
miLabel2=Label(canvas,text="Ingrese la expresion: ",fg="#383838",bg="#BCD1D5",font=("Comic Sans MS",12))
miLabel2.place(x=60,y=100)
labelPila=Label(canvas, text="PILA",fg="#383838",bg="#BCD1D5",font=("Comic Sans MS",18))
labelPila.place(x=650,y=320)


#-------------CUADRO DE TEXTO ----------------
cuadroTexto=Entry(canvas,textvariable=valor,width=20)
cuadroTexto.place(x=230,y=105)




def aceptado(tiempo):
    cadena=valor.get()
    cadena+="x"
    estado=validar(cadena,tiempo)
    if estado:
        Label(canvas,text="PALABRA ACEPTADA!",fg="#383838",bg="#BCD1D5",font=("Comic Sans MS",22)).place(x=210,y=290)
        aceptada()
    else:
        Label(canvas,text="PALABRA RECHAZADA!",fg="#383838",bg="#BCD1D5",font=("Comic Sans MS",22)).place(x=210,y=290)
        rechazada()
        
    

#--------- BOTONES -----------------

botonlento=Button(canvas,text="MODO LENTO",fg="#F7F7F7",command= lambda: aceptado(1))
botonlento.config(font=("Comic Sans MS",10),bg="#474747",width=12, height=1,relief='groove')
botonlento.place(x=250,y=350)

botonrapido=Button(canvas,text="MODO RAPIDO",fg="#F7F7F7",command= lambda: aceptado(0.5))
botonrapido.config(font=("Comic Sans MS",10),bg="#474747",width=12, height=1,relief='groove')
botonrapido.place(x=380,y=350)


#---------- PARTE LOGICA 

estados = []

def cargarAutomata():
    for estado in nodos['estados']:
        estados.append(Estado(estado))   
    for transicion in nodos['transiciones']:
        auxEstadoInicial = None
        auxEstuadoFinal = None
        caracter = None
        buscar = None
        insertar = None
        for estado in estados:
            if estado.getEstado() == 'q2':
                global aceptacion
                aceptacion = estado  
            if transicion['inicio'] == estado.getEstado():
                auxEstadoInicial = estado
                caracter = transicion['cadena']
                buscar = transicion['buscar']
                insertar = transicion['insertar']

            if transicion['fin'] == estado.getEstado():
                auxEstuadoFinal = estado

        nuevaTransicion = Transicion(auxEstadoInicial, auxEstuadoFinal, caracter, buscar, insertar)
        auxEstadoInicial.setTransicion(nuevaTransicion)


    

def validar(cadena,tiempo):
    cargarAutomata()
    p = Pila('#')
    actual = estados[0]
    Label(canvas,text="#",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=260)


    apilar=False
    trancision1=Label(canvas,text="",fg="#383838",bg="#BCD1D5")
    circulo1=Label(canvas,text="q0",bg="#FFFFFF",font=("Comic Sans MS",13))
    circulo1.place(x=111,y=210)
    circulo2=Label(canvas,text="q1",bg="#FFFFFF",font=("Comic Sans MS",13))
    circulo2.place(x=261,y=210)
    circulo3=Label(canvas,text="q2",bg="#FFFFFF",font=("Comic Sans MS",13))
    circulo3.place(x=411,y=210)



    for caracter in range(len(cadena)):
            #time.sleep(tiempo)
            for estado in estados:    
                
                for x in estado.getTransiciones():


                    if cadena[caracter] == x.getCaracter() and x.getBuscar() == p.getTope() and estado.getEstado() == actual.getEstado():

                        if x.getFin().getEstado()=="q1" and (x.getCaracter()=="c" and x.getBuscar()=="#" and x.getInsertar()=="#") or (x.getCaracter()=="c" and x.getBuscar()=="b"  and x.getInsertar()=="b") or (x.getCaracter()=="c" and x.getBuscar()=="a" and x.getInsertar()=="a"):
                            trancision1.config(text=x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar())
                            trancision1.place(x=180,y=200)
                            

                        
                        if x.getFin().getEstado()=="q2" and (x.getCaracter()=="x" and x.getBuscar()=="#" and x.getInsertar()=="#"):
                            trancision1.config(text=x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar())
                            trancision1.place(x=350,y=200)
                        

                        if estado.getEstado()=="q0":                         
                            cordenadas=100,200,150,250
                            canvas.create_oval(cordenadas,width=5, fill='grey')
                            circulo1.config(text="q0",bg="grey",font=("Comic Sans MS",13))
                            root.update()
                            
                            time.sleep(tiempo)

                            canvas.create_oval(cordenadas,width=5, fill='#FFFFFF')
                            circulo1.config(text="q0",bg="#FFFFFF",font=("Comic Sans MS",13))
                           
                            if x.getFin().getEstado() == "q1":
                                canvas.create_oval(cordenadas,width=5, fill='grey')
                                circulo1.config(text="q0",bg="grey",font=("Comic Sans MS",13))
                            else:
                                trancision1.config(text=x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar())
                                trancision1.place(x=100,y=140)
                            root.update()
                        

                        if estado.getEstado()=="q1":
                            cordenadas2=250,200,300,250
                            canvas.create_oval(cordenadas2,width=5, fill='grey')
                            circulo2.config(text="q1",bg="grey",font=("Comic Sans MS",13))
                            root.update()
                            
                            time.sleep(tiempo)

                            canvas.create_oval(cordenadas2,width=5, fill='white')
                            circulo2.config(text="q1",bg="#FFFFFF",font=("Comic Sans MS",13))
                            
                            
                            if x.getFin().getEstado() == "q2":
                                canvas.create_oval(cordenadas2,width=5, fill='grey')
                                circulo2.config(text="q1",bg="grey",font=("Comic Sans MS",13))

                            else:
                                trancision1.config(text=x.getCaracter()+"/"+x.getBuscar()+"/"+x.getInsertar())
                                trancision1.place(x=250,y=140)

                            root.update()

                        #LO QUE VOY A DESAPILAR
                        if apilar:
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
                                
                        if tiempo!=0.5:
                            hola(x.getCaracter(),x.getBuscar(),x.getInsertar())

                        #print("El tamaño de la pila es", p.getLen()) 
                        p.removeDate()
                        #print(actual.getEstado())

                        #LO QUE VOY A APILAR 
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
                                apilar=True
                        p.viewPila()
                        actual = x.getFin()
                        break
    
    if actual.getEstado()=="q2":
        time.sleep(tiempo)
        cordenadas3=400,200,450,250
        canvas.create_oval(cordenadas3,width=5, fill='grey')
        circulo3.config(text="q2",bg="grey",font=("Comic Sans MS",13)) 
        root.update()

    
    if actual.getEstado() == aceptacion.getEstado():
            print("La palabra [ "+ cadena[:len(cadena)-1] +" ] fue aceptada")
            return True
            
    else:
            print("La palabra [ "+ cadena[:len(cadena)-1] +" ] no fue aceptada")
            return False
                
root.mainloop()