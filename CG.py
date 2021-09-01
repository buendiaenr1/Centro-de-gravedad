import tkinter as tk
import win32api
import cv2

from os import system
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image
import glob

import win32api

import pandas as pd

#############################################################################################
######
# Sistema de Análisis de Biomecánico   por el método segmentario
# Enrique R.P. Buendia Lozada
# Benemérita Universidad Autónoma de Puebla
# México  [Otoño 2021]
######
#############################################################################################


##########################################################################
# Módulo Machote de calculo del Centro de gravedad
# Enrique Buendia Lozada Otoño 2021
##########################################################################


def model():
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

    x = []
    y = []
    cont = 1
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

    # modelo de alambre
    # cabeza
    x2 = []
    y2 = []
    x2.append(x[0])
    y2.append(y[0])
    x2.append(x[1])
    y2.append(y[1])
    plt.plot(x2, y2, color="c")
    # clavicula derecha
    x2 = []
    y2 = []
    x2.append(x[2])
    y2.append(y[2])
    x2.append(x[5])
    y2.append(y[5])
    plt.plot(x2, y2, color="c")
    # antebrazo derecho
    x2 = []
    y2 = []
    x2.append(x[5])
    y2.append(y[5])
    x2.append(x[6])
    y2.append(y[6])
    plt.plot(x2, y2, color="c")
    # brazo derecho
    x2 = []
    y2 = []
    x2.append(x[6])
    y2.append(y[6])
    x2.append(x[7])
    y2.append(y[7])
    plt.plot(x2, y2, color="c")
    # mano derecha
    x2 = []
    y2 = []
    x2.append(x[7])
    y2.append(y[7])
    x2.append(x[8])
    y2.append(y[8])
    plt.plot(x2, y2, color="c")

    # claviculo izquierda
    x2 = []
    y2 = []
    x2.append(x[2])
    y2.append(y[2])
    x2.append(x[9])
    y2.append(y[9])
    plt.plot(x2, y2, color="c")
    # antebrazo izquierdo
    x2 = []
    y2 = []
    x2.append(x[9])
    y2.append(y[9])
    x2.append(x[10])
    y2.append(y[10])
    plt.plot(x2, y2, color="c")
    # brazo izquierdo
    x2 = []
    y2 = []
    x2.append(x[10])
    y2.append(y[10])
    x2.append(x[11])
    y2.append(y[11])
    plt.plot(x2, y2, color="c")
    # mano izquierda
    x2 = []
    y2 = []
    x2.append(x[11])
    y2.append(y[11])
    x2.append(x[12])
    y2.append(y[12])
    plt.plot(x2, y2, color="c")

    # caderas
    x2 = []
    y2 = []
    x2.append(x[3])
    y2.append(y[3])
    x2.append(x[4])
    y2.append(y[4])
    plt.plot(x2, y2, color="c")
    # femur derecho
    x2 = []
    y2 = []
    x2.append(x[3])
    y2.append(y[3])
    x2.append(x[13])
    y2.append(y[13])
    plt.plot(x2, y2, color="c")
    # pierna derecha
    x2 = []
    y2 = []
    x2.append(x[13])
    y2.append(y[13])
    x2.append(x[14])
    y2.append(y[14])
    plt.plot(x2, y2, color="c")
    # talon derecho
    x2 = []
    y2 = []
    x2.append(x[14])
    y2.append(y[14])
    x2.append(x[15])
    y2.append(y[15])
    plt.plot(x2, y2, color="c")
    # pie derecho
    x2 = []
    y2 = []
    x2.append(x[15])
    y2.append(y[15])
    x2.append(x[16])
    y2.append(y[16])
    plt.plot(x2, y2, color="c")
    # femur izquierdo
    x2 = []
    y2 = []
    #############
    x2.append(x[4])
    y2.append(y[4])
    x2.append(x[17])
    y2.append(y[17])
    plt.plot(x2, y2, color="c")
    # pierna izquierda
    x2 = []
    y2 = []
    x2.append(x[17])
    y2.append(y[17])
    x2.append(x[18])
    y2.append(y[18])
    plt.plot(x2, y2, color="c")
    # talon izquierdo
    x2 = []
    y2 = []
    x2.append(x[18])
    y2.append(y[18])
    x2.append(x[19])
    y2.append(y[19])
    plt.plot(x2, y2, color="c")
    # pie izquierdo
    x2 = []
    y2 = []
    x2.append(x[19])
    y2.append(y[19])
    x2.append(x[20])
    y2.append(y[20])
    plt.plot(x2, y2, color="c")
    # pm caderas
    pmcx = (x[3]+x[4])/2
    pmcy = (y[3]+y[4])/2
    # tronco
    x2 = []
    y2 = []
    x2.append(x[2])
    y2.append(y[2])
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

    dfmx['x1'].loc[0] = x[0]
    dfmx['x1'].loc[1] = x[2]
    dfmx['x1'].loc[2] = x[5]
    dfmx['x1'].loc[3] = x[6]
    dfmx['x1'].loc[4] = x[7]
    dfmx['x1'].loc[5] = x[9]
    dfmx['x1'].loc[6] = x[10]
    dfmx['x1'].loc[7] = x[11]
    dfmx['x1'].loc[8] = x[3]
    dfmx['x1'].loc[9] = x[13]
    dfmx['x1'].loc[10] = x[15]
    dfmx['x1'].loc[11] = x[4]
    dfmx['x1'].loc[12] = x[17]
    dfmx['x1'].loc[13] = x[19]

    dfmx['x2'].loc[0] = x[1]
    dfmx['x2'].loc[1] = pmcx
    dfmx['x2'].loc[2] = x[6]
    dfmx['x2'].loc[3] = x[7]
    dfmx['x2'].loc[4] = x[8]
    dfmx['x2'].loc[5] = x[10]
    dfmx['x2'].loc[6] = x[11]
    dfmx['x2'].loc[7] = x[12]
    dfmx['x2'].loc[8] = x[13]
    dfmx['x2'].loc[9] = x[14]
    dfmx['x2'].loc[10] = x[16]
    dfmx['x2'].loc[11] = x[17]
    dfmx['x2'].loc[12] = x[18]
    dfmx['x2'].loc[13] = x[20]

    # print(dfmx)

    # 3a columna
    dfmx['longitud'].loc[0] = abs(dfmx['x1'].loc[0] - dfmx['x2'].loc[0])
    dfmx['longitud'].loc[1] = abs(dfmx['x1'].loc[1] - dfmx['x2'].loc[1])
    dfmx['longitud'].loc[2] = abs(dfmx['x1'].loc[2] - dfmx['x2'].loc[2])
    dfmx['longitud'].loc[3] = abs(dfmx['x1'].loc[3] - dfmx['x2'].loc[3])
    dfmx['longitud'].loc[4] = abs(dfmx['x1'].loc[4] - dfmx['x2'].loc[4])
    dfmx['longitud'].loc[5] = abs(dfmx['x1'].loc[5] - dfmx['x2'].loc[5])
    dfmx['longitud'].loc[6] = abs(dfmx['x1'].loc[6] - dfmx['x2'].loc[6])
    dfmx['longitud'].loc[7] = abs(dfmx['x1'].loc[7] - dfmx['x2'].loc[7])
    dfmx['longitud'].loc[8] = abs(dfmx['x1'].loc[8] - dfmx['x2'].loc[8])
    dfmx['longitud'].loc[9] = abs(dfmx['x1'].loc[9] - dfmx['x2'].loc[9])
    dfmx['longitud'].loc[10] = abs(dfmx['x1'].loc[10] - dfmx['x2'].loc[10])
    dfmx['longitud'].loc[11] = abs(dfmx['x1'].loc[11] - dfmx['x2'].loc[11])
    dfmx['longitud'].loc[12] = abs(dfmx['x1'].loc[12] - dfmx['x2'].loc[12])
    dfmx['longitud'].loc[13] = abs(dfmx['x1'].loc[13] - dfmx['x2'].loc[13])

    # 5a columna
    dfmx['dp'].loc[0] = (dfmx['longitud'].loc[0] * dfmx['pl'].loc[0])
    dfmx['dp'].loc[1] = (dfmx['longitud'].loc[1] * dfmx['pl'].loc[1])
    dfmx['dp'].loc[2] = (dfmx['longitud'].loc[2] * dfmx['pl'].loc[2])
    dfmx['dp'].loc[3] = (dfmx['longitud'].loc[3] * dfmx['pl'].loc[3])
    dfmx['dp'].loc[4] = (dfmx['longitud'].loc[4] * dfmx['pl'].loc[4])
    dfmx['dp'].loc[5] = (dfmx['longitud'].loc[5] * dfmx['pl'].loc[5])
    dfmx['dp'].loc[6] = (dfmx['longitud'].loc[6] * dfmx['pl'].loc[6])
    dfmx['dp'].loc[7] = (dfmx['longitud'].loc[7] * dfmx['pl'].loc[7])
    dfmx['dp'].loc[8] = (dfmx['longitud'].loc[8] * dfmx['pl'].loc[8])
    dfmx['dp'].loc[9] = (dfmx['longitud'].loc[9] * dfmx['pl'].loc[9])
    dfmx['dp'].loc[10] = (dfmx['longitud'].loc[10] * dfmx['pl'].loc[10])
    dfmx['dp'].loc[11] = (dfmx['longitud'].loc[11] * dfmx['pl'].loc[11])
    dfmx['dp'].loc[12] = (dfmx['longitud'].loc[12] * dfmx['pl'].loc[12])
    dfmx['dp'].loc[13] = (dfmx['longitud'].loc[13] * dfmx['pl'].loc[13])

    # 6a columna
    if dfmx['x1'].loc[0] <= dfmx['x2'].loc[0]:
        dfmx['dec'].loc[0] = dfmx['x1'].loc[0] + dfmx['dp'].loc[0]
    else:
        dfmx['dec'].loc[0] = dfmx['x1'].loc[0] - dfmx['dp'].loc[0]

    if dfmx['x1'].loc[1] <= dfmx['x2'].loc[1]:
        dfmx['dec'].loc[1] = dfmx['x1'].loc[1] + dfmx['dp'].loc[1]
    else:
        dfmx['dec'].loc[1] = dfmx['x1'].loc[1] - dfmx['dp'].loc[1]

    if dfmx['x1'].loc[2] <= dfmx['x2'].loc[2]:
        dfmx['dec'].loc[2] = dfmx['x1'].loc[2] + dfmx['dp'].loc[2]
    else:
        dfmx['dec'].loc[2] = dfmx['x1'].loc[2] - dfmx['dp'].loc[2]

    if dfmx['x1'].loc[3] <= dfmx['x2'].loc[3]:
        dfmx['dec'].loc[3] = dfmx['x1'].loc[3] + dfmx['dp'].loc[3]
    else:
        dfmx['dec'].loc[3] = dfmx['x1'].loc[3] - dfmx['dp'].loc[3]

    if dfmx['x1'].loc[4] <= dfmx['x2'].loc[4]:
        dfmx['dec'].loc[4] = dfmx['x1'].loc[4] + dfmx['dp'].loc[4]
    else:
        dfmx['dec'].loc[4] = dfmx['x1'].loc[4] - dfmx['dp'].loc[4]

    if dfmx['x1'].loc[5] <= dfmx['x2'].loc[5]:
        dfmx['dec'].loc[5] = dfmx['x1'].loc[5] + dfmx['dp'].loc[5]
    else:
        dfmx['dec'].loc[5] = dfmx['x1'].loc[5] - dfmx['dp'].loc[5]

    if dfmx['x1'].loc[6] <= dfmx['x2'].loc[6]:
        dfmx['dec'].loc[6] = dfmx['x1'].loc[6] + dfmx['dp'].loc[6]
    else:
        dfmx['dec'].loc[6] = dfmx['x1'].loc[6] - dfmx['dp'].loc[6]

    if dfmx['x1'].loc[7] <= dfmx['x2'].loc[7]:
        dfmx['dec'].loc[7] = dfmx['x1'].loc[7] + dfmx['dp'].loc[7]
    else:
        dfmx['dec'].loc[7] = dfmx['x1'].loc[7] - dfmx['dp'].loc[7]

    if dfmx['x1'].loc[8] <= dfmx['x2'].loc[8]:
        dfmx['dec'].loc[8] = dfmx['x1'].loc[8] + dfmx['dp'].loc[8]
    else:
        dfmx['dec'].loc[8] = dfmx['x1'].loc[8] - dfmx['dp'].loc[8]

    if dfmx['x1'].loc[9] <= dfmx['x2'].loc[9]:
        dfmx['dec'].loc[9] = dfmx['x1'].loc[9] + dfmx['dp'].loc[9]
    else:
        dfmx['dec'].loc[10] = dfmx['x1'].loc[10] - dfmx['dp'].loc[10]

    if dfmx['x1'].loc[11] <= dfmx['x2'].loc[11]:
        dfmx['dec'].loc[11] = dfmx['x1'].loc[11] + dfmx['dp'].loc[11]
    else:
        dfmx['dec'].loc[11] = dfmx['x1'].loc[11] - dfmx['dp'].loc[11]

    if dfmx['x1'].loc[12] <= dfmx['x2'].loc[12]:
        dfmx['dec'].loc[12] = dfmx['x1'].loc[12] + dfmx['dp'].loc[12]
    else:
        dfmx['dec'].loc[12] = dfmx['x1'].loc[12] - dfmx['dp'].loc[12]

    if dfmx['x1'].loc[13] <= dfmx['x2'].loc[13]:
        dfmx['dec'].loc[13] = dfmx['x1'].loc[13] + dfmx['dp'].loc[13]
    else:
        dfmx['dec'].loc[13] = dfmx['x1'].loc[13] - dfmx['dp'].loc[13]

    # 8a columna
    dfmx['momento'].loc[0] = (dfmx['dec'].loc[0] * dfmx['pp'].loc[0])
    dfmx['momento'].loc[1] = (dfmx['dec'].loc[1] * dfmx['pp'].loc[1])
    dfmx['momento'].loc[2] = (dfmx['dec'].loc[2] * dfmx['pp'].loc[2])
    dfmx['momento'].loc[3] = (dfmx['dec'].loc[3] * dfmx['pp'].loc[3])
    dfmx['momento'].loc[4] = (dfmx['dec'].loc[4] * dfmx['pp'].loc[4])
    dfmx['momento'].loc[5] = (dfmx['dec'].loc[5] * dfmx['pp'].loc[5])
    dfmx['momento'].loc[6] = (dfmx['dec'].loc[6] * dfmx['pp'].loc[6])
    dfmx['momento'].loc[7] = (dfmx['dec'].loc[7] * dfmx['pp'].loc[7])
    dfmx['momento'].loc[8] = (dfmx['dec'].loc[8] * dfmx['pp'].loc[8])
    dfmx['momento'].loc[9] = (dfmx['dec'].loc[9] * dfmx['pp'].loc[9])
    dfmx['momento'].loc[10] = (dfmx['dec'].loc[10] * dfmx['pp'].loc[10])
    dfmx['momento'].loc[11] = (dfmx['dec'].loc[11] * dfmx['pp'].loc[11])
    dfmx['momento'].loc[12] = (dfmx['dec'].loc[12] * dfmx['pp'].loc[12])
    dfmx['momento'].loc[13] = (dfmx['dec'].loc[13] * dfmx['pp'].loc[13])
    cxcg = dfmx['momento'].loc[0]+dfmx['momento'].loc[1]+dfmx['momento'].loc[2] + dfmx['momento'].loc[3] + dfmx['momento'].loc[4] + dfmx['momento'].loc[5] + dfmx['momento'].loc[6] + \
        dfmx['momento'].loc[7] + dfmx['momento'].loc[8] + dfmx['momento'].loc[9] + \
        dfmx['momento'].loc[10] + dfmx['momento'].loc[11] + \
        dfmx['momento'].loc[12] + dfmx['momento'].loc[13]

    # print(dfmx)
    print(cxcg)
    # -------------------------------------
    dfmy['y1'].loc[0] = y[0]
    dfmy['y1'].loc[1] = y[2]
    dfmy['y1'].loc[2] = y[5]
    dfmy['y1'].loc[3] = y[6]
    dfmy['y1'].loc[4] = y[7]
    dfmy['y1'].loc[5] = y[9]
    dfmy['y1'].loc[6] = y[10]
    dfmy['y1'].loc[7] = y[11]
    dfmy['y1'].loc[8] = y[3]
    dfmy['y1'].loc[9] = y[13]
    dfmy['y1'].loc[10] = y[15]
    dfmy['y1'].loc[11] = y[4]
    dfmy['y1'].loc[12] = y[17]
    dfmy['y1'].loc[13] = y[19]

    dfmy['y2'].loc[0] = y[1]
    dfmy['y2'].loc[1] = pmcy
    dfmy['y2'].loc[2] = y[6]
    dfmy['y2'].loc[3] = y[7]
    dfmy['y2'].loc[4] = y[8]
    dfmy['y2'].loc[5] = y[10]
    dfmy['y2'].loc[6] = y[11]
    dfmy['y2'].loc[7] = y[12]
    dfmy['y2'].loc[8] = y[13]
    dfmy['y2'].loc[9] = y[14]
    dfmy['y2'].loc[10] = y[16]
    dfmy['y2'].loc[11] = y[17]
    dfmy['y2'].loc[12] = y[18]
    dfmy['y2'].loc[13] = y[20]

    # print(dfmy)

    # 3a columna
    dfmy['longitud'].loc[0] = abs(dfmy['y1'].loc[0] - dfmy['y2'].loc[0])
    dfmy['longitud'].loc[1] = abs(dfmy['y1'].loc[1] - dfmy['y2'].loc[1])
    dfmy['longitud'].loc[2] = abs(dfmy['y1'].loc[2] - dfmy['y2'].loc[2])
    dfmy['longitud'].loc[3] = abs(dfmy['y1'].loc[3] - dfmy['y2'].loc[3])
    dfmy['longitud'].loc[4] = abs(dfmy['y1'].loc[4] - dfmy['y2'].loc[4])
    dfmy['longitud'].loc[5] = abs(dfmy['y1'].loc[5] - dfmy['y2'].loc[5])
    dfmy['longitud'].loc[6] = abs(dfmy['y1'].loc[6] - dfmy['y2'].loc[6])
    dfmy['longitud'].loc[7] = abs(dfmy['y1'].loc[7] - dfmy['y2'].loc[7])
    dfmy['longitud'].loc[8] = abs(dfmy['y1'].loc[8] - dfmy['y2'].loc[8])
    dfmy['longitud'].loc[9] = abs(dfmy['y1'].loc[9] - dfmy['y2'].loc[9])
    dfmy['longitud'].loc[10] = abs(dfmy['y1'].loc[10] - dfmy['y2'].loc[10])
    dfmy['longitud'].loc[11] = abs(dfmy['y1'].loc[11] - dfmy['y2'].loc[11])
    dfmy['longitud'].loc[12] = abs(dfmy['y1'].loc[12] - dfmy['y2'].loc[12])
    dfmy['longitud'].loc[13] = abs(dfmy['y1'].loc[13] - dfmy['y2'].loc[13])

    # 5a columna
    dfmy['dp'].loc[0] = (dfmy['longitud'].loc[0] * dfmy['pl'].loc[0])
    dfmy['dp'].loc[1] = (dfmy['longitud'].loc[1] * dfmy['pl'].loc[1])
    dfmy['dp'].loc[2] = (dfmy['longitud'].loc[2] * dfmy['pl'].loc[2])
    dfmy['dp'].loc[3] = (dfmy['longitud'].loc[3] * dfmy['pl'].loc[3])
    dfmy['dp'].loc[4] = (dfmy['longitud'].loc[4] * dfmy['pl'].loc[4])
    dfmy['dp'].loc[5] = (dfmy['longitud'].loc[5] * dfmy['pl'].loc[5])
    dfmy['dp'].loc[6] = (dfmy['longitud'].loc[6] * dfmy['pl'].loc[6])
    dfmy['dp'].loc[7] = (dfmy['longitud'].loc[7] * dfmy['pl'].loc[7])
    dfmy['dp'].loc[8] = (dfmy['longitud'].loc[8] * dfmy['pl'].loc[8])
    dfmy['dp'].loc[9] = (dfmy['longitud'].loc[9] * dfmy['pl'].loc[9])
    dfmy['dp'].loc[10] = (dfmy['longitud'].loc[10] * dfmy['pl'].loc[10])
    dfmy['dp'].loc[11] = (dfmy['longitud'].loc[11] * dfmy['pl'].loc[11])
    dfmy['dp'].loc[12] = (dfmy['longitud'].loc[12] * dfmy['pl'].loc[12])
    dfmy['dp'].loc[13] = (dfmy['longitud'].loc[13] * dfmy['pl'].loc[13])

    # 6a columna
    if dfmy['y1'].loc[0] <= dfmy['y2'].loc[0]:
        dfmy['dec'].loc[0] = dfmy['y1'].loc[0] + dfmy['dp'].loc[0]
    else:
        dfmy['dec'].loc[0] = dfmy['y1'].loc[0] - dfmy['dp'].loc[0]

    if dfmy['y1'].loc[1] <= dfmy['y2'].loc[1]:
        dfmy['dec'].loc[1] = dfmy['y1'].loc[1] + dfmy['dp'].loc[1]
    else:
        dfmy['dec'].loc[1] = dfmy['y1'].loc[1] - dfmy['dp'].loc[1]

    if dfmy['y1'].loc[2] <= dfmy['y2'].loc[2]:
        dfmy['dec'].loc[2] = dfmy['y1'].loc[2] + dfmy['dp'].loc[2]
    else:
        dfmy['dec'].loc[2] = dfmy['y1'].loc[2] - dfmy['dp'].loc[2]

    if dfmy['y1'].loc[3] <= dfmy['y2'].loc[3]:
        dfmy['dec'].loc[3] = dfmy['y1'].loc[3] + dfmy['dp'].loc[3]
    else:
        dfmy['dec'].loc[3] = dfmy['y1'].loc[3] - dfmy['dp'].loc[3]

    if dfmy['y1'].loc[4] <= dfmy['y2'].loc[4]:
        dfmy['dec'].loc[4] = dfmy['y1'].loc[4] + dfmy['dp'].loc[4]
    else:
        dfmy['dec'].loc[4] = dfmy['y1'].loc[4] - dfmy['dp'].loc[4]

    if dfmy['y1'].loc[5] <= dfmy['y2'].loc[5]:
        dfmy['dec'].loc[5] = dfmy['y1'].loc[5] + dfmy['dp'].loc[5]
    else:
        dfmy['dec'].loc[5] = dfmy['y1'].loc[5] - dfmy['dp'].loc[5]

    if dfmy['y1'].loc[6] <= dfmy['y2'].loc[6]:
        dfmy['dec'].loc[6] = dfmy['y1'].loc[6] + dfmy['dp'].loc[6]
    else:
        dfmy['dec'].loc[6] = dfmy['y1'].loc[6] - dfmy['dp'].loc[6]

    if dfmy['y1'].loc[7] <= dfmy['y2'].loc[7]:
        dfmy['dec'].loc[7] = dfmy['y1'].loc[7] + dfmy['dp'].loc[7]
    else:
        dfmy['dec'].loc[7] = dfmy['y1'].loc[7] - dfmy['dp'].loc[7]

    if dfmy['y1'].loc[8] <= dfmy['y2'].loc[8]:
        dfmy['dec'].loc[8] = dfmy['y1'].loc[8] + dfmy['dp'].loc[8]
    else:
        dfmy['dec'].loc[8] = dfmy['y1'].loc[8] - dfmy['dp'].loc[8]

    if dfmy['y1'].loc[9] <= dfmy['y2'].loc[9]:
        dfmy['dec'].loc[9] = dfmy['y1'].loc[9] + dfmy['dp'].loc[9]
    else:
        dfmy['dec'].loc[10] = dfmy['y1'].loc[10] - dfmy['dp'].loc[10]

    if dfmy['y1'].loc[11] <= dfmy['y2'].loc[11]:
        dfmy['dec'].loc[11] = dfmy['y1'].loc[11] + dfmy['dp'].loc[11]
    else:
        dfmy['dec'].loc[11] = dfmy['y1'].loc[11] - dfmy['dp'].loc[11]

    if dfmy['y1'].loc[12] <= dfmy['y2'].loc[12]:
        dfmy['dec'].loc[12] = dfmy['y1'].loc[12] + dfmy['dp'].loc[12]
    else:
        dfmy['dec'].loc[12] = dfmy['y1'].loc[12] - dfmy['dp'].loc[12]

    if dfmy['y1'].loc[13] <= dfmy['y2'].loc[13]:
        dfmy['dec'].loc[13] = dfmy['y1'].loc[13] + dfmy['dp'].loc[13]
    else:
        dfmy['dec'].loc[13] = dfmy['y1'].loc[13] - dfmy['dp'].loc[13]

    # 8a columna
    dfmy['momento'].loc[0] = (dfmy['dec'].loc[0] * dfmy['pp'].loc[0])
    dfmy['momento'].loc[1] = (dfmy['dec'].loc[1] * dfmy['pp'].loc[1])
    dfmy['momento'].loc[2] = (dfmy['dec'].loc[2] * dfmy['pp'].loc[2])
    dfmy['momento'].loc[3] = (dfmy['dec'].loc[3] * dfmy['pp'].loc[3])
    dfmy['momento'].loc[4] = (dfmy['dec'].loc[4] * dfmy['pp'].loc[4])
    dfmy['momento'].loc[5] = (dfmy['dec'].loc[5] * dfmy['pp'].loc[5])
    dfmy['momento'].loc[6] = (dfmy['dec'].loc[6] * dfmy['pp'].loc[6])
    dfmy['momento'].loc[7] = (dfmy['dec'].loc[7] * dfmy['pp'].loc[7])
    dfmy['momento'].loc[8] = (dfmy['dec'].loc[8] * dfmy['pp'].loc[8])
    dfmy['momento'].loc[9] = (dfmy['dec'].loc[9] * dfmy['pp'].loc[9])
    dfmy['momento'].loc[10] = (dfmy['dec'].loc[10] * dfmy['pp'].loc[10])
    dfmy['momento'].loc[11] = (dfmy['dec'].loc[11] * dfmy['pp'].loc[11])
    dfmy['momento'].loc[12] = (dfmy['dec'].loc[12] * dfmy['pp'].loc[12])
    dfmy['momento'].loc[13] = (dfmy['dec'].loc[13] * dfmy['pp'].loc[13])
    cycg = dfmy['momento'].loc[0]+dfmy['momento'].loc[1]+dfmy['momento'].loc[2] + dfmy['momento'].loc[3] + dfmy['momento'].loc[4] + dfmy['momento'].loc[5] + dfmy['momento'].loc[6] + \
        dfmy['momento'].loc[7] + dfmy['momento'].loc[8] + dfmy['momento'].loc[9] + \
        dfmy['momento'].loc[10] + dfmy['momento'].loc[11] + \
        dfmy['momento'].loc[12] + dfmy['momento'].loc[13]

    # print(dfmy)
    print(cycg)
    #####################################################################
    plt.plot(cxcg, cycg, marker="o", color="red")
    plt.show()


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

# create button to scan the points of Segmental method
saveBtn = tk.Button(
    win, text='Modelo de alambre y Centro de gravedad', command=model)
#saveBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)
saveBtn.pack(expand=tk.FALSE, side=tk.TOP)


win.mainloop()
