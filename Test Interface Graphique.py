import tkinter as tk


racine = tk.Tk()

CANVAS_HEIGHT, CANVAS_WIDTH = 600, 600







canvas=tk.Canvas(racine, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, bg="black")
annuler=tk.Button(racine, text="Annuler")
carre1=canvas.create_rectangle(0, 0, 50, 50, fill="red")
carre2=canvas.create_rectangle(50, 0, 100, 50, fill="blue")
carre3=canvas.create_rectangle(100, 0, 150, 50, fill="white")
cercle=canvas.create_oval(250, 250, 350, 350, fill="yellow")

def clic(event):
    x=event.x
    y=event.y
    canvas.create_oval(250, 250, 350, 350, fill="red")
    return

canvas.bind("<Button-1>", clic)

canvas.grid(column=0, row=1)
annuler.grid(column=1, row=1)














racine.mainloop()