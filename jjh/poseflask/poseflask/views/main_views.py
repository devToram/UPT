from flask import Blueprint, Flask, render_template, Response, jsonify, request, send_from_directory, url_for
import os

# bp = Blueprint('main', __name__,url_prefix='/')
bp = Blueprint('main', __name__,static_folder="../static")

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/test')
def test():
    return render_template('saved.html')

@bp.route('/index2')
def index2():
    return render_template('toram_UPT_demo.html')

@bp.route('/index22',methods=['POST'])
def index22():
    print(request.json)

@bp.route('/jsontest')
def jsontest():
    return render_template('jsontest.html')

@bp.route('/jsontest2',methods=['POST'])
def jsontest2():
    print(request.json)
    return jsonify(state="JSON")

@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')