import turtle

wd = turtle.Screen() # criar uma janela
wd.title("Pong game") # titulo do programa
wd.bgcolor("black") # cor do background
gameWidth = 800
gameHeight = 600
wd.setup(width=gameWidth, height=gameHeight) # tamanho da janela
wd.tracer(0) # stop automatic screen updates e por isso temos q faze-lo manualmente
             # speed up um pouco o jogo

# Raquete A
raquete_a = turtle.Turtle() # turtle object (turtle - module, Turtle - class)
raquete_a.speed(0) #  velocidade da animacao para o maximo
raquete_a.shape("square") # forma da raquete (retangular)
raquete_a.color("white") # cor da raquete (branca)
raquete_a.shapesize(stretch_wid=5, stretch_len=1) # tamanho do quadrado (raquete)
raquete_a.penup() # picks the pen up so the turtle does not draw a line as it moves
raquete_a.goto(-350, 0) # comeca nas coordenadas (-350; 0)

# Raquete B
raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.1
bola.dy = 0.1

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
wd.onkeypress(raquete_b_up, "Up") # se a seta para cima tiver a ser pressionada corre a funcao raquete_b_up
wd.onkeypress(raquete_b_down, "Down") # se a seta para baixo tiver a ser pressionada corre a funcao raquete_b_down

# Main game loop
while True:
    # debug
    print(bola.dx)
    print(bola.dy)

    # sempre que o loop corre dá update ao screen
    wd.update()

    # Mover a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Colisoes da bola com as raquetes
    # raquete A
    if (bola.xcor() > (raquete_b.xcor() - 20) and bola.xcor() < (raquete_b.xcor() + 20)) and (bola.ycor() < raquete_b.ycor() + 50 and bola.ycor() > raquete_b.ycor() - 50):
        bola.setx((raquete_b.xcor() - 20))
        bola.dx *= -1

    # raquete B
    if (bola.xcor() < (raquete_a.xcor() + 20) and bola.xcor() > bola.xcor() - 20) and (bola.ycor() < raquete_a.ycor() + 50 and bola.ycor() > raquete_a.ycor() - 50):
        bola.setx((raquete_a.xcor() + 20))
        bola.dx *= -1

    # Colisao com a barreira verticalmente (cima)
    if bola.ycor() > ((gameHeight) / 2) - 20:
        bola.sety(((gameHeight) / 2) - 20)
        bola.dy *= -1

    # Colisao com a barreira verticalmente (baixo)
    if bola.ycor() < (-(gameHeight) / 2) + 20:
        bola.sety((-(gameHeight) / 2) + 20)
        bola.dy *= -1

    # Colisao com a barreira horizontalmente (direita)
    if bola.xcor() > ((gameWidth) / 2) - 20:
        bola.goto(0, 0)
        bola.dx *= -1

    # Colisao com a barreira horizontalmente (esquerda)
    if bola.xcor() < (-(gameWidth) / 2) + 20:
        bola.goto(0, 0)
        bola.dx *= -1

    # Colisao entre as raquetes e a barreira
    # raquete A colisao cima
    if raquete_a.ycor() + 50 >= gameHeight / 2:
        raquete_a.sety((gameHeight / 2) - 50)

    # raquete A colisao baixo
    if raquete_a.ycor() - 50 <= -(gameHeight / 2):
        raquete_a.sety(-(gameHeight / 2) + 50)