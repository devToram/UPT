from flask import Flask, render_template, request, jsonify, Response, redirect, url_for, make_response
from flask_static_digest import FlaskStaticDigest
import poseflask.report as report
import poseflask.model as model
from flask_cors import CORS

flask_static_digest = FlaskStaticDigest()
rep = report.Report()
mol = model.Model()

def create_app():
    app = Flask(__name__,template_folder='templates')
    CORS(app)

    flask_static_digest.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/desc')
    def desc():
        return render_template('desc.html')

    @app.route('/workout')
    def workout():
        return render_template('workout.html')
    
    @app.route('/report',methods=['POST','GET'])
    def report():
        data = request.get_json()
        vlist = []

        for d in data:
            vlist.append(list(d.values()))

        result = rep.made(vlist)
        result = rep.made_dataframe(result)
        
        # model_result = mol.predict(result)

        rep_x = rep.report_x(rep.out_put_x_score(result,rep.data))
        rep_y = rep.report_y(rep.out_put_y_score(result,rep.data))
        
        # final_result = {
        #     "rep_x" : rep_x,
        #     "rep_y" : rep_y
        # }
        final_result = "1"
        return jsonify(final_result)

    @app.route('/result/',methods=['POST','GET'])
    @app.route('/result/<string:final_result>/')
    def result(final_result=0):
        print(final_result)
        if final_result != 0:
            return render_template('result.html')
        else:
            return render_template('result.html',final_result=final_result)

    return app


