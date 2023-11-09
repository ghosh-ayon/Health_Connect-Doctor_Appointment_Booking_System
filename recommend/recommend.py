import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from scipy.sparse import vstack

class RecommendationModel:
    def __init__(self, data_path):
        # Load the appointment data from the CSV file
        self.data = pd.read_csv(data_path)

        # Preprocess data and build TF-IDF vectors
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.compute_tfidf_matrix()

        # Compute cosine similarity between appointments
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

    def compute_tfidf_matrix(self):
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        return tfidf_vectorizer.fit_transform(self.data['medical_condition'])

    def get_recommendations(self, appointment_index, num_recommendations=5):
        # Get the pairwise similarity scores of all appointments with the specified appointment
        sim_scores = list(enumerate(self.cosine_sim[appointment_index]))

        # Sort the appointments based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the top-n most similar appointments
        sim_scores = sim_scores[1:num_recommendations + 1]

        # Get the appointment indices
        appointment_indices = [x[0] for x in sim_scores]

        # Return the top-n most similar appointments
        return appointment_indices

if __name__ == "__main__":
    data_path = "data/input/appointments.csv"  # Replace with the path to your dataset
    model = RecommendationModel(data_path)

    # Example: Get recommendations for a specific appointment index
    appointment_index = 5  # Replace with the index of the appointment you want recommendations for
    recommendations = model.get_recommendations(appointment_index)
    print(f"Recommendations for appointment at index {appointment_index}:")
    for recommendation_index in recommendations:
        print(f"Recommended appointment at index {recommendation_index}")
