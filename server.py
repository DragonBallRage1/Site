from flask import Flask, request, jsonify

app = Flask(__name__)

status = "Disconnected"
text = ""

@app.route('/connect', methods=['POST'])
def connect():
    global status
    status = "Attached"
    return jsonify({"status": status})

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": status})

@app.route('/text', methods=['POST'])
def update_text():
    global text
    text = request.json.get('text', '')
    return jsonify({"text": text})

@app.route('/text', methods=['GET'])
def get_text():
    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
