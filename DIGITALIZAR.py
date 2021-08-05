from os import system
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image
import glob

###################################################################
# Modulo de DIGITALIZACION
# Enrique Buendia Lozada BUAP 2021
###################################################################

#
files = glob.glob("*.jpg")
# contador de puntos de control del metodo segmentario
cont = 0
# archivo con todas las coordenadas digitalizadas, mundo real
f = open('c_real.txt', 'a')


def on_press(event):
    try:
        global cont
        alto_real = 1000
        ancho_real = 1000
        xp = event.xdata
        yp = event.ydata
        xmax = 1000
        xmin = 0
        ymax = 1000
        ymin = 0
        print("En pantalla:", event.button, xp, yp)

        x = (xp/ancho_real)*(xmax-xmin)+xmin
        y = ((alto_real-yp)/alto_real)*(ymax-ymin)+ymin
        #np.append(pc, x, y)
        print("En real:", x, y)
        f.write(str(x))
        f.write('\n')
        f.write(str(y))
        f.write('\n')
        cont = cont+1
        print(cont)
        if cont >= 21:
            cont = 0
            plt.close()
    except:
        f.close(0)
        raise SystemExit('Adios...')


for imagen in files:
    # Tamaño de imagen a mostrar
    my_dpi = 96
    fig = plt.figure("Método segmentario BIOMECÁNICA EN CIENCIAS DE LA ACTIVIDAD FÍSICA Y DEPORTE",
                     figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
    fig.suptitle('Enrique Buendia, BUAP 2021:  Módulo Digitalizar \n Método segmentario para el cálculo del Cntro de grevedad corporal humano', fontsize=12)
    plt.text(0, 800, 'Puntos de control')

    # cambiar a coordenadas reales
    alto_real = 1000
    ancho_real = 1000

    img = Image.open(imagen)
    #updata = True

    plt.imshow(img, animated=True)

    fig.canvas.mpl_connect('button_press_event', on_press)
    plt.show()
