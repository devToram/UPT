import pyrebase

config = {
    "apiKey": "AIzaSyCvKCIVolQ20yXNEtRTyB05Nz3wpXBM5r8",
    "authDomain": "poseflask-f554a.firebaseapp.com",
    "databaseURL": "https://poseflask-f554a.firebaseio.com",
    "storageBucket": "poseflask-f554a.appspot.com",
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

from flask import Blueprint, Flask, request, jsonify, Response
import cv2
import numpy as np
from werkzeug.utils import secure_filename
import os

bp = Blueprint('video_save', __name__, url_prefix='/video_save')

uploads_dir = os.path.join(Flask(__name__).instance_path, 'uploads')
if os.path.isdir(uploads_dir):
    os.chdir(uploads_dir)
else:
    os.makedirs(uploads_dir)
path = os.path.join(uploads_dir, secure_filename("output.avi"))

def gen_frame(cap):
    while cap:
        _, frame = cap.read()
        height, width, _ = frame.shape
        x = height if height > width else width
        y = height if height > width else width
        square= np.zeros((x,y,3), np.uint8)
        square[int((y-height)/2):int(y-(y-height)/2), int((x-width)/2):int(x-(x-width)/2)] = frame
        frame = square
        convert = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + convert + b'\r\n')


@bp.route('/video_save', methods=['POST'])
def video_save():
    upload = path
    storage.child('outpy.avi').put(upload)
    return jsonify("REC Save")

@bp.route('/saved')
def saved():
    storage.child('outpy.avi').download('./','downloaded.avi')
    capt = cv2.VideoCapture('downloaded.avi')
    return Response(gen_frame(capt),
                mimetype='multipart/x-mixed-replace; boundary=frame')