"""Author: Harshada Tupe"""

# Third party library imports
from flask import Flask, jsonify, request

# Local application imports
from camera import Camera
from notifications import send_notification
from storage import get_videos


app = Flask(__name__)
camera = Camera()

@app.route('/arm', methods=['POST'])
def arm():
    camera.arm()
    return jsonify(message="System armed."), 200

@app.route('/disarm', methods=['POST'])
def disarm():
    camera.disarm()
    return jsonify(message="System disarmed."), 200

@app.route('/get-armed', methods=['GET'])
def get_armed():
    return jsonify(armed=camera.armed), 200

@app.route('/motion_detected', methods=['POST'])
def motion_detected():
    data = request.get_json()

    if 'url' in data:
        print("URL: ", data['url'])
        send_notification(data["url"])
    else:
        print("'url' not in incoming data")

    return jsonify({}), 201

@app.route("/get-logs")
def get_logs():
    logs = get_videos()
    return jsonify({"logs": logs}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

