from flask import Flask, render_template, request, jsonify, Response, redirect, url_for, make_response
from flask_static_digest import FlaskStaticDigest
import poseflask.report as report
import poseflask.model as model
from flask_cors import CORS
import numpy as np
import pandas as pd


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

        pose_list = []

        for pose in vlist:
            xpose = []
            ypose = []
            for i in range(34):
                if i % 2:
                    ypose.append(round(pose[i],3))
                else:
                    xpose.append(round(pose[i],3))
            for i in range(17):
                xpose[i] -= xpose[0]
                ypose[i] -= ypose[0]
            for i in range(17):
                if xpose[16] == 0 or ypose[16] == 0:
                    break
                xpose[i] /= xpose[16]
                ypose[i] /= ypose[16]
            resort_array = []
            for i in range(17):
                resort_array.append(round(xpose[i],3))
                resort_array.append(round(ypose[i],3))
            pose[:34] = resort_array[:]
            pose_list.append(pose)

        # print(pose_list)

        result = rep.made(pose_list)
        result_df = rep.made_dataframe(result)
        result_df2 = rep.made_dataframe(result)
        # result.to_csv('../result.csv',sep=',')
        model_result = mol.predict(result_df2)
        # print(result_df)
        print(model_result)
        print("@"*15)
        if model_result[-1] == 0:
            rep_x = "잘못 촬영되었습니다! 다시 시도해주세요!"
        else:
            rep_x = rep.report_x(rep.out_put_x_score(result_df,model_result))
            rep_y = rep.report_y(rep.out_put_y_score(result_df,model_result))
        
        # final_result = {
        #     "rep_x" : rep_x,s
        #     "rep_y" : rep_y
        # }
        return jsonify(rep_x)

    @app.route('/result/',methods=['POST','GET'])
    @app.route('/result/<string:final_result>/')
    def result(final_result=0):
        print(final_result)
        if final_result != 0:
            return render_template('result.html')
        else:
            return render_template('result.html',final_result=final_result)

    return app


