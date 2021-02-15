import tkinter as tk

racine=tk.Tk()

def change_pixel_color(event):
    x = event.x
    y = event.y
    canvas.create_line((x,y), (x+1, y+1), fill="red")




canvas = tk.Canvas(racine, height=500, width=500, bg="black")
canvas.grid()
canvas.bind("<Button-1>", change_pixel_color)

racine.mainloop()