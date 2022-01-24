import turtle

wd = turtle.Screen() #criar uma janela
wd.title("Pong game") #titulo do programa
wd.bgcolor("black") #cor do background
wd.setup(width=800, height=600) #tamanho da janela
wd.tracer(0) #Stop automatic screen updates e por isso temos q faze-lo manualmente
             #Speed up um pouco o jogo

#Main game loop
while True:
    #Sempre que o loop corre dá update ao screen
    wd.update()