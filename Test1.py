# Créé par Ghislain, le 15/03/2014 en Python
from tkinter import Tk,Canvas
import numpy as np
from random import randint
import time as t

def addVoisin():
    global liste
    l=liste
    for humain in l:
        x=humain[0][0]
        y=humain[0][1]
        temp=False
        if randint(0,4)==0 and x != 0:
            temp = [[x-1,y],[]] in liste
            if temp== False:
                liste=np.append(liste, [[[x-1,y],[1]]], axis=0)
        if randint(0,4)==0 and x != 31:
            temp = [[x+1,y],[]] in liste
            if temp== False:
                liste=np.append(liste, [[[x+1,y],[1]]], axis=0)
        if randint(0,4)==0 and y != 0:
            temp = [[x,y-1],[]] in liste
            if temp== False:
                liste=np.append(liste, [[[x,y-1],[1]]], axis=0)
        if randint(0,4)==0 and y != 31:
            temp = [[x,y+1],[]] in liste
            if temp== False:
                liste=np.append(liste, [[[x,y+1],[1]]], axis=0)

global liste
liste=np.array([[[randint(0,31),randint(0,31)],[1]],
                [[randint(0,31),randint(0,31)],[1]],
                [[randint(0,31),randint(0,31)],[1]],
                [[randint(0,31),randint(0,31)],[1]],
                [[randint(0,31),randint(0,31)],[1]],
                [[randint(0,31),randint(0,31)],[1]],
                [[randint(0,31),randint(0,31)],[1]]])
liste2=np.empty_like(liste)


fen1=Tk()
cadrillage=Canvas(fen1, bg='light grey', height=640, width=640)
cadrillage.pack()
fen1.quit()

fen1
i=0
k=0
while True:
    try:
        humain=liste[i]
        x=humain[0][0]*20
        y=humain[0][1]*20
        cadrillage.create_rectangle(x,y,x+20,y+20, fill="red", outline="black")
        fen1.update()
    except:
        print()
        k+=1
        if k>20:
            fen1.destroy()
            exit()
    addVoisin()
    #t.sleep(0.001)
    i+=1

fen1.mainloop()

