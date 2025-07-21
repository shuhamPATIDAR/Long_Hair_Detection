import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

from utils.predictors import final_gender_prediction

class GenderPredictionApp:
    def __init__(self, master):
        self.master = master
        master.title("Long Hair Identification - Gender Predictor")
        master.geometry("500x600")
        master.configure(bg="#f0f0f0")

        self.image_path = None
        self.hair_length = tk.IntVar(value=0)  # 0 = Short Hair, 1 = Long Hair

        self.title_label = tk.Label(master, text="Long Hair Identification", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.upload_button = tk.Button(master, text="Upload Image", command=self.upload_image, font=("Arial", 12))
        self.upload_button.pack(pady=10)

        self.image_label = tk.Label(master)
        self.image_label.pack(pady=10)

        self.hair_length_label = tk.Label(master, text="Select Hair Length:", font=("Arial", 12), bg="#f0f0f0")
        self.hair_length_label.pack(pady=5)

        self.short_radio = tk.Radiobutton(master, text="Short Hair", variable=self.hair_length, value=0, font=("Arial", 12), bg="#f0f0f0")
        self.short_radio.pack()

        self.long_radio = tk.Radiobutton(master, text="Long Hair", variable=self.hair_length, value=1, font=("Arial", 12), bg="#f0f0f0")
        self.long_radio.pack()

        self.predict_button = tk.Button(master, text="Predict Gender", command=self.predict_gender, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.predict_button.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 14), bg="#f0f0f0")
        self.result_label.pack(pady=10)


    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image_path = file_path
            image = Image.open(file_path)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def predict_gender(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please upload an image first.")
            return

        hair_length_value = self.hair_length.get()

        result = final_gender_prediction(self.image_path, hair_length_value)

        age_group = result['age_group']
        predicted_gender = result['predicted_gender']

        age_text = {
            0: "Age < 20",
            1: "Age between 20–30",
            2: "Age > 30"
        }[age_group]

        gender_text = "Female" if predicted_gender == 1 else "Male"

        self.result_label.config(text=f"{age_text}\nPredicted Gender: {gender_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GenderPredictionApp(root)
    root.mainloop()
