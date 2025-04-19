import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Example dataset
data = {
    "message": [
        "You've won a free iPhone! Click here to claim.",
        "Urgent! Update your bank details now.",
        "Hello, how are you?",
        "Meeting at 5 PM tomorrow",
        "Your account has been compromised. Reset your password.",
        "Hey bro, let's play cricket!",
        "Claim your lottery prize now!"
    ],
    "label": [1, 1, 0, 0, 1, 0, 1]  # 1 = Scam, 0 = Not scam
}

df = pd.DataFrame(data)

X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF + Naive Bayes pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
with open("model/text_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved to model/text_model.pkl")
