from tkinter import *
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image
import win32api
import sys

import math

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import tkinter as tk

from matplotlib.widgets import TextBox
from tkinter import messagebox as MessageBox


def angulo(a, b, c):
    ang = math.degrees(math.atan2(
        c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang


def on_press2(event):

    try:

        global contt, aa, bb, cc, dd
        global real

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
        x = xp
        y = yp
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
        elif contt == 2:
            cc.append(x)
            cc.append(y)
            contt = contt+1
        else:
            dd.append(x)
            dd.append(y)
            contt = 0
            print('....')
            ax = float(aa[0])
            ay = float(aa[1])
            bx = float(bb[0])
            by = float(bb[1])
            cx = float(cc[0])
            cy = float(cc[1])
            dx = float(dd[0])
            dy = float(dd[1])
            dab = ((ax - bx) ** 2 + (ay-by) ** 2) ** (0.5)
            dcd = ((cx-dx) ** 2 + (cy-dy) ** 2) ** (0.5)
            dis = (dcd * float(real))/dab
            print("Distancia estimada : ", dis)
            root = Tk()

            def test():
                MessageBox.showinfo("Distancia estimada",
                                    dis)  # título, mensaje

            def callback():
                plt.close()
                root.destroy()
                sys.exit()

            Button(root, text="Mostrar distancia", command=test).pack()
            Button(root, text="Salir", command=callback).pack()
            root.mainloop()
            aa = []
            bb = []
            cc = []
            dd = []

    except:
        #raise SystemExit()
        contt = 0
        #c_angulo = str(angulo(aa, bb, cc))
        #win32api.MessageBox(0, c_angulo, 'Angulo Digitalizado')
        aa = []
        bb = []
        cc = []
        dd = []


contt = 0
aa = []
bb = []
cc = []
dd = []
# Tamaño de imagen a mostrar
my_dpi = 96
fig = plt.figure("Método segmentario BIOMECÁNICA EN CIENCIAS DE LA ACTIVIDAD FÍSICA Y DEPORTE",
                 figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
fig.suptitle('Enrique Buendia, BUAP 2021:  Módulo Estimar Distancia \n\n1: definir dos puntos para el objeto de referencia (OR) \n2: luego otros dos puntos para saber su distancia', fontsize=12)

# cambiar a coordenadas reales
alto_real = 1000
ancho_real = 1000

# leer distancia real del objeto de referencia

root = Tk()

real = ""


def retrieve_input():
    global real
    inputValue = textBox.get("1.0", "end-1c")
    print(inputValue)
    real = inputValue


textBox = Text(root, height=1, width=40)
textBox.pack()
root.title('Al registrar cierre la ventana')
buttonCommit = Button(root, height=1, width=60, text="Registrar medida real del objeto de refrencia",
                      command=lambda: retrieve_input())
# command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()


mainloop()

# leer imagen
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
initial_text = real
axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, 'OR real= ', initial=initial_text)

fig.canvas.mpl_connect('button_press_event', on_press2)


plt.show()
