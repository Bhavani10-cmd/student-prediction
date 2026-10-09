import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("student_performance.csv")

# Features
X = data[[
    "StudyHours",
    "Attendance",
    "PreviousMarks",
    "Assignments",
    "SleepHours"
]]

# Target
y = data["FinalScore"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully")
print("Mean Absolute Error:", mae)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")