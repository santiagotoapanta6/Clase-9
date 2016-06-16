from Tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 800, height = 400)
canvas.pack()

my_image = PhotoImage(file = "ball.gif")
canvas.create_image(10, 10, ancho= NW, image = my_image)
tk.mainloop()