Doctor-Appointment-Booking-System using AI _ Version - 2.3.0 (Made by Biswadeb Mukherjee) 
│
├── .git/               # Git repository directory (created when you initialize a repository)
├── .gitignore          # Git ignore file to specify which files and directories to exclude from version control
│
├── app.py              # Your Flask application for handling web requests and responses
│
├── recommendation/     # Module for appointment recommendation system
│   ├── bi_lstm_model.h5         # Trained Bi-LSTM model file
│   ├── tokenizer.pkl            # Tokenizer object for text preprocessing
│   ├── label_encoder.pkl        # Label encoder object for doctor specialty encoding
│   ├── decision.py              # Decision-making module using Bi-LSTM model
│
├── static/             # Static files (CSS, JavaScript, images)
│   ├── admin.css       # CSS styles for the admin dashboard
│   ├── pictures/       # Images
│       ├── logo.png    # Site logo
│
├── templates/          # HTML templates
│   ├── login.html      # Patient's login Template
│   ├── register.html   # Patient's register Template
│   ├── patient.html    # Patient's dashboard Template
│   ├── booking.html    # Appointment booking Template
│   ├── recommend.html  # Recommendation result Template (if needed)
│
├── trainer/            # Module for training the Bi-LSTM model
│   ├── trainer.py             # Script for loading, preprocessing, training, and saving the Bi-LSTM model
│   ├── data.csv               # Dataset for training the model (patient conditions and corresponding doctors)
│
├── README.md           # Project documentation
├── requirements.txt    # List of Python dependencies
