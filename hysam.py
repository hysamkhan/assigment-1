import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 📂 Load the dataset
file_path = "/Users/hysamkhan/Downloads/ODI Cricket Data new.csv"
df = pd.read_csv(file_path)

# 🛠 Fix the 'strike_rate' column (Remove extra dots)
df["strike_rate"] = df["strike_rate"].astype(str).apply(
    lambda x: x.replace(".", "", x.count(".") - 1)
)


df["strike_rate"] = pd.to_numeric(
    df["strike_rate"], errors="coerce"
)


# 🎭 Convert categorical values to numeric (like 'role')
label_encoder = LabelEncoder()
df["role"] = label_encoder.fit_transform(df["role"])

# 📊 Select features (X) and target variable (y)
X = df[
    [
        "strike_rate",
        "total_balls_faced",
        "total_matches_played",
        "matches_won",
        "matches_lost",
    ]
].copy()
y = df["total_runs"]  # Predicting total runs

# 🤖 Handle missing values by replacing them with the column mean
X.fillna(X.mean(), inplace=True)

# 🎯 Split into Training & Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 📈 Train a Machine Learning Model (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

# 📊 Make predictions
y_pred = model.predict(X_test)

# 🔍 Evaluate Model
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.2f}")

# 🔮 Example: Predict runs for a new player
new_data = pd.DataFrame(
    [[85.0, 12000, 500, 300, 200]],
    columns=X.columns,
)
predicted_runs = model.predict(new_data)
print(f"Predicted Total Runs: {predicted_runs[0]:.2f}")

# 📌 Step 1: Create 'models' folder if it doesn't exist
model_dir = "models"
os.makedirs(model_dir, exist_ok=True)

# 📌 Step 2: Save the trained model
model_path = os.path.join(model_dir, "cricket_model.pkl")
joblib.dump(model, model_path)

print(f"Model saved at: {model_path}")
