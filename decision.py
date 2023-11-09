from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

tfidf_vectorizer = TfidfVectorizer()
clf = MultinomialNB()

class Decision:
    def __init__(self, label_encoder_file, clf_file):
        # Load the trained label encoder and Naive Bayes classifier model
        with open(label_encoder_file, 'rb') as file:
            self.label_encoder = pickle.load(file)
        with open(clf_file, 'rb') as file:
            self.clf = pickle.load(file)

    def train_model(self, X, y):
        # Initialize and train the decision tree model
        self.model = DecisionTreeClassifier()
        self.model.fit(X, y)

    def save_model(self):
        # Save the trained decision tree model to a file
        with open(self.model_file, 'wb') as file:
            pickle.dump(self.model, file)

        # Save the label encoder object to a file
        with open(self.label_encoder_file, 'wb') as file:
            pickle.dump(self.label_encoder, file)

    def load_model(self):
        # Load the trained decision tree model from the file
        with open(self.model_file, 'rb') as file:
            self.model = pickle.load(file)

        # Load the label encoder object from the file
        with open(self.label_encoder_file, 'rb') as file:
            self.label_encoder = pickle.load(file)

    def make_recommendation(self, patient_condition):
            # Transform the patient condition text into numerical features using TF-IDF
            tfidf_features = tfidf_vectorizer.transform([patient_condition])

            # Make predictions using the trained Naive Bayes classifier
            predicted_specialty = self.clf.predict(tfidf_features)

            # Map the predicted label back to the specialty name
            recommended_specialty = self.label_encoder.inverse_transform(predicted_specialty)[0]

            # Refine recommendations based on predictions (add rules here if needed)
            if 'fever' in patient_condition and 'cough' in patient_condition and recommended_specialty != 'Internal Medicine':
                recommended_specialty = 'Internal Medicine'
            elif 'rash' in patient_condition and recommended_specialty != 'Dermatology':
                recommended_specialty = 'Dermatology'
            elif 'chest pain' in patient_condition and recommended_specialty != 'Cardiology':
                recommended_specialty = 'Cardiology'
            elif 'headache' in patient_condition and recommended_specialty != 'Neurology':
                recommended_specialty = 'Neurology'
            elif 'abdominal pain' in patient_condition and recommended_specialty != 'Gastroenterology':
                recommended_specialty = 'Gastroenterology'
            elif 'fever' in patient_condition and 'cough' in patient_condition and recommended_specialty != 'Internal Medicine':
                recommended_specialty = 'Internal Medicine'
            elif 'rash' in patient_condition and recommended_specialty != 'Dermatology':
                recommended_specialty = 'Dermatology'
            elif 'chest pain' in patient_condition and recommended_specialty != 'Cardiology':
                recommended_specialty = 'Cardiology'
            elif 'headache' in patient_condition and recommended_specialty != 'Neurology':
                recommended_specialty = 'Neurology'
            elif 'abdominal pain' in patient_condition and recommended_specialty != 'Gastroenterology':
                recommended_specialty = 'Gastroenterology'
            elif 'shortness of breath' in patient_condition and recommended_specialty != 'Pulmonology':
                recommended_specialty = 'Pulmonology'
            elif 'joint pain' in patient_condition and recommended_specialty != 'Rheumatology':
                recommended_specialty = 'Rheumatology'
            elif 'blurred vision' in patient_condition and recommended_specialty != 'Ophthalmology':
                recommended_specialty = 'Ophthalmology'
            elif 'fatigue' in patient_condition and recommended_specialty != 'Endocrinology':
                recommended_specialty = 'Endocrinology'
            elif 'dizziness' in patient_condition and recommended_specialty != 'Otolaryngology':
                recommended_specialty = 'Otolaryngology'
            elif 'urinary problems' in patient_condition and recommended_specialty != 'Urology':
                recommended_specialty = 'Urology'
            elif 'anxiety' in patient_condition and recommended_specialty != 'Psychiatry':
                recommended_specialty = 'Psychiatry'
            elif 'numbness' in patient_condition and recommended_specialty != 'Physical Medicine and Rehabilitation':
                recommended_specialty = 'Physical Medicine and Rehabilitation'
            elif 'memory loss' in patient_condition and recommended_specialty != 'Geriatrics':
                recommended_specialty = 'Geriatrics'
            elif 'weight loss' in patient_condition and recommended_specialty != 'Nutrition':
                recommended_specialty = 'Nutrition'
            elif 'hearing loss' in patient_condition and recommended_specialty != 'Audiology':
                recommended_specialty = 'Audiology'
            elif 'toothache' in patient_condition and recommended_specialty != 'Dentistry':
                recommended_specialty = 'Dentistry'
            elif 'swelling' in patient_condition and recommended_specialty != 'Plastic Surgery':
                recommended_specialty = 'Plastic Surgery'
            elif 'feeling down' in patient_condition and recommended_specialty != 'Psychology':
                recommended_specialty = 'Psychology'
            elif 'difficulty swallowing' in patient_condition and recommended_specialty != 'Gastroenterology':
                recommended_specialty = 'Gastroenterology'
            elif 'skin infection' in patient_condition and recommended_specialty != 'Dermatology':
                recommended_specialty = 'Dermatology'
            elif 'constipation' in patient_condition and recommended_specialty != 'Gastroenterology':
                recommended_specialty = 'Gastroenterology'
            elif 'hair loss' in patient_condition and recommended_specialty != 'Dermatology':
                recommended_specialty = 'Dermatology'
            elif 'irregular heartbeat' in patient_condition and recommended_specialty != 'Cardiology':
                recommended_specialty = 'Cardiology'
            elif 'coughing up blood' in patient_condition and recommended_specialty != 'Pulmonology':
                recommended_specialty = 'Pulmonology'
            elif 'speech difficulties' in patient_condition and recommended_specialty != 'Speech-Language Pathology':
                recommended_specialty = 'Speech-Language Pathology'
            elif 'muscle weakness' in patient_condition and recommended_specialty != 'Neurology':
                recommended_specialty = 'Neurology'
            elif 'burning sensation' in patient_condition and recommended_specialty != 'Dermatology':
                recommended_specialty = 'Dermatology'
            elif 'difficulty breathing' in patient_condition and recommended_specialty != 'Pulmonology':
                recommended_specialty = 'Pulmonology'
            elif 'blood in urine' in patient_condition and recommended_specialty != 'Urology':
                recommended_specialty = 'Urology'
            elif 'fainting' in patient_condition and recommended_specialty != 'Cardiology':
                recommended_specialty = 'Cardiology'
            elif 'tingling sensation' in patient_condition and recommended_specialty != 'Neurology':
                recommended_specialty = 'Neurology'
            elif 'loss of appetite' in patient_condition and recommended_specialty != 'Gastroenterology':
                recommended_specialty = 'Gastroenterology'
            elif 'visual disturbances' in patient_condition and recommended_specialty != 'Ophthalmology':
                recommended_specialty = 'Ophthalmology'
            elif 'excessive thirst' in patient_condition and recommended_specialty != 'Endocrinology':
                recommended_specialty = 'Endocrinology'
            elif 'excessive urination' in patient_condition and recommended_specialty != 'Urology':
                recommended_specialty = 'Urology'
            elif 'poor coordination' in patient_condition and recommended_specialty != 'Neurology':
                recommended_specialty = 'Neurology'
            elif 'blood in stool' in patient_condition and recommended_specialty != 'Gastroenterology':
                recommended_specialty = 'Gastroenterology'
            elif 'loss of balance' in patient_condition and recommended_specialty != 'Physical Medicine and Rehabilitation':
                recommended_specialty = 'Physical Medicine and Rehabilitation'
            elif 'sore throat' in patient_condition and recommended_specialty != 'Otolaryngology':
                recommended_specialty = 'Otolaryngology'
            elif 'swollen glands' in patient_condition and recommended_specialty != 'Otolaryngology':
                recommended_specialty = 'Otolaryngology'
            elif 'double vision' in patient_condition and recommended_specialty != 'Ophthalmology':
                recommended_specialty = 'Ophthalmology'
            elif 'problems with taste' in patient_condition and recommended_specialty != 'Otolaryngology':
                recommended_specialty = 'Otolaryngology'
            elif 'night sweats' in patient_condition and recommended_specialty != 'Internal Medicine':
                recommended_specialty = 'Internal Medicine'
            elif 'unexplained weight loss' in patient_condition and recommended_specialty != 'Internal Medicine':
                recommended_specialty = 'Internal Medicine'
            elif 'persistent cough' in patient_condition and recommended_specialty != 'Pulmonology':
                recommended_specialty = 'Pulmonology'
            elif 'hoarse voice' in patient_condition and recommended_specialty != 'Otolaryngology':
                recommended_specialty = 'Otolaryngology'
            elif 'loss of smell' in patient_condition and recommended_specialty != 'Otolaryngology':
                recommended_specialty = 'Otolaryngology'
            elif 'ear pain' in patient_condition and recommended_specialty != 'Otolaryngology':
                recommended_specialty = 'Otolaryngology'
            elif 'ear discharge' in patient_condition and recommended_specialty != 'Otolaryngology':
                recommended_specialty = 'Otolaryngology'
            elif 'ear ringing' in patient_condition and recommended_specialty != 'Otolaryngology':
                recommended_specialty = 'Otolary'

            
            return recommended_specialty
