import turtle

wd = turtle.Screen() # criar uma janela
wd.title("Pong game") # titulo do programa
wd.bgcolor("black") # cor do background
wd.setup(width=800, height=600) # tamanho da janela
wd.tracer(0) # stop automatic screen updates e por isso temos q faze-lo manualmente
             # speed up um pouco o jogo

# raquete A
raquete_a = turtle.Turtle() # turtle object (turtle - module, Turtle - class)
raquete_a.speed(0) #  velocidade da animacao para o maximo
raquete_a.shape("square") # forma da raquete (retangular)
raquete_a.color("white") # cor da raquete (branca)
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup() # picks the pen up so the turtle does not draw a line as it moves
raquete_a.goto(-350, 0)

# raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Funcoes

# mover raquete A para cima
def raquete_a_up():
    y = raquete_a.ycor()
    y += 20
    raquete_a.sety(y)

# mover raquete A para baixo
def raquete_a_down():
    y = raquete_a.ycor()
    y -= 20
    raquete_a.sety(y)

# mover raquete B para cima
def raquete_b_up():
    y = raquete_b.ycor()
    y += 20
    raquete_b.sety(y)

# mover raquete B para baixo
def raquete_b_down():
    y = raquete_b.ycor()
    y -= 20
    raquete_b.sety(y)

wd.listen() # ouvir input no teclado
wd.onkeypress(raquete_a_up, "w") # se a tecla w tiver a ser pressionada corre a funcao raquete_a_up
wd.onkeypress(raquete_a_down, "s") # se a tecla s tiver a ser pressionada corre a funcao raquete_a_down
wd.onkeypress(raquete_b_up, "Up") # se a seta de cima tiver a ser pressionada corre a funcao raquete_b_up
wd.onkeypress(raquete_b_down, "Down") # se a seta de baixo tiver a ser pressionada corre a funcao raquete_b_down

# main game loop
while True:
    # sempre que o loop corre dá update ao screen
    wd.update()