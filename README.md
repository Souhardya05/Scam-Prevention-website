
# Scam Prevention and Detection App

This repository contains the codebase for a comprehensive Scam Detection and Prevention App. The system utilizes machine learning models and multimedia processing to detect scams in three domains:

- **Text-based scams** (e.g., SMS or message-based fraud)
- **Voice-based scams** (e.g., scam calls)
- **Fake social media accounts** (based on profile screenshots and metadata)

---

## 🔧 Features

### 1. Text Scam Detection
- Detects scam attempts in text messages.
- Uses Natural Language Processing (NLP) and a trained classifier model.

### 2. Voice Scam Detection
- Identifies scam calls using voice samples.
- Converts voice input into text and analyzes it using ML models.

### 3. Fake Account Detection
- Detects fake social media profiles using:
  - Profile image (screenshot of the account)
  - Username
  - Followers and Following count
- Extracts image features and combines them with textual metadata for detection.

---

## 🧠 Machine Learning Models

### Text & Voice Detection
- NLP-based preprocessing.
- Trained with a supervised learning classifier.
- For voice, audio is converted to text using `speech_recognition`.

### Fake Account Detection
- Features used:
  - Followers
  - Following
  - Follower/Following ratio
  - Username length
  - Average RGB values from profile image
  - Presence of common spammy keywords in usernames
- Model: `RandomForestClassifier`

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- OpenCV
- SpeechRecognition
- PIL

### Frontend
- Node.js
- Express.js
- EJS
- JavaScript
- CSS
- Multer (for file uploads)

---

## 📂 Folder Structure

```
📁 scam-prevention-app/
├── backend/
│   ├── main.py
│   ├── models/
│   └── requirements.txt
├── frontend/
│   ├── views/
│   ├── public/
│   ├── routes/
│   ├── app.js
│   └── package.json
├── README.md
```

---

## ⚙️ How It Works

1. User selects one of the three options:
   - Text Detection
   - Voice Detection
   - Fake Account Detection
2. Frontend collects input (text, voice file, or image + metadata).
3. Sends request to the appropriate FastAPI route.
4. Backend processes the data and runs prediction.
5. Prediction result is returned and displayed to the user.

---

## 📌 Future Improvements

- Add support for multilingual text/voice input.
- Improve deep learning model accuracy with larger datasets.
- Integrate a real-time scam alert system.
- Add Reinforcement Learning to adapt models based on user feedback.

---

## 👨‍💻 Authors

- Souhardya Saha (2023MEB1385)


---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
