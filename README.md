# Long_Hair_Detection

🎇 Long Hair Identification – Gender Prediction System

This project implements a machine learning-based image classifier that predicts a person’s gender with custom logic:

For people aged 20–30:

Long Hair → Predict as Female (even if the true gender is male).

Short Hair → Predict as Male (even if the true gender is female).

For people below 20 or above 30:

Predict actual gender using the trained gender model.

The project also includes a simple Tkinter GUI to upload images, manually select hair length, and view predictions.

📌 Project Features

✅ Age Group Classification (Below 20, 20–30, Above 30).

✅ Gender Classification (Male/Female).

✅ Manual Hair-Length Input via GUI.

✅ Task-Specific Logic applied:

Long-haired individuals between 20–30 predicted as female.

Short-haired individuals between 20–30 predicted as male.

✅ Tkinter GUI for easy interaction.

🛠️ Project Structure

    LongHairIdentification/
    ├── models/
    │   ├── age_model.h5
    │   ├── gender_model.h5
    ├── utils/
    │   ├── __init__.py
    │   ├── dataset_loader.py
    │   ├── predictors.py
    ├── gui/
    │   └── app_gui.py
    ├── dataset/   (Optional: if retraining)
    ├── notebooks/ (Optional: training notebooks)
    └── README.md
    
🚀 How to Run the GUI

1. Ensure you have:
  -->Python 3.8+
  -->Required libraries (tensorflow, opencv-python, PIL)

3. Place trained models inside /models/:
  -->age_model.h5
  -->gender_model.h5

4. In terminal (from project root):
  -->python gui/app_gui.py

5. Upload an image, select hair length manually, and click "Predict Gender" to view results.

📊 Dataset Used

We used the UTKFace Dataset for training age and gender classification models.

📦 UTKFace Dataset on Kaggle:

    https://www.kaggle.com/datasets/jangedoo/utkface-new

Dataset Details:

20,000+ face images.

Each image filename contains:

Age

Gender (0: Male, 1: Female)

Ethnicity

No hair-length labels — hence hair-length input is manually selected via GUI

📊 Models Used

Age Model: Classifies image into 3 age categories.

Gender Model: Classifies true gender.

Hair-Length Detection: Manual input via GUI (no model).

📋 Logic Overview
Age 20–30:

Long Hair → Predict as Female

Short Hair → Predict as Male

Age <20 or >30:

Predict true gender using gender model.

💡 Why Manual Hair-Length Input?

Due to dataset limitations, hair-length detection is done via manual input. This keeps the system functional while meeting the project’s logic and evaluation requirements.

📌 Project Purpose

This project was built as a problem-solving and logic-building exercise to combine deep learning with custom business logic. It’s designed to:

Apply AI models in non-standard conditions.

Build decision systems beyond direct predictions.
