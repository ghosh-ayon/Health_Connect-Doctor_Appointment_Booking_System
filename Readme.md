Doctor-Appointment-Booking-System using AI _ Version - 2.3.0 (Made by Biswadeb Mukherjee) 
│
├── .git/                 # Git repository directory (created when you initialize a repository)
├── .gitignore            # Git ignore file to specify which files and directories to exclude from version control
│
├── app/                  # Application code and configuration
│   ├── app.py            # Your Flask application
│   ├── config.py         # Database Configuration settings
│   ├── secret.py         # Secret key generator needed for the Flask web app
│   ├── requirements.txt  # List of Python dependencies
│
├── static/               # Static files (CSS, JavaScript, images)
│   ├── assets/           # Contain all css files, picture, needed for default page
│   ├── admin.css         # CSS styles for the admin dashboard
│   ├── admin.js
│   
├── templates/            # HTML templates
│   ├── home.html         # default Page
│   ├── login.html        # Patient's login Template
│   ├── register.html     # Patient's register Template
│   ├── patient.html      # Patient's dashboard Template
│   ├── booking.html      # Appointment booking Template
│   ├── recommend.html    # Recommendation result Template (if needed)
│   ├── token.html        # For generating Patient's token
|
├── recommendation/       # Appointment Recommendation System
│   ├── data/             # Data for recommendation (real-world or synthetic)
│   ├── recommendation_model.py  # Model for appointment recommendations
|
├── trainer.py            # For training the model
|
├── docs/                 # Documentation
│   ├── README.md         # Project documentation
|
├── README.md             # Project summary and setup instructions
