import turtle
a = int(input("ingrese un numero para una figura : "))
t = turtle.Pen()

def micuadrado(size):
	for x in range(1, a+1):
		t.forward(size)
		t.left(90)
micuadrado(a)
turtle.getscreen()._root.mainloop()