from flask import Flask, send_from_directory, request
import datetime
import json

app = Flask('bootcamp-demo')

allMessages = []

@app.route('/')
def index():
    return send_from_directory('./static', 'index.html')

@app.route('/sms', methods=['GET','POST'])
def message():
    number = request.values.get('From')
    message = request.values.get('Body')
    allMessages.append({
        'number': number,
        'message': message,
        'timestamp': datetime.datetime.now().strftime('%H:%M:%S')
    })
    return ""

@app.route('/data')
def data():
    return json.dumps(allMessages)

@app.route('/clear')
def clear():
    del allMessages[:]
    return json.dumps(allMessages)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')