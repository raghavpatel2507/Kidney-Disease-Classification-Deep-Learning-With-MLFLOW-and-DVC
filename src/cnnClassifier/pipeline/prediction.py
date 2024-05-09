import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import cv2

# Disable TensorFlow warnings
tf.get_logger().setLevel('ERROR')

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = load_model("model\model.h5")

        imagename = self.filename
        img = cv2.imread(imagename)
        img = cv2.resize(img, (224, 224))  # Resize the image to match the input shape of the model
        img = np.expand_dims(img, axis=0)
    
        # Predict
        result = model.predict(img)
        print("Raw Prediction:", result)  # Print raw prediction
        
        predicted_class_index = np.argmax(result, axis=1)
        print("Predicted Class Index:", predicted_class_index)
        
        if predicted_class_index[0] < 0.5:
            prediction = 'Normal'
            return [{"image": prediction}]
        else:
            prediction = 'Tumor'
            return [{"image": prediction}]
