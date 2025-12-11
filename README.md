📘 Lumen Wellness — Personal Wellness Tracking Web App

A full-stack health & wellness tracker built with Python, Flask, AWS, and Render.

🌟 Overview

Lumen Wellness is a personal wellness tracking platform designed to help users monitor daily habits such as weight, sleep, water intake, and exercise. Users can create an account, build a personalized profile, upload a profile picture, view other user profiles, and track their own health analytics over time.

This project was developed as part of my MPS in Analytics program at Northeastern University to demonstrate skills in web development, data engineering, user authentication, cloud deployment, and interactive data collection.

🚀 Live Demo

🔗 App URL: https://lumen-app.onrender.com/

(Hosted on Render — may take a few seconds to wake up)

🧠 Key Features
👤 User Accounts & Authentication

Secure signup + login system

Password hashing

Session-based user management

📝 Profile Management

Extended user profile (age, gender, goals, preferences, etc.)

Profile photo upload (local or mobile gallery)

Clean, user-friendly profile form with validation

🧪 Wellness Tracking

Users can log and track:

Daily weight

Hours of sleep

Water intake

Exercise activity

Data is stored and tied to each user, enabling future analytics dashboards.

👥 Community Profiles Deck

Users can view other user cards (similar to a browsing deck)

Not a dating/swiping app — simply a discovery feature for the community

Displays profile picture, username, goals, and wellness summary

💳 Subscription & Free Trial (In Progress)

7-day free trial button integrated into UI

Planned payment integration via Stripe

☁️ Cloud Deployment

Backend hosted on Render

Static storage + profile images prepared for AWS S3 integration

Environment variables secured in deployment

🛠 Tech Stack
Backend

Python 3

Flask

Jinja Templates

Werkzeug (auth + security)

Frontend

HTML

CSS

Jinja templating engine

Database

SQLite (local development)

Ready for migration to PostgreSQL on Render

Cloud & Deployment

Render (hosting)

AWS S3 (image storage – planned)

GitHub Actions (version control)

📂 Project Structure
Lumen-App/
│
├── app.py                # Main Flask application
├── lumen_auth.py         # Authentication, login logic, session handler
├── dashboard.txt         # Future analytics dashboard planning
├── templates/            # HTML templates (Jinja)
│   ├── index.html
│   ├── profile.html
│   ├── login.html
│   ├── signup.html
│   └── community.html
│
├── requirements.txt      # Dependencies for Render deployment
├── Procfile.txt          # Render startup instructions
└── README.md             # Project documentation

📦 Installation (Local Development)
1. Clone the Repository
git clone https://github.com/mariamartamu/Lumen-App.git
cd Lumen-App

2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the App
python app.py


Open in your browser:
http://127.0.0.1:5000

📊 Future Enhancements

📈 Interactive analytics dashboard (weight, sleep, hydration trends)

🗂 User-to-user messaging system

☁️ Full AWS S3 integration for media uploads

🔐 OAuth login (Google Accounts)

💸 Subscription billing via Stripe

📱 Responsive mobile UI redesign

👩‍💻 About the Developer

Maria Menendez
MPS in Analytics, Northeastern University
Specializing in applied machine learning, cloud solutions, and full-stack development.
Passionate about building user-centric applications that combine data, design, and real-world impact.

🤝 Contributions

This project is open for feedback and suggestions.
Feel free to email me or open an issue in the repo.
