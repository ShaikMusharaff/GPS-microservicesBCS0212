from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/location', methods=['GET'])
def location():
    data = {
        "classroom": "Cloud Lab",
        "latitude": 9.5916,
        "longitude": 76.5222
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)