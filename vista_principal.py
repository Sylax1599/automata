from tkinter import *
from main import *



root=Tk()
root.title("AUTOMATA")
root.resizable(0,0)
root.iconbitmap("icono.ico")
root.geometry("950x450")
root.config(bg="#44656B")


canvas = Canvas(root,width=200, height=100, bg='white')
canvas.pack()
canvas.config(bg="#BCD1D5")
canvas.config(width="800", height="450")

a = Automata()

#print(a.iniciar_estados())
while True:
    '''
    if a.iniciar_estados() == "hoaaa":
        print("qq") 
        milabel = Label(canvas,text=" ya está ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=110)
        root.update()
    '''
    if a.validar_palabra() == 4:
        print("la suma es ", a.suma)
        print("la ", a.estado)
        print("a",a.transicion)
root.mainloop()

def pinta2():
    print("hola")
    milabel = Label(canvas,text=" asdasd ",font=("Comic Sans MS",15),bg="#44656B",fg="#FFFFFF").place(x=665,y=110)
    #return milabel

def pinta(objeto, texto):
    milabel.config(text=texto)
#pinta2()    
