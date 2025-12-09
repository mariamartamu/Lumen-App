from flask import Flask, session, redirect, request
import secrets, urllib.parse

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/login")
def login():
    state = secrets.token_urlsafe(16)
    session['oauth_state'] = state
    params = {
        'client_id': '2e5g6fhuebrda5809pf2k7at4n',
        'response_type': 'code',
        'scope': 'email openid phone',
        'redirect_uri': 'http://localhost:5000/callback',
        'state': state
    }
    url = "https://us-east-2cgam6s9zx.auth.us-east-2.amazoncognito.com/login?" + urllib.parse.urlencode(params)
    return redirect(url)

@app.route("/callback")
def callback():
    state = request.args.get('state')
    if state != session.get('oauth_state'):
        return "Error: Invalid state", 400
    return "Authenticated successfully!"

if __name__ == "__main__":
    app.run(debug=True)
