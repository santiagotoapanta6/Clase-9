import turtle
a = int(input("ingrese un numero para una figura : "))
t = turtle.Pen()

for x in range (1,a+1):
	t.forward(50)
	n=360/a
	t.left(n)

turtle.getscreen()._root.mainloop()