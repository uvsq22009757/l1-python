import tkinter as tk
import random as rd

racine=tk.Tk()

racine.title("Mon dessin")

CANVAS_HEIGHT, CANVAS_WIDTH = 500, 500

def dessin_cercle():
    x=rd.randint(0,400)
    y=rd.randint(0,400)
    canvas.create_oval(x, y, x+100, y+100, fill="blue")

def dessin_carre():
    x=rd.randint(0,400)
    y=rd.randint(0,400)
    canvas.create_rectangle(x, y, x+100, y+100, fill="red")

def dessin_croix():
    x=rd.randint(0,400)
    y=rd.randint(0,400)

    x1=x+100
    y1=y+100
    
    x2=x+100
    y2=y
    
    x3=x
    y3=y+100
    
    canvas.create_line(x, y, x1, y1, fill="yellow")
    canvas.create_line(x2, y2, x3, y3, fill="yellow")

canvas=tk.Canvas(racine, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, bg="black")
couleur=tk.Button(racine, text="Choisir une couleur", relief="raised")
cercle=tk.Button(racine, text="Cercle", relief="raised", command=dessin_cercle)
carre=tk.Button(racine, text="Carré", relief="raised", command=dessin_carre)
croix=tk.Button(racine, text="Croix", relief="raised", command=dessin_croix)

canvas.grid(column=1, row=1, rowspan=3)
couleur.grid(column=1, row=0)
cercle.grid(column=0, row=1)
carre.grid(column=0, row=2)
croix.grid(column=0, row=3)

racine.mainloop()