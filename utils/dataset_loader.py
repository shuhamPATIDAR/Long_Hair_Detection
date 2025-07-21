import os
import cv2
import numpy as np

def load_utkface_images(data_dir, img_size=(128, 128)):
    images, ages, genders = [], [], []
    allowed_exts = ['.jpg', '.jpeg', '.png']

    for filename in os.listdir(data_dir):
        file_ext = filename.lower()
        if not (file_ext.endswith('.jpg') or file_ext.endswith('.png') or file_ext.endswith('.jpeg')):
            continue  # Skip non-image files

        try:
            parts = filename.split('_')
            if len(parts) < 4:
                continue  # Skip improperly named files

            age = int(parts[0])
            gender = int(parts[1])  # 0 = Male, 1 = Female

            img_path = os.path.join(data_dir, filename)
            img = cv2.imread(img_path)

            if img is None:
                print(f"Image not readable: {filename}")
                continue

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, img_size)
            img = img / 255.0  # Normalize

            images.append(img)
            ages.append(age)
            genders.append(gender)

        except Exception as e:
            print(f"Error loading {filename}: {e}")
            continue

    return np.array(images), np.array(ages), np.array(genders)
