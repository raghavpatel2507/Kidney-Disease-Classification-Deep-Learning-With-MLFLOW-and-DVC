import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import tensorflow as tf


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Predict
        result = model.predict(test_image)
        print("Raw Prediction:", result)  # Print raw prediction
        
        predicted_class_index = np.argmax(result, axis=1)
        print("Predicted Class Index:", predicted_class_index)
        
        if predicted_class_index[0] == 1:
            prediction = 'Tumor'
            return [{"image": prediction}]
        else:
            prediction = 'Normal'
            return [{"image": prediction}]

