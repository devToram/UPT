from flask import Blueprint, Flask, render_template, Response, request, url_for, jsonify
from werkzeug.utils import redirect
from .camera import VideoCamera
import cv2
import time


bp = Blueprint('video_feed', __name__, url_prefix='/video_feed')

cap = VideoCamera().start()

def gen_frame(rec=''):
    if rec == 'rec':
        while cap:
            frame = cap.read()
            cap.write(frame)
            convert = cv2.imencode('.jpg', frame)[1].tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + convert + b'\r\n')
    else:
        while cap:
            frame = cap.read()
            convert = cv2.imencode('.jpg', frame)[1].tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + convert + b'\r\n')

def stop_frame():
    cap.writeClose()

    
@bp.route('/video_feed/', methods=['POST','GET'])
def video_feed():
    if request.method == 'POST':
        return Response(gen_frame('rec'),
                mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@bp.route('/rec_stop', methods=['POST'])
def rec_stop():
    stop_frame()
    return jsonify("REC Stop")