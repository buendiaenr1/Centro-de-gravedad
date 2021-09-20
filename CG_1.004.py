import tkinter as tk
import win32api
import cv2
import math
from os import system
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image
import glob


import pandas as pd

import os

import datetime
import sys
import subprocess

#############################################################################################
######
# Sistema de Análisis de Biomecánico   por el método segmentario
# Enrique R.P. Buendia Lozada
# Benemérita Universidad Autónoma de Puebla
# México  [Otoño 2021]
######
#############################################################################################

#############################################################################################
# angulo de tres puntos     (código separado)
# estimar distancias        (código separado)
#############################################################################################


def angulo(a, b, c):
    ang = math.degrees(math.atan2(
        c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang


def v_angulos():
    subprocess.call([sys.executable, 'tang_v1.py', 'argument1'])


def v_dist():
    subprocess.call([sys.executable, 'dist.py', 'argument1'])

############################################################################################
# Módulo Machote de calculo del Centro de gravedad
# Enrique Buendia Lozada Otoño 2021
############################################################################################


def model():
    files = glob.glob("*.jpg")

    x = []
    y = []
    cont = 1
    cont2 = 1
    # with open("/home/decodigo/Documentos/archivos_ejemplo/filename.txt","r") as archivo:
    with open("c_real.txt", "r") as archivo:
        for linea in archivo:
            # print(float(linea))
            num = float(linea)
            if cont % 2 == 0:  # par
                y.append(num)
            else:
                x.append(num)
            cont = cont+1

    print(x)
    print(y)
    print("Longitud digital:", cont)

    fang = open('angulos.txt', 'a')
    salto = 0      # saltar grupos de 21 datos para cada imagen

    for imagen in files:
        print("Imagen: ", imagen)
        dfmx = pd.DataFrame()

        dfmx['x1'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['x2'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['longitud'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['pl'] = [0.5976, 0.4486, 0.5772, 0.4574, 0.79, 0.5772,
                      0.4574, 0.79, 0.4095, 0.4459, 0.4415, 0.4095, 0.4459, 0.4415]
        dfmx['dp'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['dec'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['pp'] = [0.0694, 0.4346, 0.0271, 0.0162, 0.0061, 0.0271,
                      0.0162, 0.0061, 0.1416, 0.0433, 0.0137, 0.1416, 0.0433, 0.0137]
        dfmx['momento'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # print(dfmx)

        dfmy = pd.DataFrame()

        dfmy['y1'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['y2'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['longitud'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['pl'] = [0.5976, 0.4486, 0.5772, 0.4574, 0.79, 0.5772,
                      0.4574, 0.79, 0.4095, 0.4459, 0.4415, 0.4095, 0.4459, 0.4415]
        dfmy['dp'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['dec'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['pp'] = [0.0694, 0.4346, 0.0271, 0.0162, 0.0061, 0.0271,
                      0.0162, 0.0061, 0.1416, 0.0433, 0.0137, 0.1416, 0.0433, 0.0137]
        dfmy['momento'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # print(dfmy)

        ###############################################
        # Módulo graficar modelo de alambre
        # Enrique Buendia otoño 2021
        ###############################################

        # y1 = [5, 10]
        # x1 = [10, 20]
        # plt.plot(x1, y1, color="c")
        # plt.show()

        # ----->>>>> ANGULOS  a un archivo
        fang.write(imagen)
        fang.write("\n")
        ag1 = []
        ag2 = []
        ag3 = []
        ag1.append(x[3+salto])
        ag1.append(y[3+salto])
        ag2.append(x[13+salto])
        ag2.append(y[13+salto])
        ag3.append(x[14+salto])
        ag3.append(y[14+salto])
        fang.write("angulo ....en rodilla derecha: ")
        fang.write(str(angulo(ag1, ag2, ag3)))
        fang.write("\n")

        ag1 = []
        ag2 = []
        ag3 = []
        ag1.append(x[4+salto])
        ag1.append(y[4+salto])
        ag2.append(x[17+salto])
        ag2.append(y[17+salto])
        ag3.append(x[18+salto])
        ag3.append(y[18+salto])
        fang.write("angulo ....en rodilla izquierda: ")
        fang.write(str(angulo(ag1, ag2, ag3)))
        fang.write("\n")

        ag1 = []
        ag2 = []
        ag3 = []
        ag1.append(x[5+salto])
        ag1.append(y[5+salto])
        ag2.append(x[6+salto])
        ag2.append(y[6+salto])
        ag3.append(x[7+salto])
        ag3.append(y[7+salto])
        fang.write("angulo ....en codo derecho: ")
        fang.write(str(angulo(ag1, ag2, ag3)))
        fang.write("\n")

        ag1 = []
        ag2 = []
        ag3 = []
        ag1.append(x[9+salto])
        ag1.append(y[9+salto])
        ag2.append(x[10+salto])
        ag2.append(y[10+salto])
        ag3.append(x[11+salto])
        ag3.append(y[11+salto])
        fang.write("angulo ....en codo izquierdo: ")
        fang.write(str(angulo(ag1, ag2, ag3)))
        fang.write("\n")

        ag1 = []
        ag2 = []
        ag3 = []
        # pm caderas
        pmcx = (x[3+salto]+x[4+salto])/2
        pmcy = (y[3+salto]+y[4+salto])/2
        xii = (-pmcy/(y[3+salto]-pmcy))*(x[3+salto]-pmcx) + \
            pmcx  # intersección con eje x

        ag1.append(x[2+salto])  # supraesternal
        ag1.append(y[2+salto])
        ag2.append(xii)
        ag2.append(0.0)
        ag3.append(x[2+salto])  # x de supraesternal, proyección en x (piso)
        ag3.append(0)
        fang.write("angulo ....en tronco suponiendo piso paralelo al eje x: ")
        fang.write(str(angulo(ag1, ag2, ag3)))
        fang.write("\n")
        fang.write("\n")
        # ------>>>>>>>

        # modelo de alambre
        # cabeza
        x2 = []
        y2 = []
        x2.append(x[0+salto])
        y2.append(y[0+salto])
        x2.append(x[1+salto])
        y2.append(y[1+salto])
        plt.plot(x2, y2, color="c")
        # clavicula derecha
        x2 = []
        y2 = []
        x2.append(x[2+salto])
        y2.append(y[2+salto])
        x2.append(x[5+salto])
        y2.append(y[5+salto])
        plt.plot(x2, y2, color="c")
        # antebrazo derecho
        x2 = []
        y2 = []
        x2.append(x[5+salto])
        y2.append(y[5+salto])
        x2.append(x[6+salto])
        y2.append(y[6+salto])
        plt.plot(x2, y2, color="c")
        # brazo derecho
        x2 = []
        y2 = []
        x2.append(x[6+salto])
        y2.append(y[6+salto])
        x2.append(x[7+salto])
        y2.append(y[7+salto])
        plt.plot(x2, y2, color="c")
        # mano derecha
        x2 = []
        y2 = []
        x2.append(x[7+salto])
        y2.append(y[7+salto])
        x2.append(x[8+salto])
        y2.append(y[8+salto])
        plt.plot(x2, y2, color="c")

        # claviculo izquierda
        x2 = []
        y2 = []
        x2.append(x[2+salto])
        y2.append(y[2+salto])
        x2.append(x[9+salto])
        y2.append(y[9+salto])
        plt.plot(x2, y2, color="c")
        # antebrazo izquierdo
        x2 = []
        y2 = []
        x2.append(x[9+salto])
        y2.append(y[9+salto])
        x2.append(x[10+salto])
        y2.append(y[10+salto])
        plt.plot(x2, y2, color="c")
        # brazo izquierdo
        x2 = []
        y2 = []
        x2.append(x[10+salto])
        y2.append(y[10+salto])
        x2.append(x[11+salto])
        y2.append(y[11+salto])
        plt.plot(x2, y2, color="c")
        # mano izquierda
        x2 = []
        y2 = []
        x2.append(x[11+salto])
        y2.append(y[11+salto])
        x2.append(x[12+salto])
        y2.append(y[12+salto])
        plt.plot(x2, y2, color="c")

        # caderas
        x2 = []
        y2 = []
        x2.append(x[3+salto])
        y2.append(y[3+salto])
        x2.append(x[4+salto])
        y2.append(y[4+salto])
        plt.plot(x2, y2, color="c")
        # femur derecho
        x2 = []
        y2 = []
        x2.append(x[3+salto])
        y2.append(y[3+salto])
        x2.append(x[13+salto])
        y2.append(y[13+salto])
        plt.plot(x2, y2, color="c")
        # pierna derecha
        x2 = []
        y2 = []
        x2.append(x[13+salto])
        y2.append(y[13+salto])
        x2.append(x[14+salto])
        y2.append(y[14+salto])
        plt.plot(x2, y2, color="c")
        # talon derecho
        x2 = []
        y2 = []
        x2.append(x[14+salto])
        y2.append(y[14+salto])
        x2.append(x[15+salto])
        y2.append(y[15+salto])
        plt.plot(x2, y2, color="c")
        # pie derecho
        x2 = []
        y2 = []
        x2.append(x[15+salto])
        y2.append(y[15+salto])
        x2.append(x[16+salto])
        y2.append(y[16+salto])
        plt.plot(x2, y2, color="c")
        # femur izquierdo
        x2 = []
        y2 = []
        #############
        x2.append(x[4+salto])
        y2.append(y[4+salto])
        x2.append(x[17+salto])
        y2.append(y[17+salto])
        plt.plot(x2, y2, color="c")
        # pierna izquierda
        x2 = []
        y2 = []
        x2.append(x[17+salto])
        y2.append(y[17+salto])
        x2.append(x[18+salto])
        y2.append(y[18+salto])
        plt.plot(x2, y2, color="c")
        # talon izquierdo
        x2 = []
        y2 = []
        x2.append(x[18+salto])
        y2.append(y[18+salto])
        x2.append(x[19+salto])
        y2.append(y[19+salto])
        plt.plot(x2, y2, color="c")
        # pie izquierdo
        x2 = []
        y2 = []
        x2.append(x[19+salto])
        y2.append(y[19+salto])
        x2.append(x[20+salto])
        y2.append(y[20+salto])
        plt.plot(x2, y2, color="c")
        # pm caderas
        pmcx = (x[3+salto]+x[4+salto])/2
        pmcy = (y[3+salto]+y[4+salto])/2
        # tronco
        x2 = []
        y2 = []
        x2.append(x[2+salto])
        y2.append(y[2+salto])
        x2.append(pmcx)
        y2.append(pmcy)
        plt.plot(x2, y2, color="c")

        #######################################################################
        # Módulo de calculo del Centro de Gravedad por el método segmentario
        #######################################################################
        dfmx = pd.DataFrame()

        dfmx['x1'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['x2'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['longitud'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['pl'] = [0.5976, 0.4486, 0.5772, 0.4574, 0.79, 0.5772,
                      0.4574, 0.79, 0.4095, 0.4459, 0.4415, 0.4095, 0.4459, 0.4415]
        dfmx['dp'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['dec'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmx['pp'] = [0.0694, 0.4346, 0.0271, 0.0162, 0.0061, 0.0271,
                      0.0162, 0.0061, 0.1416, 0.0433, 0.0137, 0.1416, 0.0433, 0.0137]
        dfmx['momento'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # print(dfmx)

        dfmy = pd.DataFrame()

        dfmy['y1'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['y2'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['longitud'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['pl'] = [0.5976, 0.4486, 0.5772, 0.4574, 0.79, 0.5772,
                      0.4574, 0.79, 0.4095, 0.4459, 0.4415, 0.4095, 0.4459, 0.4415]
        dfmy['dp'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['dec'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dfmy['pp'] = [0.0694, 0.4346, 0.0271, 0.0162, 0.0061, 0.0271,
                      0.0162, 0.0061, 0.1416, 0.0433, 0.0137, 0.1416, 0.0433, 0.0137]
        dfmy['momento'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # print(dfmy)

        dfmx.at[0, 'x1'] = x[0+salto]
        dfmx.at[1, 'x1'] = x[2+salto]
        dfmx.at[2, 'x1'] = x[5+salto]
        dfmx.at[3, 'x1'] = x[6+salto]
        dfmx.at[4, 'x1'] = x[7+salto]
        dfmx.at[5, 'x1'] = x[9+salto]
        dfmx.at[6, 'x1'] = x[10+salto]
        dfmx.at[7, 'x1'] = x[11+salto]
        dfmx.at[8, 'x1'] = x[3+salto]
        dfmx.at[9, 'x1'] = x[13+salto]
        dfmx.at[10, 'x1'] = x[15+salto]
        dfmx.at[11, 'x1'] = x[4+salto]
        dfmx.at[12, 'x1'] = x[17+salto]
        dfmx.at[13, 'x1'] = x[19+salto]

        dfmx.at[0, 'x2'] = x[1+salto]
        dfmx.at[1, 'x2'] = pmcx
        dfmx.at[2, 'x2'] = x[6+salto]
        dfmx.at[3, 'x2'] = x[7+salto]
        dfmx.at[4, 'x2'] = x[8+salto]
        dfmx.at[5, 'x2'] = x[10+salto]
        dfmx.at[6, 'x2'] = x[11+salto]
        dfmx.at[7, 'x2'] = x[12+salto]
        dfmx.at[8, 'x2'] = x[13+salto]
        dfmx.at[9, 'x2'] = x[14+salto]
        dfmx.at[10, 'x2'] = x[16+salto]
        dfmx.at[11, 'x2'] = x[17+salto]
        dfmx.at[12, 'x2'] = x[18+salto]
        dfmx.at[13, 'x2'] = x[20+salto]

        # print(dfmx)

        # 3a columna
        dfmx.at[0, 'longitud'] = abs(dfmx['x1'].loc[0] - dfmx['x2'].loc[0])
        dfmx.at[1, 'longitud'] = abs(dfmx['x1'].loc[1] - dfmx['x2'].loc[1])
        dfmx.at[2, 'longitud'] = abs(dfmx['x1'].loc[2] - dfmx['x2'].loc[2])
        dfmx.at[3, 'longitud'] = abs(dfmx['x1'].loc[3] - dfmx['x2'].loc[3])
        dfmx.at[4, 'longitud'] = abs(dfmx['x1'].loc[4] - dfmx['x2'].loc[4])
        dfmx.at[5, 'longitud'] = abs(dfmx['x1'].loc[5] - dfmx['x2'].loc[5])
        dfmx.at[6, 'longitud'] = abs(dfmx['x1'].loc[6] - dfmx['x2'].loc[6])
        dfmx.at[7, 'longitud'] = abs(dfmx['x1'].loc[7] - dfmx['x2'].loc[7])
        dfmx.at[8, 'longitud'] = abs(dfmx['x1'].loc[8] - dfmx['x2'].loc[8])
        dfmx.at[9, 'longitud'] = abs(dfmx['x1'].loc[9] - dfmx['x2'].loc[9])
        dfmx.at[10, 'longitud'] = abs(dfmx['x1'].loc[10] - dfmx['x2'].loc[10])
        dfmx.at[11, 'longitud'] = abs(dfmx['x1'].loc[11] - dfmx['x2'].loc[11])
        dfmx.at[12, 'longitud'] = abs(dfmx['x1'].loc[12] - dfmx['x2'].loc[12])
        dfmx.at[13, 'longitud'] = abs(dfmx['x1'].loc[13] - dfmx['x2'].loc[13])

        # 5a columna
        dfmx.at[0, 'dp'] = (dfmx['longitud'].loc[0] * dfmx['pl'].loc[0])
        dfmx.at[1, 'dp'] = (dfmx['longitud'].loc[1] * dfmx['pl'].loc[1])
        dfmx.at[2, 'dp'] = (dfmx['longitud'].loc[2] * dfmx['pl'].loc[2])
        dfmx.at[3, 'dp'] = (dfmx['longitud'].loc[3] * dfmx['pl'].loc[3])
        dfmx.at[4, 'dp'] = (dfmx['longitud'].loc[4] * dfmx['pl'].loc[4])
        dfmx.at[5, 'dp'] = (dfmx['longitud'].loc[5] * dfmx['pl'].loc[5])
        dfmx.at[6, 'dp'] = (dfmx['longitud'].loc[6] * dfmx['pl'].loc[6])
        dfmx.at[7, 'dp'] = (dfmx['longitud'].loc[7] * dfmx['pl'].loc[7])
        dfmx.at[8, 'dp'] = (dfmx['longitud'].loc[8] * dfmx['pl'].loc[8])
        dfmx.at[9, 'dp'] = (dfmx['longitud'].loc[9] * dfmx['pl'].loc[9])
        dfmx.at[10, 'dp'] = (dfmx['longitud'].loc[10] * dfmx['pl'].loc[10])
        dfmx.at[11, 'dp'] = (dfmx['longitud'].loc[11] * dfmx['pl'].loc[11])
        dfmx.at[12, 'dp'] = (dfmx['longitud'].loc[12] * dfmx['pl'].loc[12])
        dfmx.at[13, 'dp'] = (dfmx['longitud'].loc[13] * dfmx['pl'].loc[13])

        # 6a columna
        if dfmx['x1'].loc[0] <= dfmx['x2'].loc[0]:
            dfmx.at[0, 'dec'] = dfmx['x1'].loc[0] + dfmx['dp'].loc[0]
        else:
            dfmx.at[0, 'dec'] = dfmx['x1'].loc[0] - dfmx['dp'].loc[0]

        if dfmx['x1'].loc[1] <= dfmx['x2'].loc[1]:
            dfmx.at[1, 'dec'] = dfmx['x1'].loc[1] + dfmx['dp'].loc[1]
        else:
            dfmx.at[1, 'dec'] = dfmx['x1'].loc[1] - dfmx['dp'].loc[1]

        if dfmx['x1'].loc[2] <= dfmx['x2'].loc[2]:
            dfmx.at[2, 'dec'] = dfmx['x1'].loc[2] + dfmx['dp'].loc[2]
        else:
            dfmx.at[2, 'dec'] = dfmx['x1'].loc[2] - dfmx['dp'].loc[2]

        if dfmx['x1'].loc[3] <= dfmx['x2'].loc[3]:
            dfmx.at[3, 'dec'] = dfmx['x1'].loc[3] + dfmx['dp'].loc[3]
        else:
            dfmx.at[3, 'dec'] = dfmx['x1'].loc[3] - dfmx['dp'].loc[3]

        if dfmx['x1'].loc[4] <= dfmx['x2'].loc[4]:
            dfmx.at[4, 'dec'] = dfmx['x1'].loc[4] + dfmx['dp'].loc[4]
        else:
            dfmx.at[4, 'dec'] = dfmx['x1'].loc[4] - dfmx['dp'].loc[4]

        if dfmx['x1'].loc[5] <= dfmx['x2'].loc[5]:
            dfmx.at[5, 'dec'] = dfmx['x1'].loc[5] + dfmx['dp'].loc[5]
        else:
            dfmx.at[5, 'dec'] = dfmx['x1'].loc[5] - dfmx['dp'].loc[5]

        if dfmx['x1'].loc[6] <= dfmx['x2'].loc[6]:
            dfmx.at[6, 'dec'] = dfmx['x1'].loc[6] + dfmx['dp'].loc[6]
        else:
            dfmx.at[6, 'dec'] = dfmx['x1'].loc[6] - dfmx['dp'].loc[6]

        if dfmx['x1'].loc[7] <= dfmx['x2'].loc[7]:
            dfmx.at[7, 'dec'] = dfmx['x1'].loc[7] + dfmx['dp'].loc[7]
        else:
            dfmx.at[7, 'dec'] = dfmx['x1'].loc[7] - dfmx['dp'].loc[7]

        if dfmx['x1'].loc[8] <= dfmx['x2'].loc[8]:
            dfmx.at[8, 'dec'] = dfmx['x1'].loc[8] + dfmx['dp'].loc[8]
        else:
            dfmx.at[8, 'dec'] = dfmx['x1'].loc[8] - dfmx['dp'].loc[8]

        if dfmx['x1'].loc[9] <= dfmx['x2'].loc[9]:
            dfmx.at[9, 'dec'] = dfmx['x1'].loc[9] + dfmx['dp'].loc[9]
        else:
            dfmx.at[9, 'dec'] = dfmx['x1'].loc[9] - dfmx['dp'].loc[9]

        if dfmx['x1'].loc[10] <= dfmx['x2'].loc[10]:
            dfmx.at[10, 'dec'] = dfmx['x1'].loc[10] + dfmx['dp'].loc[10]
        else:
            dfmx.at[10, 'dec'] = dfmx['x1'].loc[10] - dfmx['dp'].loc[10]

        if dfmx['x1'].loc[11] <= dfmx['x2'].loc[11]:
            dfmx.at[11, 'dec'] = dfmx['x1'].loc[11] + dfmx['dp'].loc[11]
        else:
            dfmx.at[11, 'dec'] = dfmx['x1'].loc[11] - dfmx['dp'].loc[11]

        if dfmx['x1'].loc[12] <= dfmx['x2'].loc[12]:
            dfmx.at[12, 'dec'] = dfmx['x1'].loc[12] + dfmx['dp'].loc[12]
        else:
            dfmx.at[12, 'dec'] = dfmx['x1'].loc[12] - dfmx['dp'].loc[12]

        if dfmx['x1'].loc[13] <= dfmx['x2'].loc[13]:
            dfmx.at[13, 'dec'] = dfmx['x1'].loc[13] + dfmx['dp'].loc[13]
        else:
            dfmx.at[13, 'dec'] = dfmx['x1'].loc[13] - dfmx['dp'].loc[13]

        # 8a columna
        dfmx.at[0, 'momento'] = (dfmx['dec'].loc[0] * dfmx['pp'].loc[0])
        dfmx.at[1, 'momento'] = (dfmx['dec'].loc[1] * dfmx['pp'].loc[1])
        dfmx.at[2, 'momento'] = (dfmx['dec'].loc[2] * dfmx['pp'].loc[2])
        dfmx.at[3, 'momento'] = (dfmx['dec'].loc[3] * dfmx['pp'].loc[3])
        dfmx.at[4, 'momento'] = (dfmx['dec'].loc[4] * dfmx['pp'].loc[4])
        dfmx.at[5, 'momento'] = (dfmx['dec'].loc[5] * dfmx['pp'].loc[5])
        dfmx.at[6, 'momento'] = (dfmx['dec'].loc[6] * dfmx['pp'].loc[6])
        dfmx.at[7, 'momento'] = (dfmx['dec'].loc[7] * dfmx['pp'].loc[7])
        dfmx.at[8, 'momento'] = (dfmx['dec'].loc[8] * dfmx['pp'].loc[8])
        dfmx.at[9, 'momento'] = (dfmx['dec'].loc[9] * dfmx['pp'].loc[9])
        dfmx.at[10, 'momento'] = (dfmx['dec'].loc[10] * dfmx['pp'].loc[10])
        dfmx.at[11, 'momento'] = (dfmx['dec'].loc[11] * dfmx['pp'].loc[11])
        dfmx.at[12, 'momento'] = (dfmx['dec'].loc[12] * dfmx['pp'].loc[12])
        dfmx.at[13, 'momento'] = (dfmx['dec'].loc[13] * dfmx['pp'].loc[13])

        cxcg = dfmx['momento'].loc[0]+dfmx['momento'].loc[1]+dfmx['momento'].loc[2] + dfmx['momento'].loc[3] + dfmx['momento'].loc[4] + dfmx['momento'].loc[5] + dfmx['momento'].loc[6] + \
            dfmx['momento'].loc[7] + dfmx['momento'].loc[8] + dfmx['momento'].loc[9] + \
            dfmx['momento'].loc[10] + dfmx['momento'].loc[11] + \
            dfmx['momento'].loc[12] + dfmx['momento'].loc[13]

        # print(dfmx)
        print(cxcg)
        # -------------------------------------
        dfmy.at[0, 'y1'] = y[0+salto]
        dfmy.at[1, 'y1'] = y[2+salto]
        dfmy.at[2, 'y1'] = y[5+salto]
        dfmy.at[3, 'y1'] = y[6+salto]
        dfmy.at[4, 'y1'] = y[7+salto]
        dfmy.at[5, 'y1'] = y[9+salto]
        dfmy.at[6, 'y1'] = y[10+salto]
        dfmy.at[7, 'y1'] = y[11+salto]
        dfmy.at[8, 'y1'] = y[3+salto]
        dfmy.at[9, 'y1'] = y[13+salto]
        dfmy.at[10, 'y1'] = y[15+salto]
        dfmy.at[11, 'y1'] = y[4+salto]
        dfmy.at[12, 'y1'] = y[17+salto]
        dfmy.at[13, 'y1'] = y[19+salto]

        dfmy.at[0, 'y2'] = y[1+salto]
        dfmy.at[1, 'y2'] = pmcy
        dfmy.at[2, 'y2'] = y[6+salto]
        dfmy.at[3, 'y2'] = y[7+salto]
        dfmy.at[4, 'y2'] = y[8+salto]
        dfmy.at[5, 'y2'] = y[10+salto]
        dfmy.at[6, 'y2'] = y[11+salto]
        dfmy.at[7, 'y2'] = y[12+salto]
        dfmy.at[8, 'y2'] = y[13+salto]
        dfmy.at[9, 'y2'] = y[14+salto]
        dfmy.at[10, 'y2'] = y[16+salto]
        dfmy.at[11, 'y2'] = y[17+salto]
        dfmy.at[12, 'y2'] = y[18+salto]
        dfmy.at[13, 'y2'] = y[20+salto]

        # print(dfmy)

        # 3a columna
        dfmy.at[0, 'longitud'] = abs(dfmy['y1'].loc[0] - dfmy['y2'].loc[0])
        dfmy.at[1, 'longitud'] = abs(dfmy['y1'].loc[1] - dfmy['y2'].loc[1])
        dfmy.at[2, 'longitud'] = abs(dfmy['y1'].loc[2] - dfmy['y2'].loc[2])
        dfmy.at[3, 'longitud'] = abs(dfmy['y1'].loc[3] - dfmy['y2'].loc[3])
        dfmy.at[4, 'longitud'] = abs(dfmy['y1'].loc[4] - dfmy['y2'].loc[4])
        dfmy.at[5, 'longitud'] = abs(dfmy['y1'].loc[5] - dfmy['y2'].loc[5])
        dfmy.at[6, 'longitud'] = abs(dfmy['y1'].loc[6] - dfmy['y2'].loc[6])
        dfmy.at[7, 'longitud'] = abs(dfmy['y1'].loc[7] - dfmy['y2'].loc[7])
        dfmy.at[8, 'longitud'] = abs(dfmy['y1'].loc[8] - dfmy['y2'].loc[8])
        dfmy.at[9, 'longitud'] = abs(dfmy['y1'].loc[9] - dfmy['y2'].loc[9])
        dfmy.at[10, 'longitud'] = abs(dfmy['y1'].loc[10] - dfmy['y2'].loc[10])
        dfmy.at[11, 'longitud'] = abs(dfmy['y1'].loc[11] - dfmy['y2'].loc[11])
        dfmy.at[12, 'longitud'] = abs(dfmy['y1'].loc[12] - dfmy['y2'].loc[12])
        dfmy.at[13, 'longitud'] = abs(dfmy['y1'].loc[13] - dfmy['y2'].loc[13])

        # 5a columna
        dfmy.at[0, 'dp'] = (dfmy['longitud'].loc[0] * dfmy['pl'].loc[0])
        dfmy.at[1, 'dp'] = (dfmy['longitud'].loc[1] * dfmy['pl'].loc[1])
        dfmy.at[2, 'dp'] = (dfmy['longitud'].loc[2] * dfmy['pl'].loc[2])
        dfmy.at[3, 'dp'] = (dfmy['longitud'].loc[3] * dfmy['pl'].loc[3])
        dfmy.at[4, 'dp'] = (dfmy['longitud'].loc[4] * dfmy['pl'].loc[4])
        dfmy.at[5, 'dp'] = (dfmy['longitud'].loc[5] * dfmy['pl'].loc[5])
        dfmy.at[6, 'dp'] = (dfmy['longitud'].loc[6] * dfmy['pl'].loc[6])
        dfmy.at[7, 'dp'] = (dfmy['longitud'].loc[7] * dfmy['pl'].loc[7])
        dfmy.at[8, 'dp'] = (dfmy['longitud'].loc[8] * dfmy['pl'].loc[8])
        dfmy.at[9, 'dp'] = (dfmy['longitud'].loc[9] * dfmy['pl'].loc[9])
        dfmy.at[10, 'dp'] = (dfmy['longitud'].loc[10] * dfmy['pl'].loc[10])
        dfmy.at[11, 'dp'] = (dfmy['longitud'].loc[11] * dfmy['pl'].loc[11])
        dfmy.at[12, 'dp'] = (dfmy['longitud'].loc[12] * dfmy['pl'].loc[12])
        dfmy.at[13, 'dp'] = (dfmy['longitud'].loc[13] * dfmy['pl'].loc[13])

        # 6a columna
        if dfmy['y1'].loc[0] <= dfmy['y2'].loc[0]:
            dfmy.at[0, 'dec'] = dfmy['y1'].loc[0] + dfmy['dp'].loc[0]
        else:
            dfmy.at[0, 'dec'] = dfmy['y1'].loc[0] - dfmy['dp'].loc[0]

        if dfmy['y1'].loc[1] <= dfmy['y2'].loc[1]:
            dfmy.at[1, 'dec'] = dfmy['y1'].loc[1] + dfmy['dp'].loc[1]
        else:
            dfmy.at[1, 'dec'] = dfmy['y1'].loc[1] - dfmy['dp'].loc[1]

        if dfmy['y1'].loc[2] <= dfmy['y2'].loc[2]:
            dfmy.at[2, 'dec'] = dfmy['y1'].loc[2] + dfmy['dp'].loc[2]
        else:
            dfmy.at[2, 'dec'] = dfmy['y1'].loc[2] - dfmy['dp'].loc[2]

        if dfmy['y1'].loc[3] <= dfmy['y2'].loc[3]:
            dfmy.at[3, 'dec'] = dfmy['y1'].loc[3] + dfmy['dp'].loc[3]
        else:
            dfmy.at[3, 'dec'] = dfmy['y1'].loc[3] - dfmy['dp'].loc[3]

        if dfmy['y1'].loc[4] <= dfmy['y2'].loc[4]:
            dfmy.at[4, 'dec'] = dfmy['y1'].loc[4] + dfmy['dp'].loc[4]
        else:
            dfmy.at[4, 'dec'] = dfmy['y1'].loc[4] - dfmy['dp'].loc[4]

        if dfmy['y1'].loc[5] <= dfmy['y2'].loc[5]:
            dfmy.at[5, 'dec'] = dfmy['y1'].loc[5] + dfmy['dp'].loc[5]
        else:
            dfmy.at[5, 'dec'] = dfmy['y1'].loc[5] - dfmy['dp'].loc[5]

        if dfmy['y1'].loc[6] <= dfmy['y2'].loc[6]:
            dfmy.at[6, 'dec'] = dfmy['y1'].loc[6] + dfmy['dp'].loc[6]
        else:
            dfmy.at[6, 'dec'] = dfmy['y1'].loc[6] - dfmy['dp'].loc[6]

        if dfmy['y1'].loc[7] <= dfmy['y2'].loc[7]:
            dfmy.at[7, 'dec'] = dfmy['y1'].loc[7] + dfmy['dp'].loc[7]
        else:
            dfmy.at[7, 'dec'] = dfmy['y1'].loc[7] - dfmy['dp'].loc[7]

        if dfmy['y1'].loc[8] <= dfmy['y2'].loc[8]:
            dfmy.at[8, 'dec'] = dfmy['y1'].loc[8] + dfmy['dp'].loc[8]
        else:
            dfmy.at[8, 'dec'] = dfmy['y1'].loc[8] - dfmy['dp'].loc[8]

        if dfmy['y1'].loc[9] <= dfmy['y2'].loc[9]:
            dfmy.at[9, 'dec'] = dfmy['y1'].loc[9] + dfmy['dp'].loc[9]
        else:
            dfmy.at[9, 'dec'] = dfmy['y1'].loc[9] - dfmy['dp'].loc[9]

        if dfmy['y1'].loc[10] <= dfmy['y2'].loc[10]:
            dfmy.at[10, 'dec'] = dfmy['y1'].loc[10] + dfmy['dp'].loc[10]
        else:
            dfmy.at[10, 'dec'] = dfmy['y1'].loc[10] - dfmy['dp'].loc[10]

        if dfmy['y1'].loc[11] <= dfmy['y2'].loc[11]:
            dfmy.at[11, 'dec'] = dfmy['y1'].loc[11] + dfmy['dp'].loc[11]
        else:
            dfmy.at[11, 'dec'] = dfmy['y1'].loc[11] - dfmy['dp'].loc[11]

        if dfmy['y1'].loc[12] <= dfmy['y2'].loc[12]:
            dfmy.at[12, 'dec'] = dfmy['y1'].loc[12] + dfmy['dp'].loc[12]
        else:
            dfmy.at[12, 'dec'] = dfmy['y1'].loc[12] - dfmy['dp'].loc[12]

        if dfmy['y1'].loc[13] <= dfmy['y2'].loc[13]:
            dfmy.at[13, 'dec'] = dfmy['y1'].loc[13] + dfmy['dp'].loc[13]
        else:
            dfmy.at[13, 'dec'] = dfmy['y1'].loc[13] - dfmy['dp'].loc[13]

        # 8a columna
        dfmy.at[0, 'momento'] = (dfmy['dec'].loc[0] * dfmy['pp'].loc[0])
        dfmy.at[1, 'momento'] = (dfmy['dec'].loc[1] * dfmy['pp'].loc[1])
        dfmy.at[2, 'momento'] = (dfmy['dec'].loc[2] * dfmy['pp'].loc[2])
        dfmy.at[3, 'momento'] = (dfmy['dec'].loc[3] * dfmy['pp'].loc[3])
        dfmy.at[4, 'momento'] = (dfmy['dec'].loc[4] * dfmy['pp'].loc[4])
        dfmy.at[5, 'momento'] = (dfmy['dec'].loc[5] * dfmy['pp'].loc[5])
        dfmy.at[6, 'momento'] = (dfmy['dec'].loc[6] * dfmy['pp'].loc[6])
        dfmy.at[7, 'momento'] = (dfmy['dec'].loc[7] * dfmy['pp'].loc[7])
        dfmy.at[8, 'momento'] = (dfmy['dec'].loc[8] * dfmy['pp'].loc[8])
        dfmy.at[9, 'momento'] = (dfmy['dec'].loc[9] * dfmy['pp'].loc[9])
        dfmy.at[10, 'momento'] = (dfmy['dec'].loc[10] * dfmy['pp'].loc[10])
        dfmy.at[11, 'momento'] = (dfmy['dec'].loc[11] * dfmy['pp'].loc[11])
        dfmy.at[12, 'momento'] = (dfmy['dec'].loc[12] * dfmy['pp'].loc[12])
        dfmy.at[13, 'momento'] = (dfmy['dec'].loc[13] * dfmy['pp'].loc[13])

        cycg = dfmy['momento'].loc[0]+dfmy['momento'].loc[1]+dfmy['momento'].loc[2] + dfmy['momento'].loc[3] + dfmy['momento'].loc[4] + dfmy['momento'].loc[5] + dfmy['momento'].loc[6] + \
            dfmy['momento'].loc[7] + dfmy['momento'].loc[8] + dfmy['momento'].loc[9] + \
            dfmy['momento'].loc[10] + dfmy['momento'].loc[11] + \
            dfmy['momento'].loc[12] + dfmy['momento'].loc[13]

        # print(dfmy)
        print(cycg)
        #####################################################################
        plt.plot(cxcg, cycg, marker="o", color="red")
        cont2 = cont2+1

        if cont2 < (cont+1)/42:
            salto = salto+21
    plt.show()
    fang.close(0)


###################################################################
# Modulo de DIGITALIZACION
# Enrique Buendia Lozada BUAP 2021
###################################################################
cont = 0  # contador de puntos


def digital():
    #
    files = glob.glob("*.jpg")
    cont = 0
    # archivo con todas las coordenadas digitalizadas, mundo real
    f = open('c_real.txt', 'a')
    f2 = open('c_pant.txt', 'a')

    def on_press(event):
        try:
            global cont
            cont = cont+1
            print(cont)

            alto_real = 1000
            ancho_real = 1000
            xp = event.xdata
            yp = event.ydata
            xmax = 1000
            xmin = 0
            ymax = 1000
            ymin = 0

            print("En pantalla:", event.button, xp, yp)
            f2.write(str(xp))
            f2.write('\n')
            f2.write(str(yp))
            f2.write('\n')

            x = (xp/ancho_real)*(xmax-xmin)+xmin
            y = ((alto_real-yp)/alto_real)*(ymax-ymin)+ymin
            #np.append(pc, x, y)
            print("En real:", x, y)
            f.write(str(x))
            f.write('\n')
            f.write(str(y))
            f.write('\n')

            if cont == 1:
                win32api.MessageBox(0, '1 Vertex', 'Digitalizado')
            if cont == 2:
                win32api.MessageBox(0, '2 Mandibular', 'Digitalizado')
            if cont == 3:
                win32api.MessageBox(0, '3 Spraesternal', 'Digitalizado')
            if cont == 4:
                win32api.MessageBox(0, '4 Cadera derecha', 'Digitalizado')
            if cont == 5:
                win32api.MessageBox(0, '5 Cadera izquierda', 'Digitalizado')
            if cont == 6:
                win32api.MessageBox(0, '6 Hombro derecho', 'Digitalizado')
            if cont == 7:
                win32api.MessageBox(0, '7 Codo derecho', 'Digitalizado')
            if cont == 8:
                win32api.MessageBox(0, '8 Muñeca derecha', 'Digitalizado')
            if cont == 9:
                win32api.MessageBox(0, '9 Mano derecha', 'Digitalizado')
            if cont == 10:
                win32api.MessageBox(0, '10 Hombro izquierdo', 'Digitalizado')
            if cont == 11:
                win32api.MessageBox(0, '11 Codo izquierdo', 'Digitalizado')
            if cont == 12:
                win32api.MessageBox(0, '12 Muñeca izquierda', 'Digitalizado')
            if cont == 13:
                win32api.MessageBox(0, '13 Mano izquierda', 'Digitalizado')
            if cont == 14:
                win32api.MessageBox(0, '14 Rodilla derecha', 'Digitalizado')
            if cont == 15:
                win32api.MessageBox(0, '15 Tobillo derecho', 'Digitalizado')
            if cont == 16:
                win32api.MessageBox(0, '16 Talón derecho', 'Digitalizado')
            if cont == 17:
                win32api.MessageBox(0, '17 Pie derecho', 'Digitalizado')
            if cont == 18:
                win32api.MessageBox(0, '18 Rodilla izquierda', 'Digitalizado')
            if cont == 19:
                win32api.MessageBox(0, '19 Tobillo izquierdo', 'Digitalizado')
            if cont == 20:
                win32api.MessageBox(0, '20 Talón izquierdo', 'Digitalizado')
            if cont == 21:
                win32api.MessageBox(0, '21 Pie izquierdo', 'Digitalizado')

            if cont >= 21:
                cont = 0
                plt.close()
        except:
            f.close(0)
            f2.close(0)
            raise SystemExit('Error desconocido: Adios...')

    for imagen in files:
        # Tamaño de imagen a mostrar
        my_dpi = 96
        fig = plt.figure("Método segmentario BIOMECÁNICA EN CIENCIAS DE LA ACTIVIDAD FÍSICA Y DEPORTE",
                         figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
        fig.suptitle(
            'Enrique Buendia, BUAP 2021:  Módulo Digitalizar \n Método segmentario para el cálculo del Cntro de grevedad corporal humano', fontsize=12)
        plt.text(
            0, 800, 'Puntos de control (digitalizar estos puntos en cada imágen)')
        plt.text(
            0, 820, '1 Vertex  2 Mandibular   3 Supraesternal   4 Cadera derecha   5 Cadera izquierda')
        plt.text(
            0, 840, '6 Hombro derecho   7 Codo derecho   8 Muñeca derecha   9 Mano derecha   10 Hombro izquierdo')
        plt.text(0, 860, '11 Codo izquierdo   12 Muñeca izquierda   13 Mano izquierda   14 Rodilla derecha   15 Tobillo derecho')
        plt.text(0, 880, '16 Talón derecho   17 Pie derecho   18 Rodilla izquierda   19 Tobillo izquierdo   20 Talón izquierdo')
        plt.text(0, 900, '21 Pie izquierdo')

        # cambiar a coordenadas reales
        alto_real = 1000
        ancho_real = 1000

        img = Image.open(imagen)
        #updata = True

        plt.imshow(img, animated=True)

        fig.canvas.mpl_connect('button_press_event', on_press)
        plt.show()

# ***********************************
# *** respaldar información anterior
# ***
# ***********************************


def borrar():
    # en realidad solo respalda la información, no se borra
    # os.remove("ChangedFile.csv")
    # c_pant.txt c_real.txt
    e = datetime.datetime.now()
    newarch = str(e.day)+str(e.month)+str(e.year) + \
        str(e.hour)+str(e.minute)+"c_real.bk"
    os.rename('c_real.txt', newarch)
    newarch = str(e.day)+str(e.month)+str(e.year) + \
        str(e.hour)+str(e.minute)+"c_pant.bk"
    os.rename('c_pant.txt', newarch)
    print("Archivos respaldados!")
    win32api.MessageBox(0, 'Archivos respaldados',
                        'Sistema de análisis biomecánico')


###################################################################
# Modulo MP4 a JPG
# Enrique Buendia Lozada BUAP 2021
###################################################################


def mp4():
    win32api.MessageBox(
        0, 'El video debe ter el nombre vid.mp4 \n todas las imégenes se guerdaran en la misma carpeta donde se encuentra el video', 'MP4 a JPG')
    try:
        vidcap = cv2.VideoCapture('vid.mp4')
        success, image = vidcap.read()
        count = 0
        while success:
            # save frame as JPEG file
            cv2.imwrite("frame%d.jpg" % count, image)
            success, image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
        win32api.MessageBox(0, 'proceso finalizado.', 'MP4 a JPG')
    except:
        win32api.MessageBox(
            0, 'No se cumplen las condiciones de uso ...', 'Error')


win = tk.Tk()
win.title('Centro de gravedad corporal [Método segmentario]')
win.geometry('600x250')

texto1 = tk.Label(
    win, text="Sistema de Análisis biomecánico [Otoño 2021] \n Enrique Buendia\n \n").pack()

# create text field
# textField = tk.Entry(win, width=50)
# textField.pack(fill=tk.NONE, side=tk.TOP)

# create button to convert video to imeges jpg
openBtn = tk.Button(win, text='MP4 a jpg', command=mp4)
openBtn.pack(expand=tk.FALSE, side=tk.TOP)

# create button to scan the points of Segmental method
saveBtn = tk.Button(win, text='Digitalizar', command=digital)
#saveBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)
saveBtn.pack(expand=tk.FALSE, side=tk.TOP)

# create button to draw model and gravity center
saveBtn = tk.Button(
    win, text='Modelo de alambre y Centro de gravedad', command=model)
#saveBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)
saveBtn.pack(expand=tk.FALSE, side=tk.TOP)

# create button to draw model and gravity center
saveBtn = tk.Button(
    win, text='Borrar archivos anteriores: ', command=borrar)
#saveBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)
saveBtn.pack(expand=tk.FALSE, side=tk.TOP)

# create button to calculate angles
saveBtn = tk.Button(
    win, text='Angulos (datos 3 puntos marcados con el ratón): ', command=v_angulos)
#saveBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)
saveBtn.pack(expand=tk.FALSE, side=tk.TOP)

# create button to calculate distances
saveBtn = tk.Button(
    win, text='Estimar distancias: ', command=v_dist)
#saveBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)
saveBtn.pack(expand=tk.FALSE, side=tk.TOP)

win.mainloop()
