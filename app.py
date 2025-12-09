from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime, timedelta
import os
import uuid
import requests
import base64

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# ==== AWS Cognito Configuration (from environment variables) ====
COGNITO_DOMAIN = os.environ.get("COGNITO_DOMAIN")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")
LOGOUT_REDIRECT_URI = os.environ.get("LOGOUT_REDIRECT_URI")
REGION = os.environ.get("REGION")
SCOPES = "openid+profile+email"

# ==== Trial Logic ====
TRIAL_PERIOD_DAYS = 7

def is_trial_valid():
    signup_time = session.get('signup_time')
    if not signup_time:
        return False
    signup_time = datetime.strptime(signup_time, '%Y-%m-%d %H:%M:%S')
    return datetime.now() < signup_time + timedelta(days=TRIAL_PERIOD_DAYS)

# ==== Routes ====

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    state = str(uuid.uuid4())
    session['oauth_state'] = state
    login_url = (
        f"{COGNITO_DOMAIN}/login?"
        f"client_id={CLIENT_ID}&"
        f"response_type=code&"
        f"scope={SCOPES}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"state={state}"
    )
    return redirect(login_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if state != session.get('oauth_state'):
        return "Invalid state", 400

    token_url = f"{COGNITO_DOMAIN}/oauth2/token"
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_header}"
    }

    response = requests.post(token_url, data=token_data, headers=headers)

    if response.status_code != 200:
        return f"Failed to get token: {response.text}", 400

    token_response = response.json()
    session['id_token'] = token_response.get("id_token")

    if 'signup_time' not in session:
        session['signup_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return redirect(url_for('profile'))

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if 'id_token' not in session:
        return redirect(url_for('login'))

    if request.method == "POST":
        session['user'] = {
            'name': request.form.get('name'),
            'age': request.form.get('age'),
            'bio': request.form.get('bio'),
            'goals': request.form.get('goals'),
            'interests': request.form.get('interests'),
            'profile_pic_url': request.form.get('profile_pic_url') or "https://via.placeholder.com/100"
        }
        return redirect(url_for('dashboard'))

    return render_template("profile.html", user=session.get('user', {}))

@app.route("/dashboard")
def dashboard():
    if 'id_token' not in session:
        return redirect(url_for('login'))

    if not is_trial_valid():
        return "Your 7-day trial has expired. Please subscribe to continue.", 403

    user = session.get('user')
    if not user or not user.get("name") or not user.get("age"):
        return redirect(url_for("profile"))

    signup_time = datetime.strptime(session.get('signup_time'), '%Y-%m-%d %H:%M:%S')
    days_left = (signup_time + timedelta(days=TRIAL_PERIOD_DAYS) - datetime.now()).days

    return render_template("dashboard.html", days_left=days_left, user=user)

@app.route("/logout")
def logout():
    session.clear()
    logout_url = (
        f"{COGNITO_DOMAIN}/logout?"
        f"client_id={CLIENT_ID}&"
        f"logout_uri={LOGOUT_REDIRECT_URI}"
    )
    return redirect(logout_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
