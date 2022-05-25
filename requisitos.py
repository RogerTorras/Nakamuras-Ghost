import chess
import chess.engine

import os
import time
import numpy as np

from picamera import PiCamera
import RPi.GPIO as GPIO

from natsort import natsorted

import tensorflow_hub as hub
from keras.models import load_model
from keras.preprocessing import image

a = 0