import pickle
import numpy as np
from PIL import Image

# Load model
with open("model/fake_account_model.pkl", "rb") as f:
    model = pickle.load(f)

def extract_features(name: str, followers: int, following: int, image: Image.Image):
    ratio = followers / (following + 1)
    username_length = len(name)
    has_digits = any(char.isdigit() for char in name)
    return np.array([followers, following, ratio, username_length, has_digits])

def predict_fake_account(name, followers, following, file):
    image = Image.open(file.file)
    features = extract_features(name, followers, following, image)
    features = features.reshape(1, -1)
    pred = model.predict(features)[0]
    return {"is_fake": bool(pred)}
