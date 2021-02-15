import tkinter as tk

racine=tk.Tk()

def color_cercle(event):
    x = event.x
    y = event.y
    if x<250 :
        canvas.create_oval((x,y), (x+50, y+50), fill="blue")
    else :
        canvas.create_oval((x,y), (x+50, y+50), fill="red")



canvas = tk.Canvas(racine, height=500, width=500, bg="black")
ligne_blanche = canvas.create_line(250, 0, 250, 500, fill="white")
canvas.grid()
canvas.bind("<Button-1>", color_cercle)

racine.mainloop()