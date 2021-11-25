from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from modelHelper import ModelHelper


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# global helper classes
modelHelper = ModelHelper()

# HTML Renders
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index2():
    return render_template("index2.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")


@app.route("/tab")
def tab():
    return render_template("tab.html")

@app.route("/work_cited")
def work_cited():
    return render_template("work_cited.html")

@app.route("/write_up")
def write_up():
    return render_template("write_up.html")

# BUTTON Routes
# this route pulls our work from the site and pushes to python, 
# @app.route("/makePredictions", methods=["POST"])
# def makePredictions():
#     content = request.json["data"]




@app.route('/makePredictions', methods=['POST'])
def my_form_post():
    text = request.form['textArea']
    processed_text = text.upper()
    prediction = modelHelper.makePredictions(processed_text)
    print(prediction)
    return(jsonify({"ok": True, "prediction": str(prediction)}))

print(my_form_post)

 
if __name__ == "__main__":
    app.run(debug=True)
