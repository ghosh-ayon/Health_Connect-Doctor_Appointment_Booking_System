import csv
from faker import Faker
import random
import datetime

fake = Faker()

# Create a list to store the generated data
data = []

# Define a list of relevant medical conditions
medical_conditions = ["Heart Checkup", "Skin Allergy", "Back Pain", "Child's Checkup", "Headache", "Anxiety"]

# Generate data for 6 appointments
for i in range(1, 10000):
    user_id = i
    patient_name = fake.name()
    patient_age = random.randint(18, 70)
    patient_gender = random.choice(["Male", "Female"])
    doctor_id = 100 + i
    doctor_name = fake.name()
    doctor_specialty = fake.random_element(elements=("Diabetes", "Hypertension", "Arthritis", "Asthma", "Cancer", "Depression", "Alzheimer's", "Autism", "Heart disease", "Stroke", "Osteoporosis", "Migraine", "Schizophrenia", "Influenza", "HIV/AIDS", "Epilepsy", "Parkinson's", "Multiple sclerosis", "COPD (Chronic Obstructive Pulmonary Disease)", "Anemia", "Allergies", "Obesity", "Celiac disease", "Crohn's disease", "Lupus", "Fibromyalgia", "Psoriasis", "Osteoarthritis", "Rheumatoid arthritis", "Eczema", "Heart Checkup", "Skin Allergy", "Back Pain", "Child's Checkup", "Headache", "Anxiety"))
    appointment_date = (datetime.date(2023, 11, 10) + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    appointment_time = fake.time(pattern="%I:%M %p")
    medical_condition = random.choice(medical_conditions)
    rating = round(random.uniform(3.5, 5.0), 1)
    review = fake.text(max_nb_chars=200)  # Generate longer and more coherent reviews

    data.append([user_id, patient_name, patient_age, patient_gender, doctor_id, doctor_name, doctor_specialty,
                 appointment_date, appointment_time, medical_condition, rating, review])

# Write the data to a CSV file
with open('data/input/appointments.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['user_id', 'patient_name', 'patient_age', 'patient_gender', 'doctor_id', 'doctor_name',
                     'doctor_specialty', 'appointment_date', 'appointment_time', 'medical_condition', 'rating', 'review'])
    writer.writerows(data)

print("Data generated and saved to appointments.csv")
