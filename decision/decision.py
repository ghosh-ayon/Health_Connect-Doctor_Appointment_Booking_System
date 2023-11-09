import joblib
import pandas as pd

# Load the trained model
model_filename = 'data/output/model.pkl'  # Replace with the actual filename
clf = joblib.load(model_filename)

# Load the dataset from a CSV file
dataset = pd.read_csv('data/input/data.csv')  # Replace with the actual file path

# Create the condition-to-index mapping from the dataset
condition_to_index = {condition: index for index, condition in enumerate(dataset['Condition'])}

# Create the list of doctors from the dataset
doctors = dataset['Doctor'].tolist()

while True:
    condition = input("Enter the patient's condition: ")

    # Check if the condition exists in the mapping
    if condition in condition_to_index:
        condition_index = condition_to_index[condition]
        if 0 <= condition_index < len(doctors):
            recommended_doctor = doctors[condition_index]
            print(f"Recommended Doctor: {recommended_doctor}")
        else:
            print("Invalid condition index")
    else:
        print("Condition not recognized")
