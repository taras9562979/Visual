import tkinter as tk
import math

nodes = []
flag_mode = False

def get_left_click(event):
    global flag_mode
    if not flag_mode:
        x = event.x
        y = event.y
        radius = 10
        print('Left Click ->  ',x,y)
        canvas.create_oval(x-radius,y-radius,x+radius,y+radius,fill='red')
        nodes.append((x,y))
    
        print('Nodes ->  ',nodes)

field = tk.Tk()
field.title('GRAPH VISUALIZATION')

canvas = tk.Canvas(field,width=1600,height=1000,bg='white')
canvas.pack()

field.bind('<Button-1>',get_left_click)

field.mainloop()
