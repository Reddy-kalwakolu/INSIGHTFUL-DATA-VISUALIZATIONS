from flask import Flask, request, jsonify, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    row = [name, email, message]

    file_exists = os.path.isfile('messages.csv')
    with open('messages.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Email', 'Message'])
        writer.writerow(row)

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
