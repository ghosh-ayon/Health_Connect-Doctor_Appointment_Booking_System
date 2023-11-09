import pandas as pd
from sklearn.neural_network import MLPClassifier
import joblib

# Load the dataset from a CSV file (replace 'your_dataset.csv' with the actual file path)
file_path = 'data/input/data.csv'  # Replace with the actual file path
dataset = pd.read_csv(file_path)

# Preprocess the data (ensure that column names are consistent)
dataset.columns = dataset.columns.str.strip()

# Extract the 'Condition' and 'Doctor' columns from the dataset
conditions = dataset['Condition']
doctors = dataset['Doctor']

# Map unique conditions and doctors to numerical values
unique_conditions = conditions.unique()
unique_doctors = doctors.unique()

condition_to_index = {condition: index for index, condition in enumerate(unique_conditions)}
doctor_to_index = {doctor: index for index, doctor in enumerate(unique_doctors)}

# Replace condition and doctor names with numerical values in the dataset
conditions = conditions.map(condition_to_index)
doctors = doctors.map(doctor_to_index)

# Create a simple neural network classifier
clf = MLPClassifier(hidden_layer_sizes=(10,), max_iter=10000, activation="relu", solver="adam")

# Train the model
X_train = conditions.values.reshape(-1, 1)  # Reshape to 2D array
y_train = doctors

clf.fit(X_train, y_train)

# Save the trained model
model_filename = 'data/output/model.pkl'  # Choose a filename
joblib.dump(clf, model_filename)
