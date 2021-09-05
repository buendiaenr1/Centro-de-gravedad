import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image
import win32api

import math

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


def angulo(a, b, c):
    ang = math.degrees(math.atan2(
        c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang


def on_press2(event):
    try:

        global contt, aa, bb, cc

        alto_real = 1000
        ancho_real = 1000
        xp = event.xdata
        yp = event.ydata
        xmax = 1000
        xmin = 0
        ymax = 1000
        ymin = 0
        print("En pantalla:", event.button, xp, yp)
        if event.button == 'MouseButton.MIDDLE':
            exit(0)
        x = (xp/ancho_real)*(xmax-xmin)+xmin
        y = ((alto_real-yp)/alto_real)*(ymax-ymin)+ymin
        #np.append(pc, x, y)
        #print("En real:", x, y)
        if contt == 0:
            aa.append(x)
            aa.append(y)
            contt = contt+1
        elif contt == 1:
            bb.append(x)
            bb.append(y)
            contt = contt+1
        else:
            #contt == 2
            cc.append(x)
            cc.append(y)
            contt = 0
            c_angulo = str(angulo(aa, bb, cc))
            win32api.MessageBox(0, c_angulo, 'Angulo Digitalizado')
            aa = []
            bb = []
            cc = []

    except:
        #raise SystemExit()
        contt = 0
        #c_angulo = str(angulo(aa, bb, cc))
        #win32api.MessageBox(0, c_angulo, 'Angulo Digitalizado')
        aa = []
        bb = []
        cc = []


contt = 0
aa = []
bb = []
cc = []
# Tamaño de imagen a mostrar
my_dpi = 96
fig = plt.figure("Método segmentario BIOMECÁNICA EN CIENCIAS DE LA ACTIVIDAD FÍSICA Y DEPORTE",
                 figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
fig.suptitle('Enrique Buendia, BUAP 2021:  Módulo Digitalizar', fontsize=12)

# cambiar a coordenadas reales
alto_real = 1000
ancho_real = 1000


filetypes = (
    ('Text files', '*.jpg'),
    ('All files', '*.*'),
)
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file
filename = askopenfilename(title='Seleccionar archivo de imagen...',
                           filetypes=filetypes)
print(filename)
img = Image.open(filename)
#updata = True

plt.imshow(img, animated=True)

fig.canvas.mpl_connect('button_press_event', on_press2)
plt.show()
