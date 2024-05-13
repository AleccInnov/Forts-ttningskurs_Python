import tkinter

root = tkinter.Tk()

# create canvas
my_canvas = tkinter.Canvas(root, bg="white", height=300, width=300)

# draw arcs
coord = 10, 10, 300, 300
arc = my_canvas.create_arc(coord, start=0, extent=150, fill="red")
arc2 = my_canvas.create_arc(coord, start=150, extent=210, fill="green")

my_canvas.pack()

root.mainloop()
