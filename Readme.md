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
│   ├── admin.css         # CSS styles for the admin dashboard
│   ├── pictures/         # Images
│       ├── logo.png      # Site logo
│
├── templates/            # HTML templates
│   ├── login.html        # Patient's login Template
│   ├── register.html     # Patient's register Template
│   ├── patient.html      # Patient's dashboard Template
│   ├── booking.html      # Appointment booking Template
│   ├── recommend.html    # Recommendation result Template (if needed)
|
├── recommendation/       # Appointment Recommendation System
│   ├── data/             # Data for recommendation (real-world or synthetic)
│   ├── recommendation_model.py  # Model for appointment recommendations
|
├── decision/              # Decision-making module
│   ├── decision_maker.py # Module for decision-making algorithm
|
├── docs/                  # Documentation
│   ├── README.md         # Project documentation
|
├── README.md             # Project summary and setup instructions
