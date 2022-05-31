import os
import cv2
import time
import numpy as np
import tensorflow_hub as hub

from picamera import PiCamera
from natsort import natsorted
from keras.utils import load_img
from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def initModels():
    M = "./Redes Neuronales/m_mano.h5"
    P = "./Redes Neuronales/p_mano.h5"

    modelo_T = load_model(M, custom_objects = {'KerasLayer':hub.KerasLayer})
    modelo_T.load_weights(P)

    M = "./Redes Neuronales/m_colores.h5"
    P = "./Redes Neuronales/p_colores.h5"

    modelo_P = load_model(M, custom_objects = {'KerasLayer':hub.KerasLayer})
    modelo_P.load_weights(P)

    return modelo_T, modelo_P


def aplicarModelo(modelo, data, tablero, M):
    if M == 'P':
        elementos = len(os.listdir(data))
        batch_holder = np.zeros((elementos, 224, 224, 3))
        data_ordenado = natsorted(os.listdir(data))

        for i, img in enumerate(data_ordenado):
            img = load_img(os.path.join(data, img), target_size = (224, 224))
            img = np.array(img).astype(float)/255
            batch_holder[i, :] = img

        prediccion = modelo(batch_holder)
        
        contador = 0
        for i in range(int(elementos/8)):
            for j in range(int(elementos/8)):
                tablero[i, j] = np.argmax(prediccion[contador])
                contador +=  1
        return

    elif M == 'T':
        img = load_img(data, target_size = (224, 224))
        img = np.array(img).astype(float)/255
        prediccion = modelo(img.reshape(-1, 224, 224, 3))

        return np.argmax(prediccion)


def deteccionTablero(modelo_T):
    control = False

    while control == False:
        capturaImagen()
        procesaImagen()

        tablero = './Data/tablero.jpg'
        casillas = './Data/Casillas'

        control = aplicarModelo(modelo_T, tablero, None, 'T')
        if control == False:
            print("Ruido en la imagen")


def capturaImagen():            #Hacer el bucle para las fotos con la raspicam y obtener la media
    with picamera.PiCamera() as camera:
        camera.resolution = (2592, 1944)
        camera.framerate = 15
        time.sleep(5)
        camera.capture('tablero.jpg')


def procesaImagen():            #Realizar el crop de la imagen tablero.jpg y de sus casillas
    img = cv2.imread('tablero.jpg')

    """
    Obtener las coordenadas a partir del ginput
    """

    size_casilla = 0
    cnt = 1

    for i in range(0, 12, size_casilla):
        for j in range(0, 12, size_casilla):
            casilla = img[j:j+size_casilla, i:i+size_casilla]
            path = './Data/Casillas/casilla_' + str(cnt) + '.jpg'
            cv2.imwrite(path, casilla)