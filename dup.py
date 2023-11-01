from faker import Faker
import random
from datetime import datetime, timedelta
import csv

fake = Faker()

# Define a function to generate a random doctor's appointment
def generate_appointment():
    appointment_date = fake.date_between(start_date="-30d", end_date="+30d")
    appointment_time = fake.time_object()
    patient_name = fake.name()
    doctor_name = fake.name()
    specialty = fake.random_element(elements=("Cardiology", "Dermatology", "Pediatrics", "Orthopedics", "Neurology"))
    location = fake.address()

    return {
        "Appointment Date": appointment_date,
        "Appointment Time": appointment_time.strftime("%H:%M"),
        "Patient Name": patient_name,
        "Doctor Name": doctor_name,
        "Specialty": specialty,
        "Location": location,
    }

# Generate a list of doctor's appointments
num_appointments = 100000  # You can change this to the desired number of appointments
appointments = [generate_appointment() for _ in range(num_appointments)]

# Save the generated data to a CSV file
csv_file = "doctor_appointments.csv"

with open(csv_file, "w", newline="") as file:
    fieldnames = [
        "Appointment Date",
        "Appointment Time",
        "Patient Name",
        "Doctor Name",
        "Specialty",
        "Location",
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    for appointment in appointments:
        writer.writerow(appointment)

print(f"Doctor's appointments data saved to {csv_file}.")
