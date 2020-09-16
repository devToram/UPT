from threading import Thread, Lock
import cv2
import numpy as np
import imutils
from imutils.video import WebcamVideoStream
import time
from werkzeug.utils import secure_filename
import os
from flask import Flask
import tensorflow as tf
import math


uploads_dir = os.path.join(Flask(__name__).instance_path, 'uploads')
if os.path.isdir(uploads_dir):
    os.chdir(uploads_dir)
else:
    os.makedirs(uploads_dir)
    
path = os.path.join(uploads_dir, secure_filename("output.avi"))

class VideoCamera(object):

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src + cv2.CAP_DSHOW)
        self.out = cv2.VideoWriter(path,cv2.VideoWriter_fourcc(*'DIVX'), 30, (640,480))
        (self.grabbed, self.frame) = self.stream.read()
        self.started = False
        self.read_lock = Lock()
        

    def start(self):
        if self.started:
            print("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):
        while self.started:
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()


    def read(self):
        try:
            self.read_lock.acquire()
            frame = self.frame.copy()
            self.read_lock.release()
            return frame
        except:
            pass

    def stop(self):
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stream.release()
        self.out.release()
        cv2.destoryAllWindows()

    def write(self,frame):
        self.out.write(frame)

    def writeClose(self):
        self.out = None


    