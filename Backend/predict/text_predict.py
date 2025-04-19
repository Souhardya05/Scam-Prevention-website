import pickle
import os

# Load model and vectorizer
model_path = os.path.join("model", "text_model.pkl")
with open(model_path, "rb") as f:
    vectorizer, model = pickle.load(f)

def predict_text(text: str) -> str:
    vect_text = vectorizer.transform([text])
    pred = model.predict(vect_text)[0]
    return "Scam ❌" if pred == 1 else "Safe ✅"
