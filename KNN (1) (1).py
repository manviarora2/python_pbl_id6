import pickle
import pandas as pd
import numpy as np

# 1. Load the model and the scaler
with open("knn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

print("Model and Scaler loaded successfully")

# Define feature names
feature_names = ["Household_Size", "Seasonal_Index"]

# 2. Take user input
values = input("Enter Household_Size and Seasonal_Index (separated by space): ")

# 3. Convert to float list and apply .abs() to sanitize input
# This ensures that even if a user enters -3, it is treated as 3
raw_features = [abs(float(x)) for x in values.split()]

# 4. Check input length
if len(raw_features) != len(feature_names):
    print(f"Error: Expected {len(feature_names)} values, but got {len(raw_features)}.")
    exit()

# 5. Convert to DataFrame for standardization
# The scaler expects a 2D structure (like a table)
input_df = pd.DataFrame([raw_features], columns=feature_names)

# 6. Apply Standardization
# Use .transform() to apply the mean/standard deviation from the training set
standardized_features = scaler.transform(input_df)

# 7. Predict using standardized values
prediction = model.predict(standardized_features)

# Apply .abs() to the final prediction for logical consistency
final_output = abs(prediction[0])

print(f"\n--- Results ---")
print(f"Standardized Input: {standardized_features}")
print(f"Predicted Daily Water Usage: {final_output:.2f} liters")