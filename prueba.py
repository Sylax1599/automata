from tkinter import Tk, Label
from time import sleep
from random import random

class BadRoot(Tk):

    def __init__(self, price, time):
        super().__init__()
        self.labels = []
        while True:
            self.labels.append(Label(self, text=(price, time)))
            self.labels[-1].pack()
            self.update()
            sleep(1)

class GoodRoot(Tk):

    def __init__(self, callback):
        super().__init__()
        self.label = Label(self, text=str(callback()))
        self.label.pack()
        while True:
##            self.label['text'] = str(callback())
            self.label.configure(text=str(callback()))
            self.update()
            sleep(1)

if __name__ == '__main__':
    BadRoot('$1.38', '2:37 PM')
    ##GoodRoot(random)