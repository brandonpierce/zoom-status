import json
import redis
import time

from flask import Flask, request, jsonify

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_zoom_status():
    retries = 5
    while True:
        try:
            return cache.get('status')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def set_zoom_status(s):
    retries = 5
    while True:
        try:
            return cache.set('status', s)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# /
@app.route('/', methods=['GET'])
def index():
    return 'zoom'

# /zoom
@app.route('/zoom', methods=['GET'])
def get_status():
    status = get_zoom_status().decode('utf-8')
    return jsonify({'status': status})


@app.route('/zoom', methods=['PUT'])
def set_status():
    r = json.loads(request.data)
    status = r['status']
    set_zoom_status(status)
    return jsonify({'status': status})


# /health
@app.route('/health', methods=['GET'])
def health():
    return jsonify('{OK}')


app.run(debug=True)