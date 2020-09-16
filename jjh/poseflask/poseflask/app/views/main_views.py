from flask import Blueprint, Flask, render_template, Response, jsonify, request
from .camera import VideoCamera

bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/test')
def test():
    return render_template('saved.html')

@bp.route('/jsontest')
def jsontest():
    return render_template('jsontest.html')

@bp.route('/jsontest2',methods=['POST'])
def jsontest2():
    print(request.json)
    return jsonify(state="JSON")