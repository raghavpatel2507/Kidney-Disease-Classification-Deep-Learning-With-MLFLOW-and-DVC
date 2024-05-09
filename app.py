from flask import Flask, render_template, request, jsonify
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model
model = load_model("model\model.h5")

def preprocess_image(image_path):
    img = cv2.imread(image_path) 
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
   
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)
    
    
    input_image = preprocess_image(filename)
    
    
    prediction = model.predict(input_image)
    
    
    result = "Normal" if prediction < 0.5 else "Tumor"
    
    return jsonify({'result': result})

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=8080)
