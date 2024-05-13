import tkinter as tk

def start_move(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def move_text(event):
    global start_x, start_y
    delta_x = event.x - start_x
    delta_y = event.y - start_y
    canvas.move(text_id, delta_x, delta_y)
    start_x, start_y = event.x, event.y

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

text_id = canvas.create_text(150, 100, text="Dra mig!", font=("Arial", 12), fill="black")

canvas.tag_bind(text_id, "<Button-1>", start_move)
canvas.tag_bind(text_id, "<B1-Motion>", move_text)

root.mainloop()
