from flask import Flask, jsonify, request
from flask_restful import Resource, Api
#from keras.applications import inception_v3
#from keras.preprocessing import image
import base64
import json

import os
from werkzeug.utils import secure_filename




# from io import BytesIO
# from commons import get_model

# import PIL.Image as Image
# import numpy as np
# from torchvision import transforms
# import matplotlib.pyplot as plt
# import random
from inference import get_prediction


app = Flask(__name__)
api = Api(app)

UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

@app.route('/hello/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'

@app.route('/hellos/', methods=['GET', 'POST'])
def hello_worlds():
    return 'Hello, World!'

@app.route('/imageclassifier/predict/', methods=['GET','POST'])
def image_classifier():
    print("files", request.files)
    if 'file' not in request.files:
            return jsonify( message='file not found' )
    file = request.files['file']
    filename = secure_filename(file.filename)
    print(filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    prediction = get_prediction(UPLOAD_FOLDER + filename)
    
    return jsonify(
        ammount=prediction,
    )

if __name__ == '__main__':
    app.run(debug=True)

