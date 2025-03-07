import joblib
import pandas as pd
import pytest

# Load the trained model
model = joblib.load("models/cricket_model.pkl")

# Sample test data
test_data = pd.DataFrame(
    [[85.0, 12000, 500, 300, 200]],
    columns=["strike_rate", "total_balls_faced", "total_matches_played", "matches_won", "matches_lost"],
)

def test_prediction_output():
    """Test if model prediction gives a valid number."""
    prediction = model.predict(test_data)
    assert isinstance(prediction[0], (int, float))  # Check if output is a number
    assert prediction[0] > 0  # Runs should be positive
