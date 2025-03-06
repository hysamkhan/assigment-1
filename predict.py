import joblib
import pandas as pd

# Load the trained model
model_path = "models/cricket_model.pkl"
loaded_model = joblib.load(model_path)

# Example: Predict runs for a new player
new_data = pd.DataFrame([[85.0, 12000, 500, 300, 200]], columns=["strike_rate", "total_balls_faced", "total_matches_played", "matches_won", "matches_lost"])
predicted_runs = loaded_model.predict(new_data)

print(f"Predicted Total Runs (Using Saved Model): {predicted_runs[0]:.2f}")
