import pandas as pd
from sklearn.neural_network import MLPClassifier
import joblib

# Load the first dataset from a CSV file
file_path1 = 'recommend/data/input/general.csv'  # Replace with the actual file path
dataset1 = pd.read_csv(file_path1)

# Load the second dataset from a CSV file
file_path2 = 'recommend/data/input/specialist.csv'  # Replace with the actual file path
dataset2 = pd.read_csv(file_path2)

# Concatenate the two datasets vertically
merged_dataset = pd.concat([dataset1, dataset2], ignore_index=True)

# Preprocess the merged data (ensure that column names are consistent)
merged_dataset.columns = merged_dataset.columns.str.strip()

# Extract the 'Condition' and 'Doctor' columns from the merged dataset
conditions = merged_dataset['Condition']
doctors = merged_dataset['Doctor']

# Map unique conditions and doctors to numerical values
unique_conditions = conditions.unique()
unique_doctors = doctors.unique()

condition_to_index = {condition: index for index, condition in enumerate(unique_conditions)}
doctor_to_index = {doctor: index for index, doctor in enumerate(unique_doctors)}

# Replace condition and doctor names with numerical values in the dataset
conditions = conditions.map(condition_to_index)
doctors = doctors.map(doctor_to_index)

# Create a simple neural network classifier
clf = MLPClassifier(hidden_layer_sizes=(20,), max_iter=10000, activation="relu", solver="adam")

# Train the model
X_train = conditions.values.reshape(-1, 1)  # Reshape to 2D array
y_train = doctors

clf.fit(X_train, y_train)

# Save the trained model
model_filename = 'recommend/data/output/model.pkl'  # Choose a filename
joblib.dump(clf, model_filename)

# Print a message after training
print("Model has been trained & successfully and saved as", model_filename)
