import pygame
import random
import math
import time

# Variables globales (columnas, filas y las matrices)
r = 50
c = 50
mat = []
nuevo = []


# Matriz nueva
def matriz(r, c, mat):
    for i in range(r):
        mat.append([])
        for j in range(c):
            ran = random.randint(0, 1)
            mat[i].append(ran)


# La segunda matriz
def fresh(nuevo, r, c):
    for i in range(r):
        nuevo.append([])
        for j in range(c):
            nuevo[i].append(0)


# Lleno de 0s la segunda matriz y así borrar las celdas vivas del juego
def clear(nuevo, r, c):
    for i in range(r):
        for j in range(c):
            nuevo[i][j] = 0

def clear_pause (mat, r, c):
    for i in range(r):
        for j in range(c):
            mat[i][j] = 0

# En esta matriz se cuentan los vecinos vivos de cada celda en 1 matriz y se almacen el valor con las reglas aplicadas en La segunda matriz
def vivos(r, c, mat, nuevo):
    for i in range(r):
        for j in range(c):
            s = 0
            state = mat[i][j]

            x = ((j - 1 + c) % c)
            y = ((i - 1 + c) % r)
            x1 = ((j + 1 + c) % c)
            y1 = ((i + 1 + c) % r)
            s = s + mat[y][x]
            s = s + mat[i][x]
            s = s + mat[y1][x]
            s = s + mat[y1][j]
            s = s + mat[y1][x1]
            s = s + mat[i][x1]
            s = s + mat[y][x1]
            s = s + mat[y][j]
            # Reglas del juego
            if (state == 0):  # Revivir
                if ((s == 3)):
                    nuevo[i][j] = 1

            elif (state == 1 and (s < 2 or s > 3)):  # Matar
                nuevo[i][j] = 0
            # Si no sucede ninunga regla, el estado de la celda es el mismo
            else:
                nuevo[i][j] = state


# Aquí hago un reset para hacer que la primera matriz y la segunda hagan un ciclo entre si y las celdas con las reglas se sustituyan en la primera matriz para volver a verificar el siguiente frame.
def reg(nuevo, mat, r, c):
    for i in range(r):
        for j in range(c):
            mat[i][j] = nuevo[i][j]


# Una figura prediseñada que es un deslizador o "glider"
def glider(nuevo):
    nuevo[4][2] = 1

    nuevo[2][3] = 1
    nuevo[4][3] = 1

    nuevo[3][4] = 1
    nuevo[4][4] = 1


# Con esta función le doy el color y hago la interfaz gráfcia basada en la segunda matriz
def color(mat, r, c, nuevo):
    blue = (0, 255, 255)
    white = (128, 128, 128)
    width = 9
    height = 9
    for i in range(r):
        for j in range(c):
            x = j * 10
            y = i * 10
            if (nuevo[i][j] == 1):  # Si la celda esta viva (Con valor de 1) se colorea de azul su cuadrado
                pygame.draw.rect(win, blue, (x, y, width, height))

            # Si la celda está muerta (Con valor de 0) se colorea de griz su cuadrado
            else:
                pygame.draw.rect(win, white, (x, y, width, height))


# Aquí uso el click izquierdo y las coordennadas del raton para poder crear a voluntad nuevas celdas
def boton(mat):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (mouse[0] < 500 and mouse[1] < 500):
        if (click[0] == 1):  # Verifico si mi mouse esta en una coordenada de mi matriz y si estoy haciendo click y así cambiar el valor de celda
            y = math.floor((mouse[0]) / 10)
            x = math.floor((mouse[1]) / 10)
            if (mat[x][y] == 0):
                mat[x][y] = 1
            else:
                mat[x][y] = 0


    pygame.display.update()


# Es la función donde se pone pausa al programa y mientras puedo seguir coloreando y agragar nuevas celdas
def pause():
    pausa = True
    while pausa:
        keys = pygame.key.get_pressed()
        boton(mat)
        color(mat, r, c, nuevo)
        if (keys[pygame.K_g]):  # si presiono la "k" puedo poner un 'glider' ya hecho
            glider(nuevo)
        if (keys[pygame.K_c]):  # si presiono la "c" puedo borrar el trablero
            clear_pause(mat, r, c)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()  # Si doy click al boton de seguir el valor de la pausa es vuelve falso y regreso al ciclo principal
        if (mouse[0] > 260 and mouse[0] < 310):
            if (mouse[1] > 510 and mouse[1] < 535):
                if (click[0] == 1):
                    pausa = False

        pygame.display.update()


# Aquí llamo la función de pausa cuando doy click en el area del botón
def botonpausa():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (mouse[0] > 190 and mouse[0] < 240):
        if (mouse[1] > 510 and mouse[1] < 535):
            if (click[0] == 1):
                pause()

    pygame.display.update()


# Llamo las funciones afuera del ciclo principal para que se creen las matrices principales
matriz(r, c, mat)
fresh(nuevo, r, c)

# Aquí se inicia le ciclo de pygame
pygame.init()
# Tamaño y nombre de la ventana
win = pygame.display.set_mode((500, 550))
pygame.display.set_caption("Juego de la Vida")

# Aquí dibujo los rectangulos y textos, ya sea para el menú o para los botones
pygame.draw.rect(win, (8, 204, 126), (260, 510, 50, 25))  # pausa
mifuente = pygame.font.SysFont("Times New Roman", 15)
fuente = pygame.font.SysFont("Arial", 12)  # instrucc
pau = mifuente.render("Pausa", 0, (0, 0, 0))
pygame.draw.rect(win, (203, 42, 8), (190, 510, 50, 25))  # resume
con = mifuente.render("Seguir", 0, (0, 0, 0))

glid = fuente.render("G : Glider", 0, (255, 0, 0))
cle = fuente.render("C : Clear", 0, (255, 0, 0))

mas = fuente.render("Vel +: ↑", 0, (255, 0, 0))
menos = fuente.render("vel -: ↓", 0, (255, 0, 0))

run = True
delay = 100
while run:
    keys = pygame.key.get_pressed()

    # Si uso las flechas de arriba o abajo, aumento o disminuyo los fps modificando el delay del programa
    if (keys[pygame.K_DOWN]):
        delay = delay + 50
    if (keys[pygame.K_UP]):
        delay = delay - 50

    pygame.time.delay(delay)
    d = str(delay)

    # Si cierro la ventana, el programa dejara de correr
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
    # Aqui llamo a todas las funciones que hacen funcional al juego dentreo de un ciclo que no termina hasta que cierre la ventana
    botonpausa()
    # textos de los botones y menu
    win.blit(pau, (195, 515))
    win.blit(con, (266, 515))
    win.blit(cle, (20, 505))
    win.blit(glid, (20, 520))
    win.blit(mas, (400, 505))
    win.blit(menos, (400, 520))

    pygame.display.update()
    vivos(r, c, mat, nuevo)

    if (keys[pygame.K_c]):
        clear(nuevo, r, c)

    reg(nuevo, mat, r, c)  # si presiono la "c" puedo borrar el trablero
    boton(mat)
    if (keys[pygame.K_g]):  # si presiono la "k" puedo poner un 'glider' ya hecho
        glider(nuevo)

    color(mat, r, c, nuevo)
    botonpausa()
    pygame.display.update()

pygame.quit()
