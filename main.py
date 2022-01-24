import turtle

wd = turtle.Screen() #criar uma janela
wd.title("Pong game") #titulo do programa
wd.bgcolor("black") #cor do background
wd.setup(width=800, height=600) #tamanho da janela
wd.tracer(0) #stop automatic screen updates e por isso temos q faze-lo manualmente
             #speed up um pouco o jogo

# Paddle A
paddle_a = turtle.Turtle() #turtle object (turtle - module, Turtle - class)
paddle_a.speed(0) # velocidade da animacao para o maximo
paddle_a.shape("square") #forma da raquete (retangular)
paddle_a.color("white") #cor da raquete (branca)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #picks the pen up so the turtle does not draw a line as it moves
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#main game loop
while True:
    #sempre que o loop corre dá update ao screen
    wd.update()