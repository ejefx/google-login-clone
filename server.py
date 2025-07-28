from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
    return jsonify ({'message': 'Credentials received'})
if__name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)