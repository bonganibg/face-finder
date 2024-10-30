import cv2
import numpy as np
import requests

def find_person(image_url):
    image = get_image(image_url)    
    faces = get_face_locations(image)
    faces = list(map(lambda x: extract_face(x, image), faces))
    return faces

def get_image(image_url):
    response = requests.get(image_url)
    image_array = np.asarray(bytearray(response.content), dtype="uint8")

    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image


def get_face_locations(img):        
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    return faces

def extract_save_faces(faces, img):
    face_bytes = []
    for i, face in enumerate(faces):        
        person = extract_face(img, face)
        cv2.imwrite(f"face_{i}.jpg".format(i), person)


def extract_face(face, img):
    x, y, w, h = face
    return np.ascontiguousarray(img[y:y+h, x:x+w])