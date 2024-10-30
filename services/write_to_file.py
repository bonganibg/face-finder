import os
import cv2

def write_to_file(image, image_name, folder):
    create_folder(folder)

    full_path = f"{folder}/{image_name}"

    cv2.imwrite(full_path, image)

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder) 

