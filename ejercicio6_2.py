import turtle
a = int(input("ingrese un numero para una figura : "))
t = turtle.Pen()
t.left(36)
#t.forward(50)

for x in range (1,a+1):
	t.forward(200)
	t.left(144)
	
turtle.getscreen()._root.mainloop()