import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the dataset from a CSV file
data = pd.read_csv('data/input/data.csv')

data['Condition'] = data['Condition'].fillna('Unknown')

data = data.dropna()

# Split the dataset into features (X) and labels (y)
X = data['Condition']  # Features
y = data['Doctor']   # Labels

# Vectorize patient conditions
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Initialize and train the decision tree model
model = DecisionTreeClassifier()
model.fit(X_vectorized, y)

# Save the trained model and vectorizer to files
with open('data/output/tree_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('data/output/vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print('Training completed. Model and vectorizer saved to tree_model.pkl and vectorizer.pkl respectively.')
