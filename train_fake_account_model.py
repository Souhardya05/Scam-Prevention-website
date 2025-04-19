import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load Excel data
df = pd.read_excel("C:/Users/ACER/ScamDetectionMLApp/data/accounts.xlsx")

# Feature Engineering
df["follower_following_ratio"] = df["userFollowerCount"] / (df["userFollowingCount"] + 1)
df["username_length"] = df["usernameLength"]
df["has_digits"] = df["usernameDigitCount"].apply(lambda x: 1 if x > 0 else 0)

# Features and labels
X = df[["userFollowerCount", "userFollowingCount", "follower_following_ratio", "username_length", "has_digits"]]
y = df["isFake"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
with open("model/fake_account_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model/fake_account_model.pkl")
