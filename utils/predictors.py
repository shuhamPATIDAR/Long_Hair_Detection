import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2

# Load trained models
age_model = load_model('models/age_model.h5')
gender_model = load_model('models/gender_model.h5')


# Preprocess input image
def preprocess_image(image_path, img_size=(128, 128)):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, img_size)
    img = img / 255.0
    return np.expand_dims(img, axis=0)   # Model expects 4D input


# Predict Age Group (0: <20, 1: 20–30, 2: >30)
def predict_age(image_path):
    img = preprocess_image(image_path)
    pred = age_model.predict(img)
    return np.argmax(pred)   # Returns 0, 1, or 2


# Predict Gender (0: Male, 1: Female)
def predict_gender(image_path):
    img = preprocess_image(image_path)
    pred = gender_model.predict(img)
    return int(pred[0][0] > 0.5)   # Threshold for sigmoid output


  # Threshold for sigmoid output


# Final Gender Prediction using Task-Specific Logic

def final_gender_prediction(image_path, manual_hair_length):
    age_group = predict_age(image_path)
    true_gender = predict_gender(image_path)

    # manual_hair_length: 1 = Long, 0 = Short (User provides via GUI)

    if age_group == 1:  # Age between 20–30
        if manual_hair_length == 1:
            predicted_gender = 1   # Long Hair => Female
        else:
            predicted_gender = 0   # Short Hair => Male
    else:
        predicted_gender = true_gender  # Use true gender outside 20–30

    return {
        'age_group': age_group,
        'manual_hair_length': manual_hair_length,
        'predicted_gender': predicted_gender,
        'true_gender': true_gender
    }


